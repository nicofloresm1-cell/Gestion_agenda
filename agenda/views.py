# agenda/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm # Importamos el formulario de registro

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

# --- Vistas de Tareas (Las que ya teníamos) ---

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'agenda/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    template_name = 'agenda/task_form.html'
    success_url = reverse_lazy('agenda:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority', 'completed']
    template_name = 'agenda/task_form.html'
    success_url = reverse_lazy('agenda:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'agenda/task_confirm_delete.html'
    success_url = reverse_lazy('agenda:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# --- Vista de Registro (ESTA ES LA NUEVA FUNCIÓN) ---

def signup(request):
    """
    Vista para registrar nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Inicia sesión automáticamente al usuario
            return redirect('agenda:task_list') # Redirige a la lista de tareas
    else:
        form = UserCreationForm()
    
    # Usará un template en 'registration/signup.html'
    return render(request, 'registration/signup.html', {'form': form})