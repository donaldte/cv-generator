from django.urls import path
from pdf.views import index, form, viewcv

urlpatterns =[
    path('', index, name='resume'),
    path('creercv', form, name="formulaire"),
    path('<int:id>', viewcv, name="generer"),
]