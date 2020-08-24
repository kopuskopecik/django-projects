from django.http import JsonResponse

from .limit import Limit


def rate_limit(function):
    """
    if a user makes more than 10 requests in 10 seconds, 
    it returns the appropriate error message.
    """
    def wrap(request, *args, **kwargs):
        rate_limit = Limit(request)
        overflow = rate_limit.check()
        if overflow:
            return JsonResponse({'status':'false','message':"Oopss! Slow down"}, status=500)
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap