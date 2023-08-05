# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone

class User(AbstractUser):
   pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    phone = models.BigIntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.avatar)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((100, 100))
        im = im.convert('RGB')

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.avatar = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.avatar.name.split('.')[0], 'avatar/jpeg',
                                        sys.getsizeof(output), None)

        super(Profile, self).save()


class Punch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    IN = 'in'
    OUT = 'out'

    PUNCH = [
        (IN,'IN'),
        (OUT,'OUT')
    ]
    status = models.CharField(max_length=3, choices= PUNCH, null=True, default='in')
    punch = models.DateTimeField(default=timezone.now)





    
# class Punch(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
#     IN = 'in'
#     OUT = 'out'

#     PUNCH = [
#         (IN,'IN'),
#         (OUT,'OUT')
#     ]
#     status = models.CharField(max_length=3, choices= PUNCH, null=True, default='in')
#     punch = models.DateTimeField(default=timezone.now)

class Role(models.Model):
    GATE = 'gate'
    CRANE = 'crane'

    ROLE_PUNCH = [
        (GATE,'Gate'),
        (CRANE,'Crane')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    role = models.CharField(max_length=10, choices= ROLE_PUNCH, blank=True, null = True)
    role_punch = models.DateTimeField(default=timezone.now, blank=True, null = True)



class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    task = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null = True)
    DONE = 'done'
    PENDING = 'pending'

    STATUS = [
        (DONE,'DONE'),
        (PENDING,'PENDING')
    ]
    status = models.CharField(max_length=10, choices= STATUS, blank=True, null = True)
    completed_on = models.DateTimeField(auto_now_add=False, blank=True, null = True)


