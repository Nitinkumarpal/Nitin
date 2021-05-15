

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login,logout, authenticate
def base(request):
    
    return render(request,'base.html')




def home(request):
    
    return render(request,'home.html')



from django.contrib.auth import login as auth_login

from .forms import SignUpForm
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! You are now become an User.')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



from django.contrib.auth.decorators import login_required

from django.urls import reverse

from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "user_login.html",
                    context={"form":form})



def Slogout(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('login')

    return HttpResponse("Logoout")
@login_required(login_url='/login')
def editsignup(request):
    
    return render(request,'edit_signup.html')


from .models import Post
@login_required(login_url='/login')
def create_blog(request):
    if request.method =='GET':

        return render(request ,'create_blog.html')

    if request.method == 'POST':

        title=request.POST.get('title')       
        slug=request.POST.get('slug')       
        auther=request.POST.get('auther')
        content=request.POST.get('content')
        status=request.POST.get('status')
       
    
        user=Post(title=title,slug=slug,auther=auther,status=status,
        content=content)
        # messages.success(request,"The user "+ request.POST['firstname']+"is Saved Succesfully..!")
        user.save()
        return render(request,'create_blog.html')
    
    return render(request,'create_blog.html')



from .models import Contact_Us


@login_required(login_url='/login')
def Contact(request):
    if request.method=='GET':
        return render(request,'contact.html')
    if request.method=='POST':

        name=request.POST.get('name')
        
      
        
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        user=Contact_Us(name=name,email=email,comment=comment)
        user.save()
        print(user)
    
    return render(request,'contact.html')




from django.views import generic

class blogs(generic.DetailView):
    model = Post
    template_name = 'blogs.html'

from .forms import SearchForm
def blogs_details(request):
    Count=Post.objects.all()
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             blog = Post.objects.get(blog_title=title)
#             return redirect(f'/blogsdetails/{blog.id}')
#     else:
#         form = SearchForm()
#         context = {
#             'dataset':Count,
#             'form':form,
#         }
    return render(request,'bogs_details.html',{'Count':Count})




from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect




@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })