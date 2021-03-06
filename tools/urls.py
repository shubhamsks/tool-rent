from django.urls import path
from .views import ListCreateTools, RetrieveUpdateDeleteTool, GetTopRatedTools, LatestTools

urlpatterns = [
    path('', ListCreateTools.as_view(), name='list-create-tools'),
    path('<uuid:tool_id>/', RetrieveUpdateDeleteTool.as_view(), name='get-update-delete-tool'),
    path('top-rated/', GetTopRatedTools.as_view(), name='get-top-rated-tools'),
    path('latest/', LatestTools.as_view(), name='latest-tools'),
]
