""" 
Views for CAVE Language
"""
from cavelanguage.utils import template
from cavelanguage.models import Symbol, Collection, Category, Diagram, Contributor

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
    connector_symbols = Symbol.objects.active().filter(collection__name='Core',categories__name='Connectors')
    data_symbols = Symbol.objects.active().filter(collection__name='Core',categories__name='Data')
    context_symbols = Symbol.objects.active().filter(collection__name='Core',categories__name='Context')
    conditional_symbols = Symbol.objects.active().filter(collection__name='Core',categories__name='Conditionals')
    mode_symbols = Symbol.objects.active().filter(collection__name='Core',categories__name='Modes')
    container_symbols = Symbol.objects.active().filter(collection__name='Core',categories__name='Containers')
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
    sym = Symbol.objects.active().get(slug=slug)
    return {'symbol':sym,'location':'symbol_library'}

@template('collection.html')
def collection(request,slug):
    """ 
    Gets the collection.
    """
    col = Collection.objects.get(slug=slug)
    return {'collection':col,'location':'symbol_library'}

@template('category.html')
def category(request,collection_slug,slug):
    """ 
    Gets the category.
    """
    cat = Category.objects.get(slug=slug)
    return {'category':cat,'location':'symbol_library'}

@template('diagram.html')
def diagram(request,diagram_id,diagram_slug):
    """
    Gets the diagram.
    """
    diagram = Diagram.objects.get(pk=diagram_id)
    return {'diagram':diagram,'location':'diagrams'}

@template('diagrams.html')
def diagrams(request):
    """
    Main diagrams page.
    """
    return {'location':'diagrams','diagrams':Diagram.objects.all()}

@template('contributors.html')
def contributors(request):
    """
    Contributors to CAVE.
    """
    return {'location':'contributors','contributors':Contributor.objects.all()}

