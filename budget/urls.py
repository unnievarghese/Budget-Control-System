"""budgetcontrolsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from budget.views import registration,signin,signout,expense_create,create_category,viewexpense,edit_expense,\
        delete_expense,review_expense,home

urlpatterns = [
        path("",home,name='home'),
        path("registration",registration,name='registraion'),
        path("signin",signin,name='signin'),
        path('signout',signout,name='signout'),
        path('addexpense',expense_create,name='addexpense'),
        path('addcategory',create_category,name='addcategory'),
        path('viewexpense',viewexpense,name='viewexpense'),
        path('editexpense/<int:id>',edit_expense,name='editexpense'),
        path('deleteexpense/<int:id>',delete_expense,name='deletexpense'),
        path('reviewexpense',review_expense,name='reviewexpense')
]
