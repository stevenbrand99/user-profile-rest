# Generated by Django 3.2.6 on 2021-09-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_userprofilefeed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileFeed',
            new_name='ProfileFeedItem',
        ),
    ]
