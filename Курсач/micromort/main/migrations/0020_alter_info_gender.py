# Generated by Django 4.1.4 on 2022-12-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_info_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default='Пол не выбран', max_length=7),
        ),
    ]
