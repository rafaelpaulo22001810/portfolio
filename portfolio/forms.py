from django.forms import ModelForm

from .models import Post
from .models import Cadeira
from .models import Projeto
from .models import Tfc


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class ProjectForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'


class TfcForm(ModelForm):
    class Meta:
        model = Tfc
        fields = '__all__'
