from django.contrib import admin
from django.urls import path, include
#from rest_framework.urlpatterns import format_suffix_patterns
from app_Ecommerce.views import CategoryList, CategoryDetail,  ProductDetail, CheckoutList, CheckoutDetail, ReviewList, ReviewDetail, paymentList, paymentDetail, tampilan, UserViewSet, WishlistListCreateView, WishlistDetailView, CartListCreateView, CartDetailView, ProductCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', tampilan, name='tampilan'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/category/', CategoryList.as_view()),
    path('api/category/<int:pk>/', CategoryDetail.as_view()),
    path('api/product/', ProductCreateView.as_view()),
    path('api/product/<int:pk>/', ProductDetail.as_view()),
    path('api/checkout/', CheckoutList.as_view()),
    path('api/checkout/<int:pk>/', CheckoutDetail.as_view()),
    path('api/review/', ReviewList.as_view()),
    path('api/review/<int:pk>/', ReviewDetail.as_view()),
    path('api/payment/', paymentList.as_view()),
    path('api/payment/<int:pk>/', paymentDetail.as_view()),
    path('api/wishlist/', WishlistListCreateView.as_view()),
    path('api/wishlist/<int:pk>/', WishlistDetailView.as_view()),
    path('api/cart/', CartListCreateView.as_view()),
    path('api/cart/<int:pk>/', CartDetailView.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)