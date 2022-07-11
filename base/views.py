from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

class TodoListLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterTodoApp(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        #ユーザーが正常に作成されたら
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    # Listviewの関数を使用している。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        # context['color'] = "red"
        context['tasks'] = context["tasks"].filter(user=self.request.user)
        # context['count'] = context["tasks"].filter(completed=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input) #icontains

        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base/task.html" #指定したテンプレートファイルをレンダリングする

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = "__all__"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("tasks")

    # ログインしているユーザーだけがフォーム有効状態になっている。
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")