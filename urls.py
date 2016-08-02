from django.conf.urls import url, include
from django.contrib import admin
from . import views

import TesseractBoxEditor

app_name = 'TesseractBoxEditor'
urlpatterns = [
    url(r'^', TesseractBoxEditor.views.tbe, name='tbe'),
]