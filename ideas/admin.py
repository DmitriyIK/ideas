from django.contrib import admin

from .models import Idea


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = (
        "fio", "group", "course", "direction",
        "status", "allow_publish", "created_at",
    )
    list_filter = ("status", "course", "direction")
    search_fields = ("fio", "idea_brief", "email", "telegram")
    readonly_fields = ("created_at",)
    actions = ["publish_selected", "reject_selected"]

    @admin.action(description="Опубликовать выбранные заявки")
    def publish_selected(self, request, queryset):
        queryset.update(status="published")

    @admin.action(description="Отклонить выбранные заявки")
    def reject_selected(self, request, queryset):
        queryset.update(status="rejected")
