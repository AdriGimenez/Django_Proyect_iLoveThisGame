from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto', views.contact, name='contact'),
    path('empresa', views.empresa, name='empresa'),
    # /categoria/calzados-deportivos
    re_path(r'^categoria/(?P<name>[-\w]+)$', views.category, name='categoria'),
    re_path(r'^descripcion/(?P<producto>[-\w]+)$', views.descripcion, name='descripcion'),
    path('oferta', views.oferta, name='oferta'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('account/login/',auth_views.LoginView.as_view(template_name='app/registration/login.html'), name='login'),
    path('account/password_change/',auth_views.PasswordChangeView.as_view(success_url='/')),
    path('account/',include('django.contrib.auth.urls')),
    path('perfil', views.perfil, name='perfil'),
    re_path(r'buscar', views.buscar, name='buscar'),

    #Administracion
    #Articulos urls
    path('administracion', views.index_administracion, name='inicio_administracion'),
    path('administracion/articulos/editar/<int:id_articulo>', views.articulos_editar, name='articulos_editar'),
    path('administracion/articulos/eliminar/<int:id_articulo>', views.articulos_eliminar, name='articulos_eliminar'),
    #path('administracion/articulos/nuevo', views.articulos_nuevo, name='articulos_nuevo'),
    path('administracion/articulos', views.articulos_index, name='articulos_index'),
    path('administracion/articulos/nuevo/', views.ArticulosView.as_view(), name='articulos_nuevo'),
    path('administracion/articulos', views.ArticulosListView.as_view(), name='articulos_index'),
    
    #Marcas urls
    path('administracion/marcas/editar/<int:id_marca>', views.marcas_editar, name='marcas_editar'),
    path('administracion/marcas/eliminar/<int:id_marca>', views.marcas_eliminar, name='marcas_eliminar'),
    #path('administracion/marcas/nuevo', views.marcas_nueva, name='marcas_nueva'),
    path('administracion/marcas', views.marcas_index, name='marcas_index'),
    path('administracion/marcas/nuevo/', views.MarcasView.as_view(), name='marcas_nuevo'),
    path('administracion/marcas', views.MarcasListView.as_view(), name='marcas_index'),
  
    #Categorias urls
    path('administracion/categorias/editar/<int:id_categoria>', views.categorias_editar, name='categorias_editar'),
    path('administracion/categorias/eliminar/<int:id_categoria>', views.categorias_eliminar, name='categorias_eliminar'),
    # path('administracion/categorias/nuevo, views.categorias_nueva', name='categorias_nuevo'),
    path('administracion/categorias', views.categorias_index, name='categorias_index'),
    path('administracion/categorias/nuevo/', views.CategoriasView.as_view(), name='categorias_nuevo'),
    path('administracion/categorias', views.CategoriasListView.as_view(), name='categorias_index'),

]
