from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from curriculum.views import Home_view
from post.views import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView
from registration.views import register, profile, activate
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .sitemaps import StaticViewsSitemap, PostsSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewsSitemap,
    'post': PostsSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('post/<int:pk>/details/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('santa/', admin.site.urls),
    path('', Home_view, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)