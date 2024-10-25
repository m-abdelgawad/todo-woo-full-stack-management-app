from django.urls import path

from . import views

app_name = 'todowoo'

urlpatterns = [
    # Auth
    path('signup/', views.signup_user, name='signup_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('login/', views.login_user, name='login_user'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create_todo'),
    path('todos_list/', views.todos_list, name='todos_list'),
    path('completed_todos/', views.completed_todos, name='completed_todos'),
    path('todo/<int:todo_pk>', views.view_todo, name='view_todo'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='complete_todo'),
    path('todo/<int:todo_pk>/delte', views.delete_todo, name='delete_todo'),

]
