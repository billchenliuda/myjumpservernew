# Generated by Django 3.1.14 on 2022-02-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0043_auto_20220217_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='protocol',
            field=models.CharField(choices=[('ssh', 'ssh'), ('rdp', 'rdp'), ('vnc', 'vnc'), ('telnet', 'telnet'), ('mysql', 'mysql'), ('oracle', 'oracle'), ('mariadb', 'mariadb'), ('sqlserver', 'sqlserver'), ('postgresql', 'postgresql'), ('redis', 'redis'), ('mongodb', 'MongoDB'), ('k8s', 'kubernetes')], db_index=True, default='ssh', max_length=16),
        ),
    ]
