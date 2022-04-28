# Generated by Django 3.1.7 on 2021-04-13 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profileWorkings', '0002_auto_20210413_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformations',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='github',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='insta',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='teligram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='twitter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='viber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userlinks',
            name='youtube',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
