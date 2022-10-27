from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreateNews, PostCreateArticle, PostUpdateNews, \
   PostUpdateArticle, PostDeleteNews, PostDeleteArticle, CategoryListView, subscribe

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreateNews.as_view(), name='post_create'),
   path('articles/create', PostCreateArticle.as_view(), name='article_create'),
   path('<int:pk>/update/', PostUpdateNews.as_view(), name='post_update'),
   path('articles/<int:pk>/update', PostUpdateArticle.as_view(), name='article_update'),
   path('<int:pk>/delete', PostDeleteNews.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete', PostDeleteArticle.as_view(), name='article_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
   ]
