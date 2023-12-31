
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Shophome"),
    path("about/",views.about,name="about us"),
    path("contact/",views.contact,name="contact"),
    path("tracker/",views.tracker,name="tracking status"),
    path("search/",views.search,name="search"),
    path("productview/<int:myid>",views.productview,name="product"),
    path("checkout/",views.checkout,name="checkout"),
    path("handlerequest/",views.handlerequest,name="handlerequest")

]