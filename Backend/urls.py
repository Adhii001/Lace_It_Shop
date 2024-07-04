from django.urls import path
from Backend import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('add_category/', views.add_category, name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:c_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:c_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),
    path('add_product/', views.add_product, name="add_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('update_product02/<int:pro_id>/', views.update_product02, name="update_product02"),
    path('delete_product/<int:pro_id>/', views.delete_product, name="delete_product"),
    path('edit_product/<pro_id>/', views.edit_product, name="edit_product"),
    path('login_page/', views.login_page, name="login_page"),
    path('', views.admin_login, name="admin_login"),
    path('logout/', views.logout, name="logout"),
    path('contact_info/', views.contact_info, name="contact_info"),
]