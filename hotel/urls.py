from django.urls import include, path
from .views import HotelListView, HotelDetailView, AdministrationView, add_review, PostListView, add_post, test_text

urlpatterns = [
    path('', HotelListView.as_view(), name='hotel-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('admin-portal/', AdministrationView.as_view(), name='admin-portal'),
    path('add-review/', add_review, name='add-review'),
    path('test-text/', test_text, name='test-text'),
    path('add-post/', add_post, name='add-post'),
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    # path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
    # path('weblog/', include('blog.urls')),
]