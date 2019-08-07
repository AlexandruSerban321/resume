from django.shortcuts import render
from curriculum.models import Experience, Education, Skill
from post.models import Post

def Home_view(request):
    posts = Post.objects.order_by("-date_posted")
    all_experiences = Experience.objects.order_by("-id")
    all_educations = Education.objects.order_by("-id")
    all_skills = Skill.objects.all()
    context = {
        'posts': posts,
        'all_experiences': all_experiences,
        'all_educations': all_educations,
        'all_skills': all_skills,
    }
    return render(request, 'resume.html', context)