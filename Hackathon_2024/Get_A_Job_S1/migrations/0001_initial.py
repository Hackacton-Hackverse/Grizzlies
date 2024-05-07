# Generated by Django 5.0 on 2024-05-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('nom_entreprise', models.CharField(max_length=100)),
                ('lieu', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('deja_pris', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=100)),
                ('remuneration', models.TextField(max_length=150)),
                ('profile', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
    ]
