# Generated by Django 2.2.3 on 2019-08-01 08:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('teachers', models.ManyToManyField(related_name='teachers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
