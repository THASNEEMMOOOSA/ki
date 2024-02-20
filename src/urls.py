from django.urls import path,include
from .views import index,bookpage,savepage,payment_status
urlpatterns = [
    path('', index ,name="index"),
    # path('test/', payment_process ,name="payment_process"),
    # path('success/', success ,name="success"),


    path('bookpage/<int:id>/', bookpage ,name="bookpage"),
    path('bookpage/<int:id>/savepage/', savepage ,name="savepage"),
    path('payment-status', payment_status, name='payment-status'),
    # path('index/bookpage/<int:id>/savepage/<int:id>/sumpage', sumpage ,name="sumpage"),
    # path('bookpage/<int:id>/savepage/sumpage/', sumpage ,name="sumpage"),





]
