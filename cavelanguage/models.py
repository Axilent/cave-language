"""
Models for cavelanguage.org.
"""
from django.db import models
from djax.content import ACEContent, M2MFieldConverter
from django.utils.text import slugify

class Collection(models.Model):
    """
    Overall collection (core, or an extension) of symbols.
    """
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)
    
    def __unicode__(self):
        return self.name

class Category(models.Model):
    """
    A category of symbols within a collection.
    """
    collection = models.ForeignKey(Collection,related_name='categories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (('collection','name'),)
        ordering = ['name']

class SymbolCategoryFieldConverter(object):
    """ 
    Field converter for symbol categories.
    """
    field = 'categories'
    deferred = True
    
    def to_local_model(self,ace_content,ace_field_value,local_model):
        categories = Category.objects.filter(name__in=ace_field_value)
        local_model.categories = categories
        local_model.save()
        return categories
    
    def to_ace(self,local_model):
        return [category.name for category in local_model.categories.all()]

class Symbol(models.Model,ACEContent):
    """
    A diagram symbol.
    """
    collection = models.ForeignKey(Collection,related_name='symbols')
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField()
    categories = models.ManyToManyField(Category,related_name='symbols')
    url = models.URLField(null=True,max_length=500)
    description = models.TextField(blank=True,null=True)
    proposed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
    def _get_collection(self):
        return self.collection.name
    
    def _set_collection(self,collection_name):
        self.collection = Collection.objects.get(name=collection_name)
    
    collection_prop = property(_get_collection,_set_collection)
    
    def _get_proposed(self):
        return 'Proposed' if self.proposed else 'Accepted'
    
    def _set_proposed(self,value):
        if value == 'Proposed':
            self.proposed = True
        else:
            self.proposed = False
    
    proposed_prop = property(_get_proposed,_set_proposed)
    
    class ACE:
        content_type = 'Symbol'
        field_map = {
            'collection':'collection_prop',
            'categories':SymbolCategoryFieldConverter(),
            'name':'name',
            'url':'url',
            'slug':'slug',
            'description':'description',
            'proposed':'proposed_prop',
        }
    
    class Meta:
        ordering = ['name']

class Diagram(models.Model,ACEContent):
    """
    A CAVE diagram.
    """
    name = models.CharField(max_length=100)
    symbols = models.ManyToManyField(Symbol,related_name='diagrams')
    image = models.URLField(max_length=500)
    download = models.URLField(null=True,max_length=500)
    discussion = models.TextField(blank=True,null=True)
    
    def __unicode__(self):
        return self.name
    
    @property
    def slug(self):
        """
        Slug version of diagram name.
        """
        return slugify(self.name)
    
    class ACE:
        content_type = 'Diagram'
        field_map = {
            'name':'name',
            'image':'image',
            'download':'download',
            'symbols':M2MFieldConverter('symbols'),
            'discussion':'discussion',
        }
    
    class Meta:
        ordering = ['name']

class Article(models.Model,ACEContent):
    """
    An article about CAVE.
    """
    title = models.CharField(unique=True,max_length=100)
    body = models.TextField(blank=True)
    diagrams = models.ManyToManyField(Diagram,related_name='articles')
    
    def __unicode__(self):
        return self.title
    
    class ACE:
        content_type = 'Article'
        field_map = {
            'title':'title',
            'body':'body',
            'diagrams':M2MFieldConverter('diagrams')
        }
