# Generated by Django 4.2.1 on 2023-07-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_users_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('faculty', 'faculty Member'), ('faculty', 'Staff Member'), ('alumni', 'Alumni')], max_length=10),
        ),
    ]
