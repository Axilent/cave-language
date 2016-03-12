""" 
Views for CAVE Language
"""
from cavelanguage.utils import template

@template('home.html')
def home(request):
    """ 
    Home page.
    """
    