# Generated by Django 3.1 on 2020-08-21 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghost_post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boast_roast',
            old_name='post_content',
            new_name='content',
        ),
    ]