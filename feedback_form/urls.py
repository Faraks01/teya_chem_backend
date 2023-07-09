from rest_framework import routers

from .views import *

app_name = 'feedback_form'

router = routers.SimpleRouter()

router.register('', FeedbackFormViewSet, basename='feedback_form')

urlpatterns = router.urls
