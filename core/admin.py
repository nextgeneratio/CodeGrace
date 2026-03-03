from django.contrib import admin
from .models import TeamMember, Project, Task


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'joined_at')
    search_fields = ('user__username', 'user__email', 'role')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    filter_horizontal = ('members',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'status', 'created_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')
