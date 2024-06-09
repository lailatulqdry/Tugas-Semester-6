from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app_Ecommerce.views import CategoryList, CategoryDetail, ProductList, ProductDetail, CheckoutList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', CategoryList.as_view()),
    path('api/category/<int:pk>/', CategoryDetail.as_view()),
    path('api/product/', ProductList.as_view()),
    path('api/product/<int:pk>/', ProductDetail.as_view()),
    path('api/checkout/', CheckoutList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)