# Generated by Django 3.0.3 on 2020-02-28 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='cell_no',
            new_name='cell_number',
        ),
    ]