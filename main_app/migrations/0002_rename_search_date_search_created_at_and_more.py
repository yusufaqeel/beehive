# Generated by Django 4.1.7 on 2023-03-22 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='search_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='video',
            name='tags',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='channel',
            name='profilephoto',
            field=models.ImageField(blank=True, null=True, upload_to='main_app/static/uploads/'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='channel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.video'),
        ),
        migrations.AlterField(
            model_name='search',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='main_app.channel'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
