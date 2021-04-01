from django.contrib import admin
from .models import Todo


class To_do_admin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo, To_do_admin)
