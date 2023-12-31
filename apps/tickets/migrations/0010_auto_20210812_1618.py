# Generated by Django 3.1.6 on 2021-08-12 08:18

import common.db.encoder
from django.conf import settings
from django.db import migrations, models, transaction
import django.db.models.deletion
import uuid

from tickets.const import TicketType, TicketApprovalStrategy

ticket_assignee_m2m = list()


def get_ticket_assignee_m2m_info(apps, schema_editor):
    ticket_model = apps.get_model("tickets", "Ticket")
    for i in ticket_model.objects.only('id', 'assignees', 'action', 'created_by'):
        ticket_assignee_m2m.append((i.id, list(i.assignees.values_list('id', flat=True)), i.action, i.created_by))


def update_ticket_process_meta_state_status(apps, schema_editor):
    ticket_model = apps.get_model("tickets", "Ticket")
    updates = list()
    with transaction.atomic():
        for instance in ticket_model.objects.all():
            if instance.action == 'open':
                state = 'notified'
            elif instance.action == 'approve':
                state = 'approved'
            elif instance.action == 'reject':
                state = 'rejected'
            else:
                state = 'closed'
            instance.process_map = [{
                'state': state,
                'approval_level': 1,
                'approval_date': str(instance.date_updated),
                'processor': instance.processor.id if instance.processor else '',
                'processor_display': instance.processor_display if instance.processor_display else '',
                'assignees': list(instance.assignees.values_list('id', flat=True)) if instance.assignees else [],
                'assignees_display': instance.assignees_display if instance.assignees_display else []
            }, ]
            instance.state = state
            instance.meta['apply_assets'] = instance.meta.pop('approve_assets', [])
            instance.meta['apply_assets_display'] = instance.meta.pop('approve_assets_display', [])
            instance.meta['apply_actions'] = instance.meta.pop('approve_actions', 0)
            instance.meta['apply_actions_display'] = instance.meta.pop('approve_actions_display', [])
            instance.meta['apply_applications'] = instance.meta.pop('approve_applications', [])
            instance.meta['apply_applications_display'] = instance.meta.pop('approve_applications_display', [])
            instance.meta['apply_system_users'] = instance.meta.pop('approve_system_users', [])
            instance.meta['apply_system_users_display'] = instance.meta.pop('approve_system_users_display', [])
            updates.append(instance)
        ticket_model.objects.bulk_update(updates, ['process_map', 'state', 'meta', 'status'])


def create_step_and_assignee(apps, schema_editor):
    ticket_step_model = apps.get_model("tickets", "TicketStep")
    ticket_assignee_model = apps.get_model("tickets", "TicketAssignee")
    creates = list()
    with transaction.atomic():
        for ticket_id, assignees, action, created_by in ticket_assignee_m2m:
            if action == 'open':
                state = 'notified'
            elif action == 'approve':
                state = 'approved'
            else:
                state = 'rejected'
            step_instance = ticket_step_model.objects.create(ticket_id=ticket_id, state=state, created_by=created_by)
            for assignee_id in assignees:
                creates.append(
                    ticket_assignee_model(
                        step=step_instance, assignee_id=assignee_id, state=state, created_by=created_by
                    )
                )
        ticket_assignee_model.objects.bulk_create(creates)


def create_ticket_flow_and_approval_rule(apps, schema_editor):
    user_model = apps.get_model("users", "User")
    org_id = '00000000-0000-0000-0000-000000000000'
    ticket_flow_model = apps.get_model("tickets", "TicketFlow")
    approval_rule_model = apps.get_model("tickets", "ApprovalRule")
    super_user = user_model.objects.filter(role='Admin')
    assignees_display = ['{0.name}({0.username})'.format(i) for i in super_user]
    with transaction.atomic():
        for ticket_type in [TicketType.apply_asset, 'apply_application']:
            ticket_flow_instance = ticket_flow_model.objects.create(created_by='System', type=ticket_type, org_id=org_id)
            approval_rule_instance = approval_rule_model.objects.create(strategy=TicketApprovalStrategy.super_admin, assignees_display=assignees_display)
            approval_rule_instance.assignees.set(list(super_user))
            ticket_flow_instance.rules.set([approval_rule_instance, ])


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0009_auto_20210426_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('level', models.SmallIntegerField(choices=[(1, 'One level'), (2, 'Two level')], default=1,
                                                   verbose_name='Approve level')),
                ('strategy', models.CharField(
                    choices=[('super_admin', 'Super admin'), ('org_admin', 'Org admin'), ('super_org_admin', 'Super admin and org admin'),
                             ('custom_user', 'Custom user')],
                    default='super_admin', max_length=64, verbose_name='Approve strategy')),
                ('assignees_display', models.JSONField(default=list, encoder=common.db.encoder.ModelJSONFieldEncoder,
                                                       verbose_name='Assignees display')),
                ('assignees',
                 models.ManyToManyField(related_name='assigned_ticket_flow_approval_rule', to=settings.AUTH_USER_MODEL,
                                        verbose_name='Assignees')),
            ],
            options={
                'verbose_name': 'Ticket flow approval rule',
            },
        ),
        migrations.RunPython(get_ticket_assignee_m2m_info),
        migrations.AddField(
            model_name='ticket',
            name='process_map',
            field=models.JSONField(default=list, encoder=common.db.encoder.ModelJSONFieldEncoder,
                                   verbose_name='Process'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='state',
            field=models.CharField(
                choices=[('open', 'Open'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('closed', 'Closed')],
                default='open', max_length=16, verbose_name='State'),
        ),
        migrations.RunPython(update_ticket_process_meta_state_status),
        migrations.RemoveField(
            model_name='ticket',
            name='action',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='assignees',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='assignees_display',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='processor_display',
        ),
        migrations.AddField(
            model_name='ticket',
            name='approval_step',
            field=models.SmallIntegerField(choices=[(1, 'One level'), (2, 'Two level')], default=1,
                                           verbose_name='Approval step'),
        ),
        migrations.CreateModel(
            name='TicketStep',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('level', models.SmallIntegerField(choices=[(1, 'One level'), (2, 'Two level')], default=1,
                                                   verbose_name='Approve level')),
                ('state', models.CharField(
                    choices=[('notified', 'Notified'), ('approved', 'Approved'), ('rejected', 'Rejected')],
                    default='notified', max_length=64)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_steps',
                                             to='tickets.ticket', verbose_name='Ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TicketFlow',
            fields=[
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('type', models.CharField(choices=[('general', 'General'), ('login_confirm', 'Login confirm'),
                                                   ('apply_asset', 'Apply for asset'),
                                                   ('apply_application', 'Apply for application'),
                                                   ('login_asset_confirm', 'Login asset confirm'),
                                                   ('command_confirm', 'Command confirm')], default='general',
                                          max_length=64, verbose_name='Type')),
                ('approval_level', models.SmallIntegerField(choices=[(1, 'One level'), (2, 'Two level')], default=1,
                                                            verbose_name='Approve level')),
                ('rules', models.ManyToManyField(related_name='ticket_flows', to='tickets.ApprovalRule')),
            ],
            options={
                'verbose_name': 'Ticket flow',
            },
        ),
        migrations.CreateModel(
            name='TicketAssignee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('state', models.CharField(
                    choices=[('notified', 'Notified'), ('approved', 'Approved'), ('rejected', 'Rejected')],
                    default='notified', max_length=64)),
                ('assignee',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_assignees',
                                   to=settings.AUTH_USER_MODEL, verbose_name='Assignee')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_assignees',
                                           to='tickets.ticketstep')),
            ],
            options={
                'verbose_name': 'Ticket assignee',
            },
        ),
        migrations.RunPython(create_step_and_assignee),
        migrations.RunPython(create_ticket_flow_and_approval_rule),
        migrations.AddField(
            model_name='ticket',
            name='flow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets',
                                    to='tickets.ticketflow', verbose_name='TicketFlow'),
        ),
    ]
