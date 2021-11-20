
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('remove/<int:todo_id>',views.remove),
    path('mark_complete/<int:todo_id>',views.mark_complete),
    path('add_todo',views.create_todo),
]
