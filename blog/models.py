from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from utils.models import BaseModel
from django.contrib.auth import get_user_model
from options.models import Option


class Region(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField('self', max_length=128, unique=True)

    def __str__(self):
        return self.title


class SubCategories(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Posts(BaseModel):
    title = models.CharField(max_length=128)
    email = models.EmailField()
    phone = PhoneNumberField(unique=True)
    content = models.TextField()
    watched = models.IntegerField(default=0, editable=False)
    is_shutdown = models.BooleanField(default=False)

    category = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='category')
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, blank=True, null=True, related_name='photos')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="district")
    is_agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Photo(BaseModel):
    image = models.ImageField(upload_to='posts')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.post.title


class Complaint(BaseModel):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title


class Saved(BaseModel):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.post
