# Generated by Django 3.2.16 on 2024-02-11 19:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0012_remove_follow_unique_follow_subscriber_pair'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]
