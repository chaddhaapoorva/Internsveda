from typing import Any
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.urls import reverse

class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=255)
    category = models.CharField(max_length=50, default='Categories')
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_all_category(self):
        return Categories.objects.all().order_by('id')

class Author(models.Model):
    author_profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name
    


class Internships(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="Media/featured_img",null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    modules = models.IntegerField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(null=True,default=0)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)


    def __str__(self):
        return self.title
       
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("internships_details", kwargs={'slug': self.slug})

    def get_url_ec(self):
        from django.urls import reverse
        return reverse("enrolledcourse_details", kwargs={'slug': self.slug})
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Internships.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Internships)

class LEARNING_OUTCOMES(models.Model):
    course = models.ForeignKey(Internships, on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points
    
class UserInternship(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    internships = models.ForeignKey(Internships,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name+" - "+self.internships.title
    

class Lesson(models.Model):
    Internships = models.ForeignKey(Internships,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " - " + self.Internships.title
class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    internships = models.ForeignKey(Internships, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')  # Define a FileField for uploading video files

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"pk": self.pk})