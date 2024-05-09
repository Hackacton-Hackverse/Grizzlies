from django.shortcuts import render

class AdminOnlyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        if request.user.is_authenticated and not request.user.is_superuser:
            return render.render(request,'erreur_admin.html',status=403)
        
        return self.get_response(request)