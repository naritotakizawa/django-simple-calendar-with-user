from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('user/<int:user_pk>/week_with_schedule/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
    path(
        'user/<int:user_pk>/week_with_schedule/<int:year>/<int:month>/<int:day>/',
        views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'
    ),
    path(
        'user/<int:user_pk>/month_with_schedule/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'user/<int:user_pk>/month_with_schedule/<int:year>/<int:month>/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path('user/<int:user_pk>/mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'user/<int:user_pk>/mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
    ),
    path(
        'user/<int:user_pk>/month_with_forms/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path(
        'user/<int:user_pk>/month_with_forms/<int:year>/<int:month>/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
]
