from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateVisitMembroView, DeleteVisitMembroView,  UpdateVisitMembroView,  IndexView, MenuInicialView, ListsView, home_whatsapp, send_whatsapp

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu_inicial/', MenuInicialView.as_view(), name='menu_inicial'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/', CreateVisitMembroView.as_view(), name='add_visitmembro'),
    path('<int:pk>/update/', UpdateVisitMembroView.as_view(), name='upd_visitmembro'),
    path('<int:pk>/delete/', DeleteVisitMembroView.as_view(), name='del_visitmembro'),
    path('listas/', ListsView.as_view(), name='listas'),
    path('home_whatsapp', home_whatsapp, name='home_whatsapp'),
    path('send_whatsapp', send_whatsapp),
]
