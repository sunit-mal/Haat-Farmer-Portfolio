from django.contrib import admin
from django.urls import path
from FarmersMarket import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='userlogin'),
    path('signup/', views.uesr_signup, name='usersignup'),
    path('logout/', views.user_logout, name='userlogout'),
    path('upload/',views.ProductPost,name='upload'),
    path('postProduct/<str:name>',views.uploadProduct,name='postProduct'),
    path('Mydetails/',views.farmerDetails,name='Mydetails'),
    path('addDetails/',views.detailsAdd,name='addDetails'),
    path('otp/<int:otp>',views.otp,name='otp'),
    path('orderdetails/',views.OrderDetails,name='orderdetails'),
    path('myorder/',views.myorder,name='myorder'),
    path('orderplace/<int:id>',views.orderPlace,name='orderplace'),
    path('deleteProduct/<int:id>',views.deleteProduct,name='deleteProduct'),
    path('placeOrder/<int:id>',views.placeOrder,name='placeOrder'),
    path('detailsDelete/<str:username>',views.detailsDelete,name='detailsDelete'),
    path('DeleteMyOrder/<int:id>',views.DeleteMyOrder,name='DeleteMyOrder'),
    path('payment/',views.paymentProcess,name='payment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
