# Generated by Django 2.2.5 on 2020-05-09 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicant_app', '0002_applicantuserprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantuserprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'usertype': 'Applicant'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicantuserprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]