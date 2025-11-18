from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserProfile
from ratelimit.decorators import ratelimit
import logging


def home(request):
    return render(request , 'accounts\home.html', {'name': 'John Doe'})

logger = logging.getLogger('notes')
@ratelimit(key='ip', rate='5/m', block=True)
def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_profile = UserProfile.objects.get(email=email, password=password)
            logger.info(f"User {email} logged in successfully.")
            return render(request ,'main/note_home.html')
        except UserProfile.DoesNotExist:
            logger.warning(f"Failed login attempt for email: {email}")
            return HttpResponse("Invalid email or password.")   
        
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        # Handle signup logic here
        email = request.POST.get('email')
        name = request.POST.get('name')
        birth_date = request.POST.get('birth_date')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Create user profile 

            user_profile = UserProfile(
                email=email,
                name=name,
                birth_date=birth_date,
                password=password
            )
            user_profile.save()
            return HttpResponse("Signup successful!")
        else:
            return HttpResponse("Passwords do not match.")
        

    return render(request, 'accounts/signup.html')

