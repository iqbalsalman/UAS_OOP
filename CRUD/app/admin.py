from django.contrib import admin
from .models import Post #add this to import the Post model
admin.site.register(Post) #add this to register the Post model

from .models import Mahasiswa #add this to import the Mahasiswa model
admin.site.register(Mahasiswa) #add this to register the Mahasiswa model