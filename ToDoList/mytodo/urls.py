
from django.urls import path
from . import views
app_name = 'mytodo'
urlpatterns = [
    path('',views.main,name='main'),
    path('<int:id>/',views.detail,name='detail'),
    path('add/',views.add_task,name='add_task')
]