from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {
         'fields': ('first_name', 'last_name', 'fone', 'endereco', 'bairro', 'id_situacao', 'id_sexo', 'imagem', 'data_aniversario')}),
        ('Permissões', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
    )


admin.site.site_header = 'Sistema de Cadastro de Membros e Visitantes'
admin.site.site_title = 'Comunidade Evangélica Salém'
admin.site.index_title = 'Comunidade Evangélica Salém'
