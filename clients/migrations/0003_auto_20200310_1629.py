# Generated by Django 3.0.4 on 2020-03-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20200310_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='attended',
            field=models.NullBooleanField(default=False),
        ),
    ]
