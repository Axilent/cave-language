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
    return {'location':'home'}

@template('symbol_library.html')
def symbol_library(request):
    """ 
    The main symbol library.
    """
    connector_symbols = Symbol.objects.filter(collection__name='Core',categories__name='Connectors')
    data_symbols = Symbol.objects.filter(collection__name='Core',categories__name='Data')
    context_symbols = Symbol.objects.filter(collection__name='Core',categories__name='Context')
    conditional_symbols = Symbol.objects.filter(collection__name='Core',categories__name='Conditionals')
    mode_symbols = Symbol.objects.filter(collection__name='Core',categories__name='Modes')
    container_symbols = Symbol.objects.filter(collection__name='Core',categories__name='Containers')
    return {'location':'symbol_library',
            'connector_symbols':connector_symbols,
            'data_symbols':data_symbols,
            'context_symbols':context_symbols,
            'conditional_symbols':conditional_symbols,
            'mode_symbols':mode_symbols,
            'container_symbols':container_symbols}

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
