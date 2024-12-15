from django.contrib import admin
from django.urls import path
from tokushimasauna.views import SpaListView, SpaDetailView, mypage_view, login_view, logout_view, register_view, favorite_view, delete_favorite_view, review_view, edit_review_view, delete_review_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SpaListView.as_view(), name='spa_list'),
    path('spas/<int:pk>/', SpaDetailView.as_view(), name='spa_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('mypage/', mypage_view, name='mypage'),
    path('favorite/<int:pk>/', favorite_view, name='favorite'),
    path('favorite/delete/<int:pk>/', delete_favorite_view, name='delete_favorite'),
    path('review/<int:pk>', review_view, name="review"),
    path('review/edit/<int:pk>/', edit_review_view, name='edit_review'),
    path('review/delete/<int:pk>/', delete_review_view, name='delete_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
