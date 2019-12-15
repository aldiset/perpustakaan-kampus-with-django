# Generated by Django 2.2.7 on 2019-11-21 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_buku_peminjaman_penjaga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Mahasiswa',
            fields=[
                ('nim', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('prodi', models.CharField(max_length=30)),
                ('fakultas', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tanggal', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='peminjaman',
            name='Nama_Buku',
        ),
        migrations.RemoveField(
            model_name='peminjaman',
            name='Peminjam',
        ),
        migrations.RenameModel(
            old_name='Buku',
            new_name='Data_Buku',
        ),
        migrations.RenameModel(
            old_name='Penjaga',
            new_name='Data_Penjaga',
        ),
        migrations.DeleteModel(
            name='Mahasiswa',
        ),
        migrations.DeleteModel(
            name='Peminjaman',
        ),
        migrations.AddField(
            model_name='data_peminjaman',
            name='Nama_Buku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Data_Buku'),
        ),
        migrations.AddField(
            model_name='data_peminjaman',
            name='Peminjam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Data_Mahasiswa'),
        ),
        migrations.AddField(
            model_name='data_peminjaman',
            name='Penanggung_Jawab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Data_Penjaga'),
        ),
    ]