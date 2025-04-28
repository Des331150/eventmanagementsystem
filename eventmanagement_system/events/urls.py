from . import views
from django.urls import path

app_name = "events"
urlpatterns = [
    path('events/create/', views.create_event, name="create_event"),
    path('events/', views.list_event, name="list_event"),
    path('events/<int:pk>/', views.retrieve_event, name="retrieve_event"),
    path('events/update/<int:pk>/', views.update_event, name="update_event"),
    path('events/delete/<int:pk>/', views.delete_event, name="delete_event"),

    path('registrations/create/', views.create_registration, name="create_registration"),
    path('registrations/', views.list_registration, name="list_registration"),
    path('registrations/<int:pk>/', views.retrieve_registration, name="retrieve_registration"),
    path('registrations/update/<int:pk>/', views.update_registration, name="update_registration"),
    path('registrations/delete/<int:pk>/', views.delete_registration, name="delete_registration")
]
