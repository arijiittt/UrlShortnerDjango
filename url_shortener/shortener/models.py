from django.db import models
import string
import random

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=6, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(6))
        if URL.objects.filter(short_code=short_code).exists():
            return self.generate_short_code()  # Regenerate if it already exists
        return short_code
