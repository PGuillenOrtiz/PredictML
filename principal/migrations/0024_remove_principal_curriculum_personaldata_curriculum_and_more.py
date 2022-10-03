# Generated by Django 4.1.1 on 2022-10-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0023_alter_principal_notebook_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principal',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='curriculum',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='principal',
            name='images',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='principal',
            name='notebook_model',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
