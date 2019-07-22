from django.shortcuts import render
from curriculum.models import Experience, Education, Skill

# Create your views here.
def Home_view(request):
    all_experiences = Experience.objects.order_by("-id")
    all_educations = Education.objects.order_by("-id")
    all_skills = Skill.objects.all()
    context = {
        'all_experiences': all_experiences,
        'all_educations': all_educations,
        'all_skills': all_skills,
    }
    return render(request, 'resume.html', context)