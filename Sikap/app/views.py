from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import *
from .import views
from datetime import *
from passlib.hash import pbkdf2_sha256
from app.models import Posts

#from .forms import *
# Create your views here.

#START OF LANDING

class LandingView(View):
    def get(self,request):
        return render(request,'index.html')
    
    def post(self,request):
        if('login' in request.POST):
            return redirect('app:login_view')
        elif('rega' in request.POST):
            return redirect('app:registera_view')
        elif('rege' in request.POST):
            return redirect('app:registere_view')

#END OF LANDING


#START OF LOGIN

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("pass")

        q = User.objects.get(email=email)
        if(q.verify_password(password)):
            if(q.user_type):
                #IMPLEMENT CONTEXT HERE
                request.session['email'] = q.email       
                request.session['companyName'] = q.companyName
                return redirect('app:viewase_view')
                
            else:
                #IMPLEMENT CONTEXT HERE
                request.session['email'] = q.email
                request.session['name'] = q.firstname
                request.session['surname'] = q.lastname
                request.session['industry'] = q.industry
                request.session['region'] = q.region
                request.session['province'] = q.province
                request.session['city'] = q.city
                request.session['age'] = q.age
                return redirect('app:viewasa_view')
                # return render(request,'applicant.html',context)
                
                
        else:
            return HttpResponse("User does not EXIST!")

#END OF LOGIN


#START OF REGISTERA

class RegisterViewA(View):
    def get(self,request):
        return render(request,'Applicant_Registration.html')

    def post(self,request):
        if 'applicant' in request.POST:
                
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
            enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16)


            
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
                
                email = email,
                password = enc_password,
                firstname = name,
                lastname = surname,
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
        return HttpResponse("Fail")

#END OF REGISTERA

#START OF REGISTERE

class RegisterViewE(View):
    def get(self,request):
        return render(request,'Employer_Registration.html')

    def post(self,request):
        if 'employer' in request.POST: 
            email = request.POST.get("eemail")
            password = request.POST.get("epassword")
            name = request.POST.get("ename")
            surname = request.POST.get("esurname")
            user_type = 1
            isVerified = 0
            companyName = request.POST.get("ecompanyName")
            industry = request.POST.get("eindustry")

            #encrypt password
            enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16)


            
            print(email)
            print(password)
            print(name)
            print(surname)
            print(user_type)
            print(isVerified)
            print(industry)

            form = User(
                
                email = email,
                password = enc_password,
                firstname = name,
                lastname = surname,
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
        return HttpResponse("Fail")

#END OF REGISTERE

#START OF VIEWAS

class ViewAsAView(View):
    def get(self,request):
        return render(request,'applicant.html')
    
    def post(self,request):
        if('post' in request.POST):
            return redirect('app:posts_view')
        elif('logout' in request.POST):
            del request.session['email']
            del request.session['name']
            del request.session['surname']
            del request.session['industry']
            del request.session['region']
            del request.session['province']
            del request.session['city']
            del request.session['age']
            return redirect('app:landing_view')


class ViewAsEView(View):
    def get(self,request):
        return render(request,'viewase.html')
    
    def post(self,request):
        if('logout' in request.POST):
            del request.session['email']
            del request.session['companyName']
            return redirect('app:landing_view')

    
def LiveSearch(request):
    template_name = "index.html"
    filt = request.GET.getlist("d")[0]
    d=""
    mat = Posts.objects.filter(industry__icontains=filt)
    print(filt)
    image = "/static/img_avatar.png"
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
        
    print(d)
    mat = Posts.objects.filter(region__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    mat = Posts.objects.filter(province__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    mat = Posts.objects.filter(city__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    return JsonResponse({"d": d})
    #def get(self, request):
     #   if 'term' in request.GET:
      #      qs = Material.objects.filter(title__icontains=request.GET.get('term'))
       #     titles = list()
        #    for material in qs:
         #       print(material)
          #      titles.append(material.title)
           # return JsonResponse(titles, safe=False)

        #return render(request, 'search.html')    

#END OF VIEWAS


#START OF POSTS

class PostsView(View):
    def get(self,request):
        return render(request,'createpost.html')

    def post(self,request):
        
        yearsOfExperience = request.POST.get("yearsOfExperience")
        position = request.POST.get("position")
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
            position = position,
            industry = industry,
            region = region,
            province = province,
            city = city,
            age = age,
            dateadded = datetime.now(),
            email = request.session['email'],
            isAgeViewable = isAgeViewable,
            firstname = request.session['name'],
            lastname = request.session['surname']
        )
        form.save()
        return redirect('app:viewasa_view')

#END OF POSTS
