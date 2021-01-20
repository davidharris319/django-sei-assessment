from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/delete/', views.WidgetDelete.as_view(), name='widget_delete'),
]
