from django.urls import path
from .views import HomeView, ArticleDetailsView, AddPostView, UpdatePostView
from .views import AddCommentView
# from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name="article-detail"),
    path('article/comment/<int:pk>', AddCommentView.as_view(), name="add_comment"),
    path('addpost/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),  name="update_post"),
]




