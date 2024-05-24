from django.shortcuts import render

# class AdminOnlyMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
        
#     def __call__(self,request):
#         if request.user.is_authenticated :
#             return render(request,'Get_A_Job_S1/erreur_admin.html',status=403)
        
#         return self.get_response(request)