from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, RegisterUserForm
from .forms import SignUpForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from myweb import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str,force_bytes
from .forms import UserRegisterForm
from . tokens import generate_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse  
from .forms import LoginForm, SignUpForm  



 

# def signup(request):  
#     if request.method == 'POST':  
#         form = SignUpForm(request.POST)  
#         if form.is_valid():  
#             user = form.save(commit=False)  
#             user.set_password(form.cleaned_data['password'])  
#             user.save()  
#             return redirect('signin')  # Redirect to login or wherever you want  
#     else:  
#         form = SignUpForm()  
#     return render(request, 'authentical/signup.html', {'form': form})

# Create your views here.
# def login_user(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request,user)
#                 return redirect('myapp/')
#         else:
#             messages.success(request,'There was a error logging in')
#             return render(request,'authentical/login.html')
        
#     else:
#         return render(request,'authentical/login.html')
def index(request):
    return render(request, 'authentical/index.html')
    

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         #email=request.POST.get('email')
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('calendar1')
        
#         else:
#             messages.success(request, 'There was an error logging pls try again')
#             return redirect('signin')
    

#     else:
#         return render(request, "authentical/signin2.html")


def user_login(request):  
    if request.method == 'POST':  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username')
#           
            password = form.cleaned_data['password']  
            user = authenticate(request, username=username, password=password)  
            if user is not None:  
                login(request, user)  
                return redirect('workorder-1')  # Change 'home' to your target page  
            else:  
                return HttpResponse("Invalid login")  
    else:  
        form = LoginForm()  
    return render(request, 'authentical/signin.html', {'form': form})  
    



    
def logout_user(request):
    logout(request)
    messages.success(request, 'You were successfully logged out')
    return redirect('signin')


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                return redirect('signin')
            elif User.objects.filter(email = email).exists():
                return redirect('register_user')
            else:
                user=User.objects.create_user(username = username,email = email)
                user.save()
            return redirect('signin')
        else:
            return redirect('/')

    else:
        return render(request, 'authentical/signup.html')



# def registration(request):
#     c= {}
#     c.update(csrf(request))
#     state = "Please Register below..."
#     username = None
#     email = None
#     password = None
#     user_success = None
#     user_created = None
#     if request.method=="POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print ("username ",username)

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 user_created = True
#         else:
#             user_created = False
#     else:
#         user = User.objects.create_user(username=username,password=password,email=email)
#         user.save()
#         user.is_active = True
#         user_success = True

#     return render_to_response('register.html',{'success':user_success,'created':user_created,'username': username},context_instance = RequestContext(request))

# def index(request):
#     return render(request,'authentical/index.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             ######################### mail system #################################### 
#             htmly = get_template('user/Email.html')
#             d = { 'username': username }
#             subject, from_email, to = 'welcome', 'your_email@gmail.com', email
#             html_content = htmly.render(d)
#             msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()
#             ################################################################## 
#             messages.success(request, f'Your account has been created ! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  