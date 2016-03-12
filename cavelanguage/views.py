""" 
Views for CAVE Language
"""
from cavelanguage.utils import template
from cavelanguage.models import Symbol, Collection, Category

@template('home.html')
def home(request):
    """ 
    Home page.
    """
    pass # TODO

@template('symbol.html')
def symbol(request,slug):
    """ 
    Shows the symbol.
    """
    sym = Symbol.objects.get(slug=slug)
    return {'symbol':sym}

@template('collection.html')
def collection(request,slug):
    """ 
    Gets the collection.
    """
    col = Collection.objects.get(slug=slug)
    return {'collection':col}

@template('category.html')
def category(request,slug):
    """ 
    Gets the category.
    """
    cat = Category.objects.get(slug=slug)
    return {'category':cat}
