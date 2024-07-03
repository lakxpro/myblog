from django.urls import path
from .views import Homepage, Listpage, SearchResultsView, ArticleDetail, ArticlesByTag

app_name = "blog"

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("listpage/", Listpage.as_view(), name="listpage"),
    path("search/", SearchResultsView.as_view(), name="search"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
    path("articles/<str:tag_name>/", ArticlesByTag.as_view(), name="articles_by_tag"),
]
