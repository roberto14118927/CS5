# Generated by Django 2.2.1 on 2019-05-23 14:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
