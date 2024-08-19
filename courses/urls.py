from django.urls import path,include


from . import views

urlpatterns = [
    path("universities/",views.get_all_universities,name="universities"),
    path("programs/",views.get_all_programs,name="programs"),
    path("programs/<str:pk>/",views.get_programs_detail,name="program_detail"),
    path("universities/<str:pk>/",views.get_university_detail,name="university_detail")
]