from django.urls import path,include


from . import views

urlpatterns = [
    path("services/",views.get_all_services,name="services"),
]