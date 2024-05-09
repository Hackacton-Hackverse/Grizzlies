from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def admin_required(function):
    """Permet de vérifier si l'utilisateur actuel (request.user)
    est un super-utilisateur(administrateur) .s'il ne l'est pas
    une exception PermissionDenied est levée.

    
    """
    def wrap(request, *args,**kwargs):
        if not request.user.is_superuser :
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return wrap
