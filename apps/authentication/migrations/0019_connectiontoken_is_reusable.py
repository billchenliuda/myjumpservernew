# Generated by Django 3.2.17 on 2023-05-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_alter_connectiontoken_input_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectiontoken',
            name='is_reusable',
            field=models.BooleanField(default=False, verbose_name='Reusable'),
        ),
    ]
