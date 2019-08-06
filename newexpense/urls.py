from django.urls import path
from newexpense import views


urlpatterns = [

    path('category/', views.loadCategory, name='category'),
    path('home/', views.home, name='home'),
    path('save2/', views.saveCategory, name='save2'),
    path('deleteCategory/', views.deleteCategory, name='deleteCategory'),
    path('getCategoryByType/', views.getCategoryByType, name='getCategoryByType'),
    path('saveIncomeExpense/', views.saveIncomeExpense, name='saveIncomeExpense'),
    path('incomes/', views.incomeList, name='incomes'),
    path('expenses/', views.expenseList, name='expenses'),
    path('deleteIncome/', views.deleteIncome, name='deleteIncome'),
    path('deleteExpense/', views.deleteExpense, name='deleteExpense'),
    path('income_edit/<int:pk>', views.incomeUpdate, name='income_edit'),
    path('expense_edit/<int:pk>', views.expenseUpdate, name='expense_edit'),

]