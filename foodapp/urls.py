from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('categories',views.CategoriesView)
router.register('dish',views.DishView)
router.register('orders',views.OrdersView)

urlpatterns = [
    path('',include(router.urls))
]