# Generated by Django 2.2.7 on 2019-11-20 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nama',
            new_name='nama_barang',
        ),
    ]