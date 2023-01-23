from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import News


class NewsHome(ListView):
    """ Класс представления Новости и объявления """
    model = News
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = '-time_create'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Вывод динамических данных модели
        """
        contex = super(NewsHome, self).get_context_data(**kwargs)
        return contex


def show_post(request, post_id):
    """ Вывод текста новости """
    post = get_object_or_404(News, pk=post_id)
    contex = {
        'post': post,
        'title': post.title,
    }

    return render(request, f'news/post.html', context=contex)
