# Generated by Django 4.2.5 on 2023-09-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.CharField(default='e58816f3-bcfa-4801-8be6-4abd84bf4add', max_length=100, unique=True),
        ),
    ]
