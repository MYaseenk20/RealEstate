# Generated by Django 3.0.3 on 2020-07-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='relator',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='relator_email',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
