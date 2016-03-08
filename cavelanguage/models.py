"""
Models for cavelanguage.org.
"""
from django.db import models
from djax.content import ACEContent

class Collection(models.Model):
    """
    Overall collection (core, or an extension) of symbols.
    """
    name = models.CharField(unique=True, max_length=100)
    
    def __unicode__(self):
        return self.name

class Category(models.Model):
    """
    A category of symbols within a collection.
    """
    collection = models.ForeignKey(Collection,related_name='categories')
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = (('collection','name'),)

class Symbol(models.Model,ACEContent):
    """
    A diagram symbol.
    """
    collection = models.ForeignKey(Collection,related_name='symbols')
    name = models.CharField(unique=True, max_length=100)
    categories = models.ManyToManyField(Category,related_name='symbols')
    url = models.URLField(null=True)
    
    def __unicode__(self):
        return self.name
    
    def _get_collection(self):
        return self.collection.name
    
    def _set_collection(self,collection_name):
        self.collection = Collection.objects.get(name=collection_name)
    
    collection_prop = property(_get_collection,_set_collection)
    
    def _get_categories(self):
        return [category.name for category in self.categories.all()]
    
    def _set_categories(self,category_names):
        self.categories = Category.objects.filter(name__in=category_names)
    
    categories_prop(_get_categories,_set_categories)
    
    class ACE:
        content_type = 'Symbol'
        field_map = {
            'collection':'collection_prop',
            'categories':'categories_prop',
            'name':'name',
            'url':'url'
        }
