from django.urls import path,include
from .views import *
urlpatterns = [
    path('houses/', houses),
    path('house-details/<slug:slug>/',house_details),
    path('agent-details/<slug:slug>/',agent_details),
    path('users/me/',userProfile),
    path('users/',allusers),
    path('agents/me/',agentProfile),
    path('agents/',allagents),
    path('sign-up/',signup)
] 