from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post, Comment

class HomeView(ListView):
    """Base home view."""

    template_name = "core/home.html"
    queryset = Post.objects.values("title", "body")

class AboutView(TemplateView):
    """Base about view."""

    template_name = "core/about.html"