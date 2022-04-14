from django.urls import path
from .views import CreateVisitMembroView, DeleteVisitMembroView,  UpdateVisitMembroView,  IndexView,  ListsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateVisitMembroView.as_view(), name='add_visitmembro'),
    path('<int:pk>/update/', UpdateVisitMembroView.as_view(), name='upd_visitmembro'),
    path('<int:pk>/delete/', DeleteVisitMembroView.as_view(), name='del_visitmembro'),
    path('listas/', ListsView.as_view(), name='listas'),
]
