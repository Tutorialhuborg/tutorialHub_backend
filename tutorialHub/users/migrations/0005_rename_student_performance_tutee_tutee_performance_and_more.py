# Generated by Django 5.0.3 on 2024-03-20 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_student_performance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutee',
            old_name='student_performance',
            new_name='tutee_performance',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='student_performance',
        ),
    ]
