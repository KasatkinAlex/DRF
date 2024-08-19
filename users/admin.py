from django.contrib import admin

from users.models import User, UserPayment

# admin.site.register(User)


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_payment', 'amount', 'method')
    search_fields = ('user', 'course_paid', 'lesson_paid')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone')
    search_fields = ('email', 'phone')
