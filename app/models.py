from django.db import models
class Post(models.Model):
 title = models.CharField(max_length=120, help_text='title of message.')
 message = models.TextField(help_text="what's on your mind ...")
 
 def __str__(self):
  return self.title

class Mahasiswa(models.Model):
 npm = models.CharField(max_length=20, help_text='NPM mahasiwa.')
 nama = models.CharField(max_length=100, help_text='Nama Mahasiswa.')
 kelas = models.CharField(max_length=120, help_text='Kelas Mahasiswa.')
 jurusan = models.CharField(max_length=20, help_text='Jurusan Mahasiswa.')
 fakultas = models.CharField(max_length=100, help_text='Fakultas Mahasiwa.')
 
 def __str__(self):
  return self.nama