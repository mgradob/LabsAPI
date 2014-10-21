from django.conf.urls import include, url
from rest_framework import routers
from Lab_Electronica.views import StudentViewSet, DetailCartViewSet, DetailHistoryViewSet, ComponentViewSet, CategoryViewSet
from BetaTesters.views import TestersViewSet

lab_electronica_router = routers.DefaultRouter()
lab_electronica_router.register(r'student', StudentViewSet)
lab_electronica_router.register(r'detailcart', DetailCartViewSet)
lab_electronica_router.register(r'detailhistory', DetailHistoryViewSet)
lab_electronica_router.register(r'component', ComponentViewSet)
lab_electronica_router.register(r'category', CategoryViewSet)

testers_router = routers.DefaultRouter()
testers_router.register(r'testers', TestersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^elec/', include(lab_electronica_router.urls)),
    url(r'^testers/', include(testers_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]