# Generated by Django 5.0.1 on 2024-06-02 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_course_discount_remove_course_featured_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_outcomes',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_outcomes_set', to='base.course'),
        ),
    ]
