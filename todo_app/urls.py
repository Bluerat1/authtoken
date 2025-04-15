from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, SecureHelloView



router = DefaultRouter()
router.register(r'todos', TodoItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('secure-hello/', SecureHelloView.as_view()),

]