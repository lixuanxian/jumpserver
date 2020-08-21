# Generated by Django 2.2.13 on 2020-08-21 08:20

from django.db import migrations
from django.db.models import Q


def fill_node_value(apps, schema_editor):
    Node = apps.get_model('assets', 'Node')
    Asset = apps.get_model('assets', 'Asset')
    for node in Node.objects.all():
        assets_amount = Asset.objects.filter(
            Q(nodes__key__startswith=f'{node.key}:') | Q(nodes=node)
        ).distinct().count()
        parent_key = ':'.join(node.key.split(':')[0:-1])
        node.assets_amount = assets_amount
        node.parent_key = parent_key
        node.save()
        print(f'Fill {node} finished')


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0057_auto_20200821_1620'),
    ]

    operations = [
        migrations.RunPython(fill_node_value)
    ]