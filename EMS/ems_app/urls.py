from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name= 'home'),
    path('new_emp', views.new_emp, name = 'new_emp'),
    path('edit_emp/<int:id>', views.edit_emp, name = 'edit_emp'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
]
