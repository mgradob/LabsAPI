from django.conf.urls import include, url
from rest_framework import routers
from Lab_Electronica import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'detailcart', views.DetailCartViewSet)
router.register(r'detailhistory', views.DetailHistoryViewSet)
router.register(r'component', views.ComponentViewSet)
router.register(r'category', views.CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]