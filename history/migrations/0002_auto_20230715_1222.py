# Generated by Django 3.2 on 2023-07-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='History6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='Nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
