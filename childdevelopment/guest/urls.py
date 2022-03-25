from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index)'),
    path('vue-test', views.vue_test, name='vue_test'),
]