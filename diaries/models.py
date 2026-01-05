# diaries/models.py
import uuid
from django.db import models

class Entry(models.Model):
    # ID menggunakan UUID (acak) bukan angka urut 1,2,3
    # Ini penting agar link share aman.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    title = models.CharField(max_length=200, blank=True, default="Tanpa Judul")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Fitur Share: Jika True, orang lain bisa akses via link
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at'] # Menampilkan dari yang terbaru

    def __str__(self):
        return f"{self.created_at.date()} - {self.title}"