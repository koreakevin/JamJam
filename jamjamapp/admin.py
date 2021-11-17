from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserForm
from .models import Post, Profile, Bucket, Blog, Comment, Hashtag, Big_Region, Small_Region, Bookmark, SettingUser


admin.site.register(Blog)
admin.site.register(Hashtag)
admin.site.register(Comment)
admin.site.register(Big_Region)
admin.site.register(Small_Region)


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_site_name', 'book_url']


admin.site.register(Bookmark, BookmarkAdmin)

# ----민정이 개발 부분------

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Bucket)

# ----예찬이 개발 부분------


class UserAdmin(BaseUserAdmin):
    add_form = UserForm

    list_display = ('username', 'email', 'nickname',
                    'phone_number', 'gender', 'is_staff')
    list_filter = ('is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'nickname',
                           'phone_number', 'birthyear', 'birthmonth', 'birthday', 'gender', 'is_active', 'is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)
        }),
    )


admin.site.register(SettingUser, UserAdmin)

# ----광현이 개발 부분------
