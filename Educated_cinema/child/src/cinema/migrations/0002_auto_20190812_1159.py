# Generated by Django 2.2.2 on 2019-08-12 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category',
            new_name='name',
        ),
    ]
