from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Author, Post



def hello(request):
    return HttpResponse('Hello World from function')

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello World from class')

def year_post(request, year):
    text = ''
    ... # create posts for year
    return HttpResponse(f'Posts from {year}<br>{text}')

class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        ... # create posts for year and month
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')
    
def post_detail(request, year, month, slug):
    ... # create posts for year and month by id

    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'What is create lists faster, list() or []',
        'content': 'During create new app, I interested, '
                    'which way create lists in Python is faster...'
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
def my_view(request):
    context = {'name': 'John'}
    return render(request, 'myapp3/my_template.html', context)

def if_view(request):
    message = ['text1', 'text2', 'text3','text2', 'text3']
    context = {'message': message[0], 'number': len(message)}
    return render(request, 'myapp3/templ_if.html', context)

# class TemplIf(TemplateView):
#     template_name = 'myapp3/templ_if.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['message'] = 'Hello world'
#         context['number'] = 2

#         return context

def view_for(request):
    my_list = ['apple', 'banna', 'orange']
    my_dict = {
        'каждый': 'red',
        'охотник': 'orange',
        'желает': 'yellow',
        'знать': 'green',
        'где': 'blue',
        'сидит': 'blue',
        'фазан': 'purple',
    }
    context = {'messages': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)

def index(request):
    return render(request, 'myapp3/index.html')

def about(request):
    return render(request, 'myapp3/about.html')

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
# Create your views here.
