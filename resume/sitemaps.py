from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from post.models import Post


class StaticViewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['post-create', 'profile', 'register', 'login', 'logout', 'password_reset', 'home']

    def location(self, item):
        return reverse(item)


class PostsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()
