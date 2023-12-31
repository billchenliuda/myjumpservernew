# Generated by Django 2.1.7 on 2019-07-02 09:54

import common.utils.django
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# users.migrations.0010_auto_20180606_1505

def remove_deleted_group(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    group_model = apps.get_model("users", "UserGroup")
    group_model.objects.using(db_alias).filter(is_discard=True).delete()


class Migration(migrations.Migration):

    replaces = [('users', '0002_auto_20171225_1157'), ('users', '0003_auto_20180101_0046'), ('users', '0004_auto_20180125_1218'), ('users', '0005_auto_20180306_1804'), ('users', '0006_auto_20180411_1135'), ('users', '0007_auto_20180419_1036'), ('users', '0008_auto_20180425_1516'), ('users', '0009_auto_20180517_1537'), ('users', '0010_auto_20180606_1505'), ('users', '0011_user_source'), ('users', '0012_auto_20180710_1641'), ('users', '0013_auto_20180807_1116'), ('users', '0014_auto_20180816_1652'), ('users', '0015_auto_20181105_1112'), ('users', '0016_auto_20181109_1505'), ('users', '0017_auto_20181123_1113'), ('users', '0018_auto_20190107_1912'), ('users', '0019_auto_20190304_1459')]

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=128, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='wechat',
            field=models.CharField(blank=True, max_length=128, verbose_name='Wechat'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_first_login',
            field=models.BooleanField(default=True, verbose_name='Is first login'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'User'},
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'ordering': ['name'], 'verbose_name': 'User group'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='secret_key_otp',
            new_name='otp_secret_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='enable_otp',
        ),
        migrations.AddField(
            model_name='user',
            name='otp_level',
            field=models.SmallIntegerField(choices=[(0, 'Disable'), (1, 'Enable'), (2, 'Force enable')], default=0, verbose_name='MFA'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_secret_key',
        ),
        migrations.AddField(
            model_name='user',
            name='_otp_secret_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Name'),
        ),
        migrations.RunPython(
            code=remove_deleted_group,
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='discard_time',
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='is_discard',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_expired',
            field=models.DateTimeField(blank=True, db_index=True, default=common.utils.django.date_expired_default, null=True, verbose_name='Date expired'),
        ),
        migrations.AddField(
            model_name='user',
            name='source',
            field=models.CharField(choices=[('local', 'Local'), ('ldap', 'LDAP/AD'), ('openid', 'OpenID'), ('radius', 'Radius')], default='local', max_length=30, verbose_name='Source'),
        ),
        migrations.AddField(
            model_name='loginlog',
            name='mfa',
            field=models.SmallIntegerField(choices=[(0, 'Disabled'), (1, 'Enabled'), (2, '-')], default=2, verbose_name='MFA'),
        ),
        migrations.AddField(
            model_name='loginlog',
            name='reason',
            field=models.SmallIntegerField(choices=[(0, '-'), (1, 'Username/password check failed'), (2, 'MFA authentication failed'), (3, 'Username does not exist'), (4, 'Password expired')], default=0, verbose_name='Reason'),
        ),
        migrations.AddField(
            model_name='loginlog',
            name='status',
            field=models.BooleanField(choices=[(True, 'Success'), (False, 'Failed')], default=True, max_length=2, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='org_id',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='usergroup',
            unique_together={('org_id', 'name')},
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='loginlog',
            name='username',
            field=models.CharField(max_length=128, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='user',
            name='date_password_last_updated',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date password last updated'),
        ),
        migrations.AlterField(
            model_name='accesskey',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_keys', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable(
                    name='accesskey',
                    table='authentication_accesskey',
                ),
                migrations.AlterModelTable(
                    name='privatetoken',
                    table='authentication_privatetoken',
                ),
                migrations.AlterModelTable(
                    name='loginlog',
                    table='audits_userloginlog',
                ),
            ],
            state_operations=[
                migrations.DeleteModel(
                    name='accesskey',
                ),
                migrations.DeleteModel(
                    name='privatetoken',
                ),
                migrations.DeleteModel(
                    name='loginlog',
                ),
            ],
        ),
    ]
