# Generated by Django 4.2.5 on 2023-09-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token',
            field=models.CharField(default='33ff8c04-0d88-484c-9c7f-cba6f9a90899', max_length=100, unique=True),
        ),
    ]
