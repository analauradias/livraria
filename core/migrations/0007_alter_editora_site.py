# Generated by Django 5.1.7 on 2025-04-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_editora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editora',
            name='site',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
