# Generated by Django 2.2.24 on 2023-12-09 15:47

from django.db import migrations


def transfer_ownership_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            full_name=flat.owner,
            defaults={
                'phonenumber': flat.owners_phonenumber,
                'pure_phonenumber': flat.owner_pure_phone
            }
        )
        

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(transfer_ownership_data)
    ]