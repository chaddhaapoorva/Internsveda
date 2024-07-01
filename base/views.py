from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .models import *
from django.shortcuts import render, get_object_or_404  

# Create your views here.
def base (request):
    return render(request,'base.html')
def index (request):
    return render(request,'main/index.html')
def about (request):
    return render(request,'about.html')
def internships (request):
    category = Categories.objects.all().order_by('id')
    internships = Internships.objects.filter(status = 'PUBLISH').order_by('id')
    context = {
        'category':category,
        'internships' : internships,     
    }
    return render(request,'internships.html',context)

def enrolledinternship(request):
    user_internships = UserInternship.objects.filter(user=request.user).select_related('internships')
    internships = [ui.internships for ui in user_internships]
    
    context = {
        'internships': internships,
    }
    return render(request, 'enrolledinternship.html', context)
def home (request):
    return render(request,'main/home.html')
def DO_LOGIN (request):
    return render(request,'login.html')
def SINGLE_INTERNSHIP(request):
    return render(request,'single_internship.html')
def PROFILE(request):
    return render(request,'registration/profile.html')
def PROFILE_UPDATE(request):
    if request.method == "POST":
      username = request.POST.get('username')
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      user_id = request.user.id

      user = User.objects.get(id=user_id)
      user.first_name = first_name
      user.last_name = last_name
      user.username = username
      user.email = email

      if password != None and password != "":
       user.set_password(password)
      
      user.save()
      messages.success(request,'Profile Is Successfully Updated.')
      return redirect('profile') 
def logout_view(request):
    logout(request)
    return redirect('login')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
    messages.success(request,'Your Message Is Successfully Delivered.')
    return render(request, 'contacts.html')
def contact_index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        category = request.POST.get('category')
        subject = request.POST.get('subject')

        contacts = Contact_us(
            name=name,
            email=email,
            category=category,
            subject=subject,
        )
        contacts.save()
    messages.success(request,'Your Message Is Successfully Delivered.')
    return render(request, 'main/index.html')
def SINGLE_INTERNSHIP(request):
    category = Categories.get_all_category(Categories).order_by('id')
    internships = Internships.objects.all
    context = {
        'internships':internships,
        'category':category
    }
    return render(request, 'single_internship.html',context)
def INTERNSHIPS_DETAILS(request, slug):
    category = Categories.objects.all().order_by('id')
    internships = get_object_or_404(Internships, slug=slug)
    learning_outcomes = LEARNING_OUTCOMES.objects.filter(course=internships)

    context = {
        'internships': internships,
        'category': category,
        'learning_outcomes': learning_outcomes
    }
    return render(request, 'single_internship.html', context)
def ENROLLEDCOURSE_DETAILS(request, slug):
    category = Categories.get_all_category(Categories).order_by('id')
    internships = get_object_or_404(Internships, slug=slug)
    learning_outcomes = LEARNING_OUTCOMES.objects.filter(course=internships)
    lesson = Lesson.objects.filter(Internships=internships)

    lesson_videos = {}
    for lesson in lesson:
        lesson_videos[lesson] = lesson.video_set.all()
    
    context = {
        'internships': internships,
        'category': category,
        'learning_outcomes': learning_outcomes,
        'lesson': lesson,
        'lesson_videos': lesson_videos,
    }
    return render(request, 'enrolledcourse.html', context)
