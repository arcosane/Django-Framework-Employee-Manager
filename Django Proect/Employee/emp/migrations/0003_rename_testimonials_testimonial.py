# Generated by Django 4.2.2 on 2023-06-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_testimonials'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]
