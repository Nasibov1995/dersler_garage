
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from bs4 import BeautifulSoup
import requests

def post_job(request):
    return render(request, 'main/post_job.html')

def post_job_it(request):
    if request.method == 'POST':
        sirket = request.POST['sirket']
        maas = request.POST['maas']
        seher = request.POST['seher']
        mezmun = request.POST['mezmun']
        start = request.POST['start']
        end = request.POST['end']
        basliq = request.POST['basliq']
        email = request.POST['email']
        staj = request.POST['staj']
        yash = request.POST['yash']
        tehsil = request.POST['tehsil']
        rejm = request.POST['rejm']
        muqavile = request.POST['muqavile']
        apply_link = request.POST['apply_link']
        text1 = request.POST['text1']
        text2 = request.POST['text2']
        text3 = request.POST['text2']
        text4 = request.POST['text2']

        it = IT(sirket=sirket,maas=maas,muqavile=muqavile,apply_link=apply_link,text1=text1,text2=text2,
            seher=seher,mezmun=mezmun,start=start,end=end,basliq=basliq,email=email,staj=staj,yash=yash,tehsil=tehsil,
            rejm=rejm,text3=text3,text4=text4)
        it.save()
    return render(request, 'main/post_job_it.html')
    
    

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Bu istifadeci artiq movcuddur')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Bu email artiq movcuddur')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login')
        else:
            messages.info(request, 'Parollar uygun deyil')
            return redirect('register')
            
    else:
        return render(request, 'main/register.html')
    


def login(request): 

    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password , request=request) 

        if user is not None:
          
                auth.login(request,user)
                return redirect('index')
         
        else:
            
            messages.info(request, 'Login ve ya parol yanlishdir')
            return redirect('login')
        
    else:
        
        return render(request, 'main/login.html' )
        
def logout(request):
    auth.logout(request)
    return redirect('index')
    


def it(request):
    it = IT.objects.all().order_by('-id')[0:11]
    count = IT.objects.all().count()
    data = {'it':it,'count':count}
    return render(request,'main/it.html',data)

def index(request):
    keyword = request.GET.get('keyword')
    if keyword:
        
        articles = Elan.objects.filter(sirket__contains = keyword)
        return render(request,'main/index.html',{'articles':articles})
    
    elan = Elan.objects.all().order_by('-id')[0:11]
    it = IT.objects.all().count()
    marketinq = Marketinq.objects.all().count()
    neqliyyat = Neqliyyat.objects.all().count()
    satish = Satish.objects.all().count()
    security = Security.objects.all().count()
    senaye = Senaye.objects.all().count()
    techizat = Techizat.objects.all().count()
    tibb = Tibb.objects.all().count()

    data = {'elan':elan,'it':it,'marketinq':marketinq,'tibb':tibb,'satish':satish,'neqliyyat':neqliyyat
            ,'senaye':senaye,'security':security,'techizat':techizat}
    return render(request,'main/index.html',data)

def senaye(request):
    senaye = Senaye.objects.all().order_by('-id')[0:11]

    data = {'senaye':senaye}
    return render(request,'main/senaye.html',data)

def tibb(request):
    tibb = Tibb.objects.all().order_by('-id')[0:11]

    data = {'tibb':tibb}
    return render(request,'main/tibb.html',data)

def neqliyyat(request):
    neqliyyat = Neqliyyat.objects.all().order_by('-id')[0:11]

    data = {'neqliyyat':neqliyyat}
    return render(request,'main/neqliyyat.html',data)

def security(request):
    security = Security.objects.all().order_by('-id')[0:11]

    data = {'security':security}
    return render(request,'main/security.html',data)

def satish(request):
    satish = Satish.objects.all().order_by('-id')[0:11]

    data = {'satish':satish}
    return render(request,'main/satish.html',data)

def marketinq(request):
    marketinq = Marketinq.objects.all().order_by('-id')[0:11]

    data = {'marketinq':marketinq}
    return render(request,'main/marketinq.html',data)

def techizat(request):
    techizat = Techizat.objects.all().order_by('-id')[0:11]

    data = {'techizat':techizat}
    return render(request,'main/techizat.html',data)

def add_job(request):


    req = requests.get("https://www.offer.az")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Elan(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))

def add_it(request):
    

    req = requests.get("https://www.offer.az/category/it-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = IT(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))

def add_senaye(request):
    
    req = requests.get("https://www.offer.az/category/senaye-tikinti-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Senaye(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))

def add_tibb(request):
    
    req = requests.get("https://www.offer.az/category/tibb-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Tibb(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))

def add_security(request):
    
    req = requests.get("https://www.offer.az/category/tehlukesizlik-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Security(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))

def add_satish(request):
    
    req = requests.get("https://www.offer.az/category/satis-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Satish(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))


def add_neqliyyat(request):
    
    req = requests.get("https://www.offer.az/category/neqliyyat-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Neqliyyat(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))

def add_techizat(request):
    
    req = requests.get("https://www.offer.az/category/techizat-logistika-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Techizat(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))


def add_marketinq(request):
    
    req = requests.get("https://www.offer.az/category/marketinq-vakansiyalari/")
    soup = BeautifulSoup(req.text, 'html.parser')
    sayt = soup.find_all('div',class_ = "job-card") 

    for i in sayt:
        qisa_mezmun = ''
        link = i.find('a',class_ = 'job-card__title',href=True)
        link = link["href"]
        data = requests.get(link)
        soup = BeautifulSoup(data.content,'html.parser')
        
        title = soup.find("h1",class_ = "top-banner__title").text
        
        email = soup.find("span",id = "post_email").text
        # email.replace()
        # if '@' in email.text:
        
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text

        qisa_mezmun = soup.find("div",class_="post__excerpt")
        if qisa_mezmun is not None:
            qisa_mezmun = qisa_mezmun.text
        else :
            qisa_mezmun = ''
        
        
        sirket = soup.find("a",attrs ={"target":"_self"} ).text
        
        start_date = soup.find("span",class_ = "post__meta-value").find_parent()
        if start_date is not None:
                start_date = start_date.text
                
        end_date = soup.find("span",class_ = "post__meta-value").find_next()
        if end_date is not None:
             end_date = end_date.text
                
        city = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if city is not None:
                city = city[3].text
                
        maas = soup.find_all("span",attrs = {"class" :"post__meta-value"} )
        if maas is not None:
                maas = maas[4].text
        
        
        
        # text = soup.find("div",class_ = "post__content")
        # for x in text:
        #     text = x.find('li')
        
        try:
            text1 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[0]
            text2 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[1]
            text3 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[2]
            text4 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[3]
            text5 = soup.find("div",class_ = "post__content").find_all('ul')[0].find_all('li')[4]
            
            text_1 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[0]
            text_2 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[1]
            text_3 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[2]
            text_4 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[3]
            text_5 = soup.find("div",class_ = "post__content").find_all('ul')[1].find_all('li')[4]

            
            text1 = text1.text
            text2 = text2.text
            text3 = text3.text
            text4 = text4.text
            text5 = text5.text
            
             
            text_1 = text_1.text
            text_2 = text_2.text
            text_3 = text_3.text
            text_4 = text_4.text
            text_5 = text_5.text

        except : IndexError 
            
        apply = soup.find("a",attrs={"rel":"nofollow"})
        if apply is not None:
            apply = apply.text
        else:
            apply = 0
        
        staj = soup.find_all("li")[11].text
        age = soup.find_all("li")[12].text    
        tehsil = soup.find_all("li")[13].text  
        rejm = soup.find_all("li")[14].text
        muqavile = soup.find_all("li")[15].text
        
        if  age != '' and tehsil != '' and rejm != '' and muqavile != '' and staj != '' and email != '' and text1 != '' and title != '' and qisa_mezmun != '' and sirket != '' and city !='' and start_date != '' and end_date != ' ' and maas != '' :
            try:
                add = Marketinq(apply_link = apply,yash = age,staj = staj,tehsil=tehsil,rejm=rejm,muqavile=muqavile,
                        basliq = title,mezmun = qisa_mezmun ,sirket=sirket, seher=city,start =start_date,
                        end = end_date,maas=maas,text1 = text1,text2 = text2,text3 = text3,email=email,text4 = text4,
                        text5 = text5,text_1 = text_1,text_2 = text_2,text_3 = text_3,text_4 = text_4,text_5 = text_5)   
                add.save()
            except:TypeError
    return HttpResponseRedirect(reverse('index'))


def job_details(request, id):
  
    elan = Elan.objects.filter(id=id)
    return render(request,('main/job_details.html'),{"elan":elan})

def job_details_it(request, id):
  
    it = IT.objects.filter(id=id)
    return render(request,('main/job_details_it.html'),{"it":it})

def job_details_senaye(request, id):
  
    senaye = Senaye.objects.filter(id=id)
    return render(request,('main/job_details_senaye.html'),{"senaye":senaye})

def job_details_tibb(request, id):
  
    tibb = Tibb.objects.filter(id=id)
    return render(request,('main/job_details_tibb.html'),{"tibb":tibb})

def job_details_satish(request, id):
  
    satish = Satish.objects.filter(id=id)
    return render(request,('main/job_details_satish.html'),{"satish":satish})

def job_details_neqliyyat(request, id):
  
    neqliyyat = Neqliyyat.objects.filter(id=id)
    return render(request,('main/job_details_neqliyyat.html'),{"neqliyyat":neqliyyat})

def job_details_security(request, id):
  
    security = Security.objects.filter(id=id)
    return render(request,('main/job_details_security.html'),{"security":security})

def job_details_techizat(request, id):
  
    techizat = Techizat.objects.filter(id=id)
    return render(request,('main/job_details_techizat.html'),{"techizat":techizat})

def job_details_marketinq(request, id):
  
    marketinq = Marketinq.objects.filter(id=id)
    return render(request,('main/job_details_marketinq.html'),{"marketinq":marketinq})