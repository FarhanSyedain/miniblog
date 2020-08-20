from django.contrib import admin
from .models import to_be_added_in_admin_page


for i in to_be_added_in_admin_page:
    admin.site.register(i)


