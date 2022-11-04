from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='person_add'),
  	path('ajax/load_breed/', views.load_breed, name='ajax_load_breed'), # AJAX
   	path('delete_item/<int:id>',views.delete_item,name="delete_item"),
]