from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('newpost', views.newpost_page_view, name='newpost'),
    path('editar/<int:post_id>', views.editar_page_view, name='editar'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('newcadeira', views.new_cadeira_page_view, name='newcadeira'),
    path('editcadeira/<int:cadeira_id>', views.editar_cadeira_page_view, name='editcadeira'),
    path('newprojeto', views.new_project_page_view, name='newprojeto'),
    path('editprojeto/<int:projeto_id>', views.editar_project_page_view, name='editprojeto'),
    path('tfc', views.tfc_page_view, name='tfc'),
    path('newtfc', views.new_tfc_page_view, name='newtfc'),
    path('edittfc/<int:tfc_id>', views.editar_tfc_page_view, name='edittfc'),
    path('web', views.web_page_view, name='web'),
    path('video', views.video_page_view, name='video'),

]