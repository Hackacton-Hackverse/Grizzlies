# Generated by Django 5.0 on 2024-04-14 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Get_A_Job', '0008_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='email',
            field=models.EmailField(default='azangueleonel9@gmail.com', max_length=100),
        ),
    ]
