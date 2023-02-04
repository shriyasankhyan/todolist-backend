from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'api/todos',TodoViewSet,'todos')

urlpatterns = router.urls