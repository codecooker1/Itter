# Generated by Django 5.1.1 on 2025-01-03 07:00

import django.db.models.deletion
import itterapi.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itterapi', '0002_remove_like_user_id_remove_post_user_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='itterapi.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='media_url',
            field=models.URLField(validators=[itterapi.models.validate_media_url]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.URLField(default='https://jzydvbxwyynlezjnqbbd.supabase.co/storage/v1/object/public/profilepics/1%20(1).png'),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'followee')},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
    ]
