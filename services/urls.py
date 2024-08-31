from django.urls import path,include


from . import views

urlpatterns = [
    path("services/",views.get_all_services,name="services"),
    path("locations/",views.get_all_locations,name="locations"),
    path("events/",views.get_all_events,name="events"),
    path("events/<str:pk>/",views.get_event_detail,name="events-detail"),

    path("knowledges/",views.get_all_knowledges,name="knowledges"),
    path("knowledges/<str:pk>/",views.get_knowledge_detail,name="knowledges-detail"),

]