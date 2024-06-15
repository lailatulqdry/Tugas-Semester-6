from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app_Ecommerce.views import CategoryList, CategoryDetail, ProductList, ProductDetail, CheckoutList, CheckoutDetail, ReviewList, ReviewDetail, paymentList, paymentDetail, CustomUserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', CustomUserCreateView.as_view(), name='custom-user-register'),
    path('api/category/', CategoryList.as_view()),
    path('api/category/<int:pk>/', CategoryDetail.as_view()),
    path('api/product/', ProductList.as_view()),
    path('api/product/<int:pk>/', ProductDetail.as_view()),
    path('api/checkout/', CheckoutList.as_view()),
    path('api/checkout/<int:pk>/', CheckoutDetail.as_view()),
    path('api/review/', ReviewList.as_view()),
    path('api/review/<int:pk>/', ReviewDetail.as_view()),
    path('api/payment/', paymentList.as_view()),
    path('api/payment/<int:pk>/', paymentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)