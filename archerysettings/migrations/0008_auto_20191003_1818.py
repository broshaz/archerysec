# Generated by Django 2.2.6 on 2019-10-03 18:18

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('archerysettings', '0007_sonarqube_setting_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openvas_setting_db',
            name='password',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True)),
        ),
        migrations.AlterField(
            model_name='openvas_setting_db',
            name='user',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True)),
        ),
    ]
