# Generated by Django 2.2.3 on 2019-08-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20190729_0557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='statement',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_1',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_2',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_3',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_4',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_5',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default=None, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=512),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]