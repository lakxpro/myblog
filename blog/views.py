from django.views.generic import ListView, DetailView
from .models import Article, Tag


class Homepage(ListView):
    model = Article
    template_name = "homepage/_homepage.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all()[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class Listpage(ListView):
    model = Article
    template_name = "listpage/_listpage.html"
    context_object_name = "articles"
    paginate_by = 3

    def get_queryset(self):
        return Article.objects.all().order_by("id")


class SearchResultsView(ListView):
    model = Article
    template_name = "search_results/_search_results.html"
    context_object_name = "articles"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("query")
        return Article.objects.filter(title__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query")
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = "article_detail/_article_detail.html"
    context_object_name = "article"


class ArticlesByTag(ListView):
    model = Article
    template_name = "search_results/_search_by_tag.html"
    context_object_name = "articles"
    paginate_by = 3

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"]
        return Article.objects.filter(tags__name=tag_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = self.kwargs["tag_name"]
        return context
