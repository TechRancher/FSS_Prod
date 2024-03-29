from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contactRep/', views.contactRep_view, name="contactRep"),
    path('salesInfo/', views.salesInfo_view, name="salesInfo"),
    path('otherMarkets/', views.otherMarket_view, name="otherMarkets"),
    path('BuyerSellerInfo/', views.info_view, name="info"),
]
