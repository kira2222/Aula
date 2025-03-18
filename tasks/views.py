from django.shortcuts import render,redirect
from .forms import TaskForm
from . models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




# Esta función es llamada cuando el usuario quiere ver las tareas
@login_required
def task_list(request):
    # Obtener todas las tareas relacionadas con el usuario logueado
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos del request
        form = TaskForm(request.POST)

        if form.is_valid():
            # Crear una instancia del modelo Task con los datos del formulario
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                date_created=form.cleaned_data['date_created'],
                date_limit=form.cleaned_data['date_limit'],
                priot=form.cleaned_data['priot']
            )

            return redirect('home')

    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


# Esta función es llamada cuando el usuario quiere editar una tarea
@login_required
def task_update(request, task_id):
    # Obtener la tarea a editar a partir de su ID
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid(): 
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.date_created = form.cleaned_data['date_created']
            task.date_limit = form.cleaned_data['date_limit']
            task.priot = form.cleaned_data['priot']
            task.save()  # Guarda los cambios en la base de datos
            return redirect('home')
        
    else:
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'date_created': task.date_created,
            'date_limit': task.date_limit,
            'priot': task.priot
        })
                
        return render(request, 'task_form.html', {'form': form})
    

# Esta función es llamada cuando el usuario quiere eliminar una tarea
@login_required
def task_delete(request,task_id):
    # Obtener la tarea a eliminar a partir de su ID
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

# Esta función es llamada cuando el usuario quiere cerrar sesión
def logout_view(request):
    # Cerrar la sesión del usuario
    logout(request)
    return redirect('/')