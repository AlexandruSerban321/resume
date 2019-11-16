from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    def items(self):
        return ['post-create', 'profile', 'register', 'login', 'logout', 'password_reset', 'home']

    def location(self, item):
        return reverse(item)
