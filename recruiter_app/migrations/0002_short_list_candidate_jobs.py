# Generated by Django 3.0.6 on 2020-07-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='short_list_candidate',
            name='jobs',
            field=models.ManyToManyField(to='recruiter_app.Job'),
        ),
    ]