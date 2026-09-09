from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'learning_logs'

urlpatterns = [
path('', views.index, name='index'),

```
path('topics/', views.topics, name='topics'),

path('topics/<int:topic_id>/', views.topic, name='topic'),

path('new_topic/', views.new_topic, name='new_topic'),

path(
    'topics/<int:topic_id>/new_entry/',
    views.new_entry,
    name='new_entry'
),

path(
    'topics/<int:topic_id>/edit_entry/<int:entry_id>/',
    views.edit_entry,
    name='edit_entry'
),

path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ),
    name='login'
),

path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),
```

]
