from django.conf.urls import include, url
from rest_framework import routers
from Lab_Electronica.views import  DetailCartViewSet, DetailHistoryViewSet, ComponentViewSet, CategoryViewSet
from BetaTesters.views import TestersViewSet
from LabsIndex.views import LabsViewSet, StudentViewSet, AdministratorViewSet

lab_electronica_router = routers.DefaultRouter()
lab_electronica_router.register(r'detailcart', DetailCartViewSet)
lab_electronica_router.register(r'detailhistory', DetailHistoryViewSet)
lab_electronica_router.register(r'component', ComponentViewSet, base_name='component-view')
lab_electronica_router.register(r'category', CategoryViewSet)

index_router = routers.DefaultRouter()
index_router.register(r'labs', LabsViewSet)
index_router.register(r'students', StudentViewSet)
index_router.register(r'testers', TestersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(index_router.urls)),
    url(r'^elec/', include(lab_electronica_router.urls)),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^docs/', include('rest_framework_swagger.urls'))
]
