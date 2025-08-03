from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from .models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'preview', 'content', 'is_published']
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        # Фильтруем только опубликованные посты
        return super().get_queryset().filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # Получаем объект
        obj = super().get_object(queryset)
        # Увеличиваем счетчик просмотров
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'preview', 'content', 'is_published']
    template_name = 'blog/post_update.html'

    def get_success_url(self):
        # Перенаправление на страницу просмотра статьи
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')
