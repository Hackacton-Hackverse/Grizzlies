# Generated by Django 5.0 on 2024-05-07 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat_Fora_S2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='titre',
            field=models.CharField(default='leo', max_length=200),
        ),
    ]
