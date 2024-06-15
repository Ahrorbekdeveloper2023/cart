from django.urls import path
from .views import HomeView, ProductDetailView, CotegoryView, CartDetailView, delete

app_name = 'cart'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('delete<int:delete_id>/', delete, name='delete'),
    path('cotegory<int:id>/', CotegoryView.as_view(), name='cotegory'),
    path('cart-detail/', CartDetailView.as_view(), name='cart_detail'),


]