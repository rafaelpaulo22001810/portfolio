from django.contrib import admin
from .models import Post
from .models import Cadeira
from .models import Linguagem
from .models import Professor
from .models import Projeto
from .models import Tfc

# Register your models here.

admin.site.register(Post)
admin.site.register(Cadeira)
admin.site.register(Linguagem)
admin.site.register(Projeto)
admin.site.register(Professor)
admin.site.register(Tfc)

