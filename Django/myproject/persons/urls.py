from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addperson/', views.addperson, name='addperson'),
    path('update/<int:x>', views.update, name='upd'),
    path('update/updatePerson/<int:x>', views.updatePerson, name='updperson'),
    path('delete/<int:x>', views.delete, name='del'),
    
]

urlpatterns += staticfiles_urlpatterns()
