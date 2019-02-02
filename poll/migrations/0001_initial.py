# Generated by Django 2.1.3 on 2018-12-15 23:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250, verbose_name='value')),
                ('pos', models.SmallIntegerField(default='0', verbose_name='position')),
            ],
            options={
                'verbose_name_plural': 'answers',
                'verbose_name': 'answer',
                'ordering': ['pos'],
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='poll')),
                ('description', models.CharField(default='', max_length=250, verbose_name='description')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('show_results', models.BooleanField(default=True, verbose_name='show results')),
            ],
            options={
                'verbose_name_plural': 'polls',
                'verbose_name': 'poll',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='question')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll', verbose_name='poll')),
            ],
            options={
                'verbose_name_plural': 'questions',
                'verbose_name': 'question',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name="user's IP")),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Item', verbose_name='voted item')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Question', verbose_name='question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'votes',
                'verbose_name': 'vote',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Question', verbose_name='question'),
        ),
    ]
