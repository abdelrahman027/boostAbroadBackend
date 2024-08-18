from django.urls import path,include


from . import views

urlpatterns = [
    path("universities/",views.get_all_universities,name="universities"),
]