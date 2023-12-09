# Generated by Django 2.2.24 on 2023-12-09 12:29

from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.owners_phonenumber:
            try:
                phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
                if phonenumbers.is_valid_number(phone_number):
                    formatted_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
                    flat.owner_pure_phone = formatted_number
                else:
                    flat.owner_pure_phone = None
                flat.save()
            except phonenumbers.NumberParseException:
                flat.owner_pure_phone = None
                flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]