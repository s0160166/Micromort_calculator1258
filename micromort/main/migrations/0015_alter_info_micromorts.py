# Generated by Django 4.1.4 on 2022-12-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_info_cigarets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='micromorts',
            field=models.TextField(default=0),
        ),
    ]
