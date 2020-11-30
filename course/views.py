from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Course, Category
from django.shortcuts import render
from .forms import CourseForm


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'courses': Category.objects.all()
        }
        return content


class CourseListView(ListView):
    model = Course
    template_name = 'index.html'
    paginate_by = 2


class CourseCreateView(CreateView):
    model = Course
    template_name = 'course.html'
    form_class = CourseForm
    success_url = '/'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'single.html'


def category_list(request):
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }
    return render(request, 'index.html', context)
