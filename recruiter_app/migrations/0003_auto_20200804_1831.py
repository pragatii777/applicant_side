# Generated by Django 3.0.6 on 2020-08-04 13:01

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter_app', '0002_short_list_candidate_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_requirements',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('JAVA', 'JAVA'), ('CPP', 'CPP'), ('C', 'C'), ('Python', 'Python'), ('jQuery', 'jQuery'), ('Javascript', 'Javascript')], max_length=540),
        ),
    ]
