from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

urlpatterns =[
    #-------------ALL VIEWS-----------------------
    path('all/',views.all,name='all_lawyers'),
    path('allS/',views.allS,name='all_Specialization'),
    #-------------FILTER VIEWS-----------------------
    path('llawyers/<str:pk>/',views.location,name="locations_lawyers"),
    path('nlawyers/<str:pk>/',views.ncasetype,name="case_type_lawyers"),
    #-------------SPECIFIC VIEWS-----------------------
    path('lawyer/<str:pk>/',views.lawyer,name="lawyer"),
    path('specialization/<str:pk>/',views.specialization,name="specialization"),
    #-------------ADD---------------------------------
    path('addlawyer/',views.addlawyer,name="addlawyer"),
    path('addSpecialization/',views.addSpecialization,name="add_Specialization"),
    #-------------DELETE------------------------------
    path('deletelawyer/<str:pk>',views.deletelawyer,name="delete_lawyer"),
    path('deleteSpecialization/<str:pk>',views.deleteSpecilization,name="delete_Specialization"),
    #-------------UPDATE-------------------------------
    path('updateLawyer/<str:pk>/',views.updateLawyer,name="update_Lawyer"),
    path('updateSpecialization/<str:pk>/',views.updateSpecialization,name="update_Specialization"),

]