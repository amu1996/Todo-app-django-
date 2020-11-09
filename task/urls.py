from django.urls import path
from . import views as tview
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',tview.index, name='home'),
    path('delete_task/<str:pk>',tview.deleteTask,name='delete_task'),
    path('update_task/<str:pk>/',tview.updateTask,name='update_task'),
]