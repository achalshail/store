from rest_framework import routers
from contact.views import ContactViewset
from login.views import RegisterViewSet
from login.views import RegisterViewSet, LoginViewSet
from product.views import ProductViewset
from checkout.views import CheckoutViewSet



router = routers.DefaultRouter()
router.register(r'contacts', ContactViewset)
router.register(r'register', RegisterViewSet)
router.register(r'login', LoginViewSet)
router.register(r'products', ProductViewset)
router.register(r'checkout', CheckoutViewSet)