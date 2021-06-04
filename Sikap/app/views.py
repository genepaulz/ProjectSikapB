from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import *
from django.template import *
from .import views
from datetime import *
from passlib.hash import pbkdf2_sha256

#from .forms import *
# Create your views here.

#START OF LANDING

class LandingView(View):
    def get(self,request):
        return render(request,'index.html')

#END OF LANDING


#START OF LOGIN

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("pass")

        q = User.objects.get(email=email)
        #if(q.password == password):
        if(q.verify_password(password)):
            if(q.user_type):
                #IMPLEMENT CONTEXT HERE
                return render(request,'viewase.html')
            else:
                #IMPLEMENT CONTEXT HERE
                return render(request,'applicant.html')
        else:
            return HttpResponse("User does not EXIST!")

#END OF LOGIN


#START OF REGISTER

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):        
        if 'applicant' in request.POST:
                account_type = 1
                email = request.POST.get("aemail")
                password = request.POST.get("apassword")
                name = request.POST.get("aname")
                surname = request.POST.get("asurname")
                user_type = 0
                isVerified = 0
                industry = request.POST.get("aindustry")
                region = request.POST.get("aregion")
                province = request.POST.get("aprovince")
                city = request.POST.get("acity")
                age = request.POST.get("aage")

                #Encrypt Password
                enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16);


                print(account_type)
                print(email)
                print(password)
                print(name)
                print(surname)
                print(user_type)
                print(isVerified)
                print(industry)
                print(region)
                print(province)
                print(city)
                print(age)

                form = User(
                    account_type = account_type,
                    email = email,
                    password = enc_password,
                    name = name,
                    surname = surname,
                    user_type = user_type,
                    isVerified = isVerified,
                    companyName = "",
                    industry = industry,
                    region = region,
                    province = province,
                    city = city,
                    age = age
                )
                form.save()                
                return redirect('app:landing_view')

        elif 'employer' in request.POST:
                account_type = 1
                email = request.POST.get("eemail")
                password = request.POST.get("epassword")
                name = request.POST.get("ename")
                surname = request.POST.get("esurname")
                user_type = 1
                isVerified = 0
                companyName = request.POST.get("ecompanyName")
                industry = request.POST.get("eindustry")

                #encrypt password
                enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16);


                print(account_type)
                print(email)
                print(password)
                print(name)
                print(surname)
                print(user_type)
                print(isVerified)
                print(industry)

                form = User(
                    account_type = account_type,
                    email = email,
                    password = enc_password,
                    name = name,
                    surname = surname,
                    user_type = user_type,
                    isVerified = isVerified,
                    companyName = companyName,
                    industry = industry,
                    region = "",
                    province = "",
                    city = "",
                    age = 0
                )
                form.save()
                return redirect('app:landing_view')

#END OF LOGIN


#START OF VIEWAS

class ViewAsAView(View):
    def get(self,request):
        return render(request,'applicant.html')

    
class ViewAsEView(View):
    def get(self,request):
        return render(request,'viewase.html')

#END OF VIEWAS


#START OF POSTS

class PostsView(View):
    def get(self,request):
        return render(request,'createpost.html')

    def post(self,request):        
        yearsOfExperience = request.POST.get("yearsOfExperience")
        industry = request.POST.get("industry")
        region = request.POST.get("region")
        province = request.POST.get("province")
        city = request.POST.get("city")
        age = request.POST.get("age")
        isAgeViewable = request.POST.get("isAgeViewable")
        if isAgeViewable == 'on':
            isAgeViewable = 1
        else:
            isAgeViewable = 0

        form = Posts(
            yearsOfExperience = yearsOfExperience,
            industry = industry,
            region = region,
            province = province,
            city = city,
            age = age,
            dateadded = datetime.now(),
            # EMAIL TO BE IMPLEMENTED WHEN WE HAVE SESSIONS
            isAgeViewable = isAgeViewable
        )
        form.save()
        return redirect('app:posts_view')

#END OF POSTS