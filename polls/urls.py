from rest_framework.routers import DefaultRouter
from django.urls import path

from .apiviews import *

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')


urlpatterns = [
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name='vote_create'),
    path('choices/<int:pk>/', ChoiceDetail.as_view(), name='choice_detail'),
]
urlpatterns += router.urls
