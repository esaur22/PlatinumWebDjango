# Generated by Django 3.0.4 on 2020-04-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interesados', '0003_auto_20200401_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='modificado',
            field=models.TextField(blank=True, null=True),
        ),
    ]