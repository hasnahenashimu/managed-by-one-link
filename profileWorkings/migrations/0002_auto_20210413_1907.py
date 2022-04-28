# Generated by Django 3.1.7 on 2021-04-13 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileWorkings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformations',
            old_name='button_style',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='userlinks',
            old_name='icon',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='userlinks',
            old_name='private',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='userlinks',
            old_name='link',
            new_name='insta',
        ),
        migrations.RenameField(
            model_name='userlinks',
            old_name='link_name',
            new_name='youtube',
        ),
        migrations.AddField(
            model_name='userlinks',
            name='linkedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userlinks',
            name='teligram',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userlinks',
            name='twitter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userlinks',
            name='viber',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userlinks',
            name='website',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userlinks',
            name='whatsapp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
