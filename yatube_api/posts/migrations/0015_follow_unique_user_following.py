# Generated by Django 3.2.16 on 2024-02-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0014_alter_post_options'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(
                fields=('user', 'following'), name='unique_user_following'
            ),
        ),
    ]