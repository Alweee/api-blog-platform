# Generated by Django 2.2.16 on 2022-06-06 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_group'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_following',
        ),
    ]