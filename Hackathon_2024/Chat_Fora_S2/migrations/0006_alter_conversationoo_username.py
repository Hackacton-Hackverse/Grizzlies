# Generated by Django 5.0 on 2024-05-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat_Fora_S2', '0005_remove_conversationoo_participants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationoo',
            name='Username',
            field=models.CharField(max_length=200),
        ),
    ]
