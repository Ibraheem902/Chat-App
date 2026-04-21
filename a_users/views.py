
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.contrib.auth import logout


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    return render(request, 'a_users/profile.html', {'profile':profile})

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False
    
    return render(request, 'a_users/profile_edit.html', {'form':form, 'onboarding':onboarding})

@login_required
def profile_settings_view(request):
    return render(request, 'a_users/profile_settings.html')

@login_required
def profile_emailchange(request):
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)
        if form.is_valid():
            
            #check if email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already taken.')
                return redirect('profile_settings')
            form.save()
            
            #then signal updates emailaddress and set verified to False
            user = request.user
            try:
                email_address = EmailAddress.objects.get_primary(user)
                if email_address.email != user.email:
                    email_address.email = user.email
                    email_address.verified = False
                    email_address.save()
                    email_address.send_confirmation(request)
            except:
                EmailAddress.objects.create(
                    user=user,
                    email=user.email,
                    verified=False,
                    primary=True
                ).send_confirmation(request)
            #then send confirmation email
            return redirect('profile_settings')
        else:
            messages.warning(request, 'Please enter a valid email address.')
            return redirect('profile_settings')
    return redirect('home')

@login_required
def profile_emailverify(request):
    email_address = get_object_or_404(EmailAddress, user=request.user,primary=True)
    email_address.send_confirmation(request)
    return redirect('profile_settings')

@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')
    
    return render(request, 'a_users/profile_delete.html')