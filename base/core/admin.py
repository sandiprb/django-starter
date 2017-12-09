# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUsrAdmin

from .models import User


class UserAdmin(DjangoUsrAdmin):
    search_fields = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_verified', 'is_superuser')
    list_filter = ('is_verified',)
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Status', {'fields': ('is_verified', 'is_active')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
         ),
    )
    ordering = ('id',)


admin.site.register(User, UserAdmin)
