# Generated by Django 3.2 on 2022-08-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_campo_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictivo',
            name='name',
            field=models.TextField(max_length=255),
        ),
    ]
