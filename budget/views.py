from django.shortcuts import render,redirect
from budget.forms import userregistrationform,createexpenseform,createcategoryform,datesearchform,review_expenseform
from django.contrib.auth import authenticate,login,logout
from budget.models import expense
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        user=authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return render(request,'budget/Home.html')
        else:
            return render(request,'budget/signin.html')
    return render(request,'budget/signin.html')

def registration(request):
    form=userregistrationform()
    context={}
    context['form']=form
    if request.method=='POST':
        form=userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request,'budget/registration.html',context)

def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def home(request):
    return render(request,'budget/Home.html')

@login_required
def expense_create(request):
    form=createexpenseform(initial={'user':request.user})
    context={}
    context['form']=form
    if request.method=='POST':
        form=createexpenseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addexpense')
    return render(request,'budget/addexpense.html',context)

@login_required
def create_category(request):
    form=createcategoryform()
    context={}
    context['form']=form
    if request.method=='POST':
        form=createcategoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcategory')
    return render(request,'budget/addcategory.html',context)

@login_required
def viewexpense(request):
    form=datesearchform()
    expens=expense.objects.filter(user=request.user)
    context={}
    context['expens']=expens
    context['form']=form
    if request.method=='POST':
        form=datesearchform(request.POST)
        if form.is_valid():
            date=form.cleaned_data.get('date')
            expens=expense.objects.filter(user=request.user,date=date)
            context={}
            context['expens']=expens
            form = datesearchform()
            context['form']=form
            return render(request,'budget/viewexpense.html',context)
        else:
            context['form']=form
            return render(request,'budget/viewexpense.html',context)
    return render(request,'budget/viewexpense.html',context)

@login_required
def edit_expense(request,id):
    expens=expense.objects.get(id=id)
    form=createexpenseform(instance=expens)
    context={}
    context['form']=form
    if request.method=="POST":
        form=createexpenseform(request.POST,instance=expens)
        if form.is_valid():
            form.save()
            return redirect('viewexpense')
    return render(request,'budget/editexpense.html',context)

@login_required
def delete_expense(request,id):
    expens=expense.objects.get(id=id)
    expens.delete()
    return redirect('viewexpense')

@login_required
def review_expense(request):
    form=review_expenseform()
    context={}
    context['form']=form
    if request.method=='POST':
        form=review_expenseform(request.POST)
        if form.is_valid():
            from_date=form.cleaned_data.get('from_date')
            to_date=form.cleaned_data.get('to_date')
            total=expense.objects.filter(date__gte=from_date,date__lte=to_date,user=request.user).aggregate(Sum('amount'))
            highest_spender=expense.objects.order_by('-amount')[0].category
            context['highspender']=highest_spender
            context['total']=total['amount__sum']
            return render(request,'budget/reviewexpense.html',context)
    return render(request,'budget/reviewexpense.html',context)