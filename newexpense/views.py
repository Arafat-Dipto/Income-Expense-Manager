from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Category
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum
from django.forms import ModelForm


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['type', 'category', 'amount', 'description', 'date_created']

def getCategoryByType(request):
    type = request.GET.get('type', None)
    print(type)
    all= Category.objects.filter(typeName=type)
    categoryList= list(all)
    newLi=[]
    for x in categoryList:
        newLi.append(x.categoryName)
    data = {
        'categoryList': newLi,
        "name": 'arafat'
    }
    print(data)
    return JsonResponse(data)




def saveCategory(request):
    if request.method == 'POST':
        if request.POST.get('categoryName') and request.POST.get('typeName'):
            category = Category()
            category.categoryName = request.POST.get('categoryName')
            category.typeName = request.POST.get('typeName')
            user2 = request.user.get_username()
            print(type(user2))
            category.userName = user2
            category.save()
            return redirect('category')



    else:
        return render(request, 'newexpense/category.html')

@login_required
def loadCategory(request):

    categoryList = Category.objects.filter(userName=request.user.get_username())
    print(categoryList)
    context={
        'categoryList': categoryList,
    }
    return render(request, 'newexpense/category.html', context)

def deleteCategory(request):
    if request.method == 'POST':
        if request.POST.get('categoryId'):
            category = Category()
            category.id = request.POST.get('categoryId')
            print(category.id)
            category.delete()
            return redirect('category')


def deleteIncome(request):
    if request.method == 'POST':
        if request.POST.get('incomeId'):
            income = Expense()
            income.id = request.POST.get('incomeId')
            print(income.id)
            income.delete()
            return redirect('incomes')

def deleteExpense(request):
    if request.method == 'POST':
        if request.POST.get('expenseId'):
            expense = Expense()
            expense.id = request.POST.get('expenseId')
            print(expense.id)
            expense.delete()
            return redirect('expenses')



def incomeUpdate(request, pk, template_name='newexpense/income_edit.html'):
    income = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, instance=income)
    if form.is_valid():
        form.save()
        return redirect('incomes')

    return render(request, template_name, {'form':form})

def expenseUpdate(request, pk, template_name='newexpense/expenseedit.html'):
    expense = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('expenses')

    return render(request, template_name, {'form':form})


@login_required
def home(request):

    sumIncome = Expense.objects.filter(type='income',userName=request.user.get_username()).aggregate(Sum('amount'))['amount__sum']
    print(sumIncome)
    if sumIncome is None:
        sumIncome =0
    sumExpense = Expense.objects.filter(type='expense',userName=request.user.get_username()).aggregate(Sum('amount'))['amount__sum']
    print(sumExpense)
    if sumExpense is None:
        sumExpense =0
        total = sumIncome - sumExpense
    else:
        total = sumIncome-sumExpense
    print(total)

    data = {
        'balance': total
    }

    return render(request, 'newexpense/home.html', data)

@login_required
def incomeList(request):
    incomeList = Expense.objects.filter(type='income', userName=request.user.get_username())
    context={
        'incomeList':incomeList
    }
    print(incomeList)
    return render(request, 'newexpense/income.html', context)

@login_required
def expenseList(request):
    expenseList = Expense.objects.filter(type='expense', userName=request.user.get_username())
    context={
        'expenseList':expenseList
    }
    print(expenseList)
    return render(request, 'newexpense/expense.html', context)


def saveIncomeExpense(request):
    if request.method == 'POST':
        if request.POST.get('category') and request.POST.get('type') and request.POST.get('amount') and request.POST.get('description') :
            data = Expense()
            data.date_created = request.POST.get('date')
            data.type = request.POST.get('type')
            data.category = request.POST.get('category')
            data.amount = request.POST.get('amount')
            data.description = request.POST.get('description')
            data.userName = request.user.get_username()
            data.save()
            if data.type=='income':
                return redirect('incomes')
            elif data.type=='expense':
                return redirect('expenses')

            print(data)
            all_data = Expense.objects.all()
            context = {
                'data': all_data
            }
            return redirect('home')


