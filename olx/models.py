from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from utils.models import BaseModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .choices import PriceTypeChoices, StatusChoices, CodeChoice, PlanChoiceDetail
from options.models import Option, OptionValue


class Region(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="regions")

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='categories')
    order = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="category_options")

    def __str__(self):
        return self.title


class SubCategories(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="subcategory_option")

    def __str__(self):
        return self.title


class Posts(BaseModel):
    title = models.CharField(max_length=128)
    content = models.TextField()
    watched = models.IntegerField(default=0, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="author")
    price = models.IntegerField(blank=True, null=True)
    price_type = models.CharField(max_length=64, choices=PriceTypeChoices.choices)
    status = models.CharField(max_length=64, choices=StatusChoices.choices)

    email = models.EmailField()
    phone = PhoneNumberField(unique=True)
    is_shutdown = models.BooleanField(default=False)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='subcategory')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="districts")
    is_agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Photo(BaseModel):  # rasm
    image = models.ImageField(upload_to='posts')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.post.title


class PostOption(BaseModel):  # Этаж: 8, Этажность дома: 9, Общая площадь: 50
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="posts_options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="post_option")
    value = models.ForeignKey(OptionValue, on_delete=models.CASCADE, related_name="values")


class Plan(BaseModel):
    title = models.CharField(max_length=128)
    plan_detail = models.ManyToManyField("PlanDetail", related_name="details")


class PlanPrice(BaseModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plans")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="plan_category")
    price = models.IntegerField()


class PlanDetailGroup(BaseModel):
    title = models.CharField(max_length=256)
    is_multiple = models.BooleanField(default=False)
    text = models.TextField()


class PlanDetail(BaseModel):
    group_id = models.ForeignKey(PlanDetailGroup, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="groups")
    code = models.CharField(max_length=128, choices=CodeChoice.choices, default=CodeChoice.TOP_UP)
    choice_text = models.CharField(max_length=128, choices=PlanChoiceDetail.choices, default=PlanChoiceDetail.NUll)


class PlanDetailPrice(BaseModel):
    plan_detail = models.ForeignKey(PlanDetail, on_delete=models.CASCADE, related_name="plan_details")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="detail_category")
    price = models.IntegerField()

    def __str__(self):
        return self.plan_detail


class Complaint(BaseModel):  # shikoyat
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title


class Saved(BaseModel):  # like
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="saved_post")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="saved_users")

    def __str__(self):
        return self.post


from config.settings.base import AUTH_USER_MODEL


class Chat(BaseModel):
    from_to = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="to_user")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="chat_posts")


class ChatMessage(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chats", )
    # sender = models.
    message = models.TextField()
