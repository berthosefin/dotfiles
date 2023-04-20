from django.urls import path
from .views import index, login, register, add_friend, show_profile, modify_profile, ajax_check_email_field, ajax_add_frien


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('addFriend/', add_friend, name='addFriend'),
    path('showProfile/', show_profile, name='showProfile'),
    path('modifyProfile/', modify_profile, name='modifyProfile'),
    path('ajax/checkEmailField', ajax_check_email_field, name='ajax-checkEmailFiled'),
]