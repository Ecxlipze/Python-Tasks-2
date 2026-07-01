from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SignupView, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("", include(router.urls)),
]