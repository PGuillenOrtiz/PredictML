# Generated by Django 3.2 on 2022-09-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_alter_principal_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='full_description',
            field=models.TextField(max_length=1500, null=True),
        ),
    ]
