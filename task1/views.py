from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def function(request):
    posts = Post.objects.all().order_by('created_at')  # задаем в переменную все объекты из бд

    posts_on_page = request.GET.get('posts_on_page', 3)  # делаем запрос на количество элементов на странице,
    # по умолчанию 3
    try:
        posts_on_page = int(posts_on_page)
        if posts_on_page <= 0:
            posts_on_page = 3
    except ValueError:
        posts_on_page = 3


    # создаем пагинатор
    paginator = Paginator(posts, posts_on_page)  # указываем что будем размещать и количество

    page_number = request.GET.get('page')   # получаем номер страницы, на которую переходит пользователь

    page_obg = paginator.get_page(page_number)   # получаем посты для текущей страницы

    return render(request, 'paginator.html', {'page_obj': page_obg, 'posts_on_page': posts_on_page})


def menu(request):
    return render(request, 'menu.html')

# Create your views here.
