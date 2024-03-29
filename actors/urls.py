from django.urls import path
from actors import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
