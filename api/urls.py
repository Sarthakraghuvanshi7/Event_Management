from django.contrib import admin
from django.urls import path,include
from api.views import *
from rest_framework import routers


router= routers.DefaultRouter()
# router.register(r'companies', CompanyViewSet, basename='Product')
# router.register(r'singup', RegisterView)
# router.register(r'venues', VenueViewSet)
# router.register(r'registration', RegistrationViewSet)
# router.register(r'events', EventView)

# urlpatterns = router.urls
urlpatterns = [    
    path('',include(router.urls)),
    path('get-token/', MyObtainTokenPairView.as_view(), name='get-token'),
    path('signup/', RegisterView.as_view(), name='auth_register'),
    path('events/', EventView.as_view(), name='events'),
    path('venues/', VenueViewSet.as_view(), name='venues'),
    # path('registration/', RegistrationViewSet.as_view(), name='registration'),
    
]



