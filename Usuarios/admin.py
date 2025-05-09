from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Add custom fields to the list_display in the admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')

    # Add custom fields to the fieldsets for the add/change forms
    # This organizes fields in the admin interface when editing a user
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información Personal', {'fields': ('cedula', 'telefono', 'fecha_nacimiento', 'direccion')}),
        ('Rol y Académico', {'fields': ('role', 'especialidad', 'departamento')}),
    )
    
    # Add custom fields to the add_fieldsets for the user creation form
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name')}), # Standard fields
        ('Información Personal', {'fields': ('cedula', 'telefono', 'fecha_nacimiento', 'direccion')}),
        ('Rol y Académico', {'fields': ('role', 'especialidad', 'departamento')}),
    )

    # Add custom fields to search functionality
    search_fields = BaseUserAdmin.search_fields + ('role', 'cedula')
    
    # Add custom fields to filter options
    list_filter = BaseUserAdmin.list_filter + ('role', 'is_staff', 'is_superuser', 'is_active')

admin.site.register(User, UserAdmin)
# Register your models here.
