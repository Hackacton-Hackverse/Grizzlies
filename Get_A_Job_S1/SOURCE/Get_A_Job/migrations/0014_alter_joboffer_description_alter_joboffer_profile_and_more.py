# Generated by Django 5.0 on 2024-04-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Get_A_Job', '0013_alter_joboffer_description_alter_joboffer_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='profile',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='remuneration',
            field=models.CharField(max_length=150),
        ),
    ]
