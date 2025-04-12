from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class LoginView(View):
  def get(self, request):
    return render(request,'login.html')
  
  def post(self,request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('booking_list')
  
    error = "Username atau password salah"
    return render(request,'login.html',{
      'error':error,
    })
      


def logout_view(request):
  logout(request)

  return redirect('login')

def signup_view(requets):
  return render(requets, 'signup.html')