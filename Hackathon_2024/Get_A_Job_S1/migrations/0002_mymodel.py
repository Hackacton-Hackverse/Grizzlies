# Generated by Django 5.0 on 2024-05-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Get_A_Job_S1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('classe', models.CharField(max_length=100)),
                ('matricule', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
