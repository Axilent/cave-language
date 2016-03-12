"""
General utils for CAVE Language.
"""

# ===============================
# = Decorator to simplify views =
# ===============================
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import uuid
import logging
import traceback

log = logging.getLogger('cave.utils')

def template(template_name):
    """
    Parameterized decorator to allow a view to return a context dictionary as a response.
    The decorator will place the dictionary in a RequestContext wrapper, and return using
    the template specified in the parameter.
    """
    def function_builder(func):
        def view(request,*args,**kwargs):
            response = func(request,*args,**kwargs)
            if isinstance(response,HttpResponse):
                return response
            elif response == 'OK':
                return HttpResponse('OK')
            else:
                return render_to_response(template_name,response,context_instance=RequestContext(request))
        return view
    return function_builder

def get_module(module_name):
    """
    Imports and returns the named module.
    """
    module = __import__(module_name)
    components = module_name.split('.')
    for comp in components[1:]:
        module = getattr(module,comp)
    return module

def get_function(module_name,function_name):
    """
    Imports and returns the named function in the specified module.
    """
    module = get_module(module_name)
    return getattr(module,function_name)

def gf(function_path):
    """
    Shortcut to get function.
    """
    module_name, function_name = function_path.rsplit('.',1)
    return get_function(module_name,function_name)

def random_hex():
    """
    Returns a random hex string.
    """
    return uuid.uuid4().hex

def catch(func):
    """
    Catches any exception and prints a stack trace.
    """
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except:
            log.exception('Exception while executing function %s' % str(func))
            traceback.print_exc()

    return wrapper