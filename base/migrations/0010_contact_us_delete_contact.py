# Generated by Django 5.0.1 on 2024-06-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_course_internships_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
