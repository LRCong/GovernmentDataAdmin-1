# Generated by Django 2.2.3 on 2020-05-29 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200529_2036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DisposeRecord',
        ),
        migrations.DeleteModel(
            name='PostRecord',
        ),
    ]