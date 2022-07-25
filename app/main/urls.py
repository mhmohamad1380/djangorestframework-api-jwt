from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import ShopAPIRetrieveDestroy, ShopAPIList, HomePage,add_email

router = routers.SimpleRouter()

urlpatterns =[
    path("",HomePage.as_view()),
    path("",include(router.urls)),
    path("api/shop/view",ShopAPIList.as_view()),
    path("api/shop/retrieve-destroy/<pk>",ShopAPIRetrieveDestroy.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("add-email",add_email),
    
]