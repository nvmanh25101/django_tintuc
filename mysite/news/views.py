from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import SignupForm, CommentForm
from .models import Article


# def index(request):
#     latest_article_list = Article.objects.order_by('-publish_date')[:5]
#     context = {'latest_article_list': latest_article_list}
#     return render(request, 'news/index.html', context)
#
#
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, article=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, 'news/detail.html', {'article': article, 'form': form})


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_article_list'
    paginate_by = 2

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-publish_date')


# class DetailView(generic.DetailView):
#     model = Article
#     template_name = 'news/detail.html'


def error404(request, exception):
    return render(request, 'layouts/error.html')


def error500(request):
    return render(request, 'layouts/error.html')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save to database
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'layouts/signup.html', {'form': form})
