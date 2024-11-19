from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(BlogModel)
admin.site.register(NewsLetterModel)
admin.site.register(CommentModel)
