from django.contrib import admin

# Register your models here.
from expenses_tracker2.expenses import models

admin.site.register(models.Expense)
