from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ArticleViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls
urlpatterns += [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
]
