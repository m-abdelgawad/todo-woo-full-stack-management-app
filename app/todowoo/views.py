from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import TodoForm, NewUserForm, UserLoginForm
from .models import Todo


# Create your views here.
def signup_user(request):
    if request.method == 'GET':
        return render(request, 'todowoo/auth/signup_user.html',
                      {'form': NewUserForm(), })
    else:

        form = NewUserForm(request.POST)

        if form.is_valid():

            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                )
                # The previous function just creates a User object and doesn't
                # save it into the database. We have to save it by using the
                # following line
                user.save()

                # Create the To do-Woo group if it doesn't exists and Add the
                # new user to the group
                group_name = 'Todo-Woo'
                groups_list = [group.name for group in Group.objects.all()]
                if group_name in groups_list:
                    todowoo_group = Group.objects.get(name=group_name)
                else:
                    todowoo_group = Group.objects.create(name=group_name)

                todowoo_group.user_set.add(user)

                # After creating the user, we want to log them into their new
                # account. Then, redirect them to their to do list..
                login(request, user)
                return redirect('todowoo:todos_list')

            except IntegrityError as e:
                return render(request, 'todowoo/auth/signup_user.html',
                              {'form': form, 'error': str(e)})
        else:

            return render(request, 'todowoo/auth/signup_user.html',
                          {'form': form})


@login_required(login_url='login/')
def logout_user(request):
    # It is super important to only execute this function if the request is
    # POST request.
    if request.method == 'POST':
        logout(request)
        return redirect('todowoo:home')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todowoo/auth/login_user.html',
                      {'form': UserLoginForm()})
    else:

        form = UserLoginForm(data=request.POST)

        if form.is_valid():

            user = authenticate(request, username=request.POST['username'],
                                password=request.POST['password'])

            # If the user is authenticated correctly
            login(request, user)
            return redirect('todowoo:todos_list')

        else:
            form = UserLoginForm(data=request.POST)
            return render(request, 'todowoo/auth/login_user.html',
                          {'form': form})


def home(request):
    return render(request, 'todowoo/home.html')


@login_required(login_url='login/')
def todos_list(request):
    todos = Todo.objects.filter(author=request.user, completed__isnull=True)
    return render(request, 'todowoo/todos_list.html', {'todos': todos})


@login_required(login_url='login/')
def completed_todos(request):
    todos = Todo.objects.filter(
        author=request.user, completed__isnull=False
    ).order_by('-completed')
    return render(request, 'todowoo/completed_todos.html', {'todos': todos})


@login_required(login_url='login/')
def create_todo(request):
    if request.method == 'POST':
        try:
            form = TodoForm(request.POST)

            if form.is_valid():
                # Create a new to-do object but don't save it in the database yet;
                # because it's missing the user field
                new_todo = form.save(commit=False)

                # Add the logged-in user to the new to-do object
                new_todo.author = request.user

                # Save the new to-do to the database
                new_todo.save()

                # Send the user to their todos list
                return redirect('todowoo:todos_list')

        except ValueError:
            return render(request, 'todowoo/create_todo.html',
                          {'form': TodoForm(), 'error': 'Bad data passed in. Try again.'})
    else:
        form = TodoForm()

    return render(request, 'todowoo/create_todo.html', {'form': form})


@login_required(login_url='login/')
def view_todo(request, todo_pk):
    # pk is the primary key that shows in the admin URL of that object
    # We specified the user in the below function; because if the user tries
    # to access an object that doesn't belong to them; return 404
    todo = get_object_or_404(Todo, pk=todo_pk, author=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todowoo/view_todo.html',
                      {'todo': todo, 'form': form})
    else:
        # Because the form was already populated with the user and all required
        # fields, we can go ahead and save it.
        try:
            # We have to pass the instance to-do that we need to update; to let
            # Django know that this is already an object
            form = TodoForm(request.POST, instance=todo)
            form.save()
            # Send the user to their todos list
            return redirect('todowoo:todos_list')
        except ValueError:
            return render(request, 'todowoo/create_todo.html',
                          {'form': TodoForm(),
                           'error': 'Bad data passed in. Try again.'})


@login_required(login_url='login/')
def complete_todo(request, todo_pk):
    print('hii')
    todo = get_object_or_404(Todo, pk=todo_pk, author=request.user)
    if request.method == 'POST':
        todo.completed = timezone.now()
        todo.save()
        # Send the user to their todos list
        return redirect('todowoo:todos_list')


@login_required(login_url='login/')
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, author=request.user)
    if request.method == 'POST':
        todo.delete()
        # Send the user to their todos list
        return redirect('todowoo:todos_list')
