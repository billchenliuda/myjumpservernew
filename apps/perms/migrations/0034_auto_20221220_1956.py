# Generated by Django 3.2.14 on 2022-12-20 11:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('perms', '0033_alter_assetpermission_actions'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetpermission',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='assetpermission',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='assetpermission',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='assetpermission',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='assetpermission',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='userassetgrantedtreenoderelation',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='userassetgrantedtreenoderelation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userassetgrantedtreenoderelation',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
    ]