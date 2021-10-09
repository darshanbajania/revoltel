from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'revoltel_site'

urlpatterns = [
    path('', views.Home_view, name='home_page'),
    path('about_us/', views.About_us_view, name='about_us_page'),
    path('contact_us/', views.Contact_us_view, name='contact_us_page'),
    path('all_in_one_pbx/', views.Product1_view, name='all_in_one_pbx'),
    path('call_center_dialer/', views.Product2_view, name='call_center_dialer'),
    path('crm/', views.Product3_view, name='crm'),
    path('hospital_pbx/', views.Product4_view, name='hospital_pbx'),
    path('multi_level_ivr/', views.Product5_view, name='multi_level_ivr'),
    path('real_estate/', views.Product6_view, name='real_estate'),
    path('telecom_consultant/', views.Product7_view, name='telecom_consultant'),
    path('virtual_extension/', views.Product8_view, name='virtual_extensions'),
    path('login/', views.Login_View, name="login_view"),
    path('register/', views.register_view, name="register_view"),
    path('logout/', LogoutView.as_view(next_page='revoltel_site:home_page'),
         name="logout_url"),
    path('shop/', views.Shop_view, name='shop_page'),
    path('product_view/', views.Product_view_page, name='product_view_page'),
    path('services/', views.Services_view, name='services_page'),
    path('cart/', views.Cart_view, name='cart_page'),
    path('checkout/', views.Checkout_view, name='payment_page'),
    path('payment_status/', views.Payment_complete_view,
         name='payment_complete_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
