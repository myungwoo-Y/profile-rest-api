# Generated by Django 2.2 on 2019-11-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_remove_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]