# Generated by Django 3.0.4 on 2020-04-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interesados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='comentarios',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interesado',
            name='modificado',
            field=models.TextField(blank=True, null=True),
        ),
    ]