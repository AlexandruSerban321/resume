from django.shortcuts import render
from curriculum.models import Experience, Education, Skill
from post.models import Post
from django.core.paginator import Paginator

def Home_view(request):
    posts = Post.objects.order_by("-date_posted")
    all_experiences = Experience.objects.order_by("-id")
    all_educations = Education.objects.order_by("-id")
    all_skills = Skill.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'posts': posts,
        'all_experiences': all_experiences,
        'all_educations': all_educations,
        'all_skills': all_skills,
        'post_list': post_list,
        'is_paginated': True,
    }
    return render(request, 'resume.html', context)


def home(request, slug):
    return render(request, 'resume.html', {'slug':slug})