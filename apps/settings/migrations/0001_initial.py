# Generated by Django 2.1.7 on 2019-02-26 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0006_auto_20190304_1515'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True,
                                          verbose_name='Name')),
                ('value', models.TextField(verbose_name='Value')),
                ('category',
                 models.CharField(default='default', max_length=128, verbose_name='Category')),
                ('encrypted', models.BooleanField(default=False, verbose_name='Encrypted')),
                ('enabled',
                 models.BooleanField(default=True, verbose_name='Enabled')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Setting',
                'db_table': 'settings_setting',
            },
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
