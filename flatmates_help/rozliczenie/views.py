from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Expense
from .forms import ExpenseForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def index(request):
    return render(request, '')

def user_detail(request, user_id):
    user = get_object_or_404(User, username=user_id)
    expense_list = Expense.objects.filter(user_id=user.id)
    total = sum(expense.price for expense in expense_list)
    return render(request, 'user.html', {'user_': user ,'expense_list': expense_list, 'total': total})

def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'expense_detail.html', {'expense': expense})

def expenses(request):
    expense_list = Expense.objects.all()
    total = sum(expense.price for expense in expense_list)
    context = {'expense_list': expense_list, 'User': User, 'total': total}
    return render(request, 'index.html', context)

def users(request):
    users = User.objects.all()
    sums = [sum(expense.price for expense in Expense.objects.filter(user_id=user.id)) for user in users]
    return render(request, 'users.html', {'users_n_sums': zip(users, sums)})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def post_expense(request):
    if request.method =="POST":
        form = ExpenseForm(request.POST)
        if form.is_valid() and request.user.is_active:
            expense = Expense(description=form.cleaned_data['description'],
                              pub_date=form.cleaned_data['pub_date'],
                              price=form.cleaned_data['price'],
                              user_id=request.user)
            #expense.user = request.user
            expense.save()
        return HttpResponseRedirect('/')
    else:
        form = ExpenseForm()
        return render(request, 'post_expense.html', {'form': form})
