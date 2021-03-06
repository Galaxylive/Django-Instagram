# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 02:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import member.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20171022_1354'),
        ('member', '0002_auto_20171022_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', member.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, to='post.Post'),
        ),
        migrations.AddField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_relations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_relations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='relations',
            field=models.ManyToManyField(through='member.Relation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
