# Generated by Django 3.2.14 on 2022-12-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0025_auto_20221206_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvalrule',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='approvalrule',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='ticketassignee',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='ticketassignee',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='ticketflow',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='ticketflow',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='ticketstep',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='ticketstep',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='approvalrule',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='ticketassignee',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='ticketflow',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='ticketstep',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
    ]
