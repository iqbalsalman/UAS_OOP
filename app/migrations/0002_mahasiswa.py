# Generated by Django 3.0 on 2019-12-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npm', models.CharField(help_text='NPM mahasiwa.', max_length=20)),
                ('nama', models.CharField(help_text='Nama Mahasiswa.', max_length=100)),
                ('kelas', models.CharField(help_text='Kelas Mahasiswa.', max_length=120)),
                ('jurusan', models.CharField(help_text='Jurusan Mahasiswa.', max_length=20)),
                ('fakultas', models.CharField(help_text='Fakultas Mahasiwa.', max_length=100)),
            ],
        ),
    ]
