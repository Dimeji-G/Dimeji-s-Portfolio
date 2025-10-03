from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectImage, Technology, Contact


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'status', 'visible', 'order', 'created_at', 'image_preview']
    list_filter = ['category', 'featured', 'status', 'visible', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'visible', 'order']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'short_description', 'category')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url', 'documentation_url')
        }),
        ('Media', {
            'fields': ('image', 'thumbnail')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'status')
        }),
        ('Project Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display Settings', {
            'fields': ('featured', 'visible', 'order')
        }),
    )
    
    inlines = [ProjectImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"
    
    actions = ['make_featured', 'remove_featured', 'make_visible', 'make_hidden']
    
    def make_featured(self, request, queryset):
        queryset.update(featured=True)
    make_featured.short_description = "Mark selected projects as featured"
    
    def remove_featured(self, request, queryset):
        queryset.update(featured=False)
    remove_featured.short_description = "Remove featured status from selected projects"
    
    def make_visible(self, request, queryset):
        queryset.update(visible=True)
    make_visible.short_description = "Make selected projects visible"
    
    def make_hidden(self, request, queryset):
        queryset.update(visible=False)
    make_hidden.short_description = "Hide selected projects"


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'icon_preview', 'color_preview']
    list_filter = ['category']
    search_fields = ['name']
    
    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="{}"></i> {}', obj.icon, obj.icon)
        return "No Icon"
    icon_preview.short_description = "Icon"
    
    def color_preview(self, obj):
        if obj.color:
            return format_html(
                '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #ccc; display: inline-block; margin-right: 5px;"></div> {}',
                obj.color, obj.color
            )
        return "No Color"
    color_preview.short_description = "Color"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'replied']
    list_filter = ['subject', 'replied', 'newsletter', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    list_editable = ['replied']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Preferences & Status', {
            'fields': ('newsletter', 'replied', 'created_at')
        }),
    )
    
    actions = ['mark_as_replied', 'mark_as_unread']
    
    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)
    mark_as_replied.short_description = "Mark selected messages as replied"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(replied=False)
    mark_as_unread.short_description = "Mark selected messages as unread"


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order', 'image_preview']
    list_filter = ['project']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"
