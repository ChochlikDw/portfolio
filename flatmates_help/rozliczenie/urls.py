from django.urls import path
from . import views

urlpatterns = [
    #ex: /user/3
    path('user/<str:user_id>/', views.user_detail, name='user_detail'),
    #ex: /expense/5
    path('expense/<int:expense_id>/', views.expense_detail, name='expense_detail'),
    #ex: /users/
    path('users/', views.users, name='users'),
    #ex: /login
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post_expense/', views.post_expense, name='post_expense'),
    #ex: /
    path('', views.expenses, name='expenses'),
]
