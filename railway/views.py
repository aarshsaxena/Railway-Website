from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from bookings.models import Tickets
from information.models import Station, Train, Website
websitedata=Website.objects.all()

for z in websitedata: #Dynamic title that can be changed through admin side of site.
    title=z.title

# functions defined here for urls.

def index(request):
    if request.user.is_authenticated: #User authentication
        return HttpResponseRedirect('/home/')
    else:
        data={
            'title':title
        }
        return render(request, 'index.html',data)


def homepage(request):
    if request.user.is_authenticated:
        data={
            'title':title
        }
        return render(request, 'home.html',data)
    else:
        return HttpResponseRedirect('/')


def aboutus(request):
    data={
            'title':title
        }
    return render(request, 'about.html',data)


def book(request):
    if request.user.is_authenticated:
        stationdata = Station.objects.all() #Fetching list of stations
        if request.method == "POST": # this will only be executed when station is entered on frontend.
            sour = request.POST.get('source')
            desti = request.POST.get('destination')
            date = request.POST.get('date')

            traindata = Train.objects.all().filter(source=sour, destination=desti) # Fetching train data between source and destination.
            data = {
                'traindata': traindata,
                'stationdata': stationdata,
                'date': date,
                'check': True,
                'title':title
            }

            return render(request, 'book.html', data)
        data = {
            'stationdata': stationdata,
            'title':title
        }
        return render(request, 'book.html', data)

    else:
        return HttpResponseRedirect('/')


def details(request):

    if request.user.is_authenticated: 
        if request.method == "POST":
            number = request.POST.get('trainno')
            name = request.POST.get('trainname')
            classs = request.POST.get('classs')
            date = request.POST.get('date')
            traindata = Train.objects.filter(trainno=number)
            fare = 0
            if classs == 'EC': # to fetch price of entered class on site.
                for i in traindata:
                    fare = i.ec
            else:
                for i in traindata:
                    fare = i.cc

            data = {
                'traindata': traindata,
                'fare': fare,
                'date': date,
                'classs': classs,
                'title':title
            }

            return render(request, "details.html", data)
        else:
            return HttpResponseRedirect('/book-ticket/')
    else:
        return HttpResponseRedirect('/')
    # Aarsh Saxena (21bec001)

def register(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    else:
        if request.method == "POST": # To register users.
            try:
                fname = request.POST.get('fname')
                lname = request.POST.get('lname')
                city = request.POST.get('city')
                state = request.POST.get('state')
                country = request.POST.get('country')
                pin = request.POST.get('pin')
                mob = request.POST.get('mob')
                email = request.POST.get('email')
                cemail = request.POST.get('cemail')
                passwd = request.POST.get('passwd')
                cpasswd = request.POST.get('cpasswd')

                address = str(city)+" "+str(state)+" "+str(country)

                if email != cemail:
                    mstr1 = 'Email and Confirm Email are not same.'
                    messages.error(request, mstr1)
                    return HttpResponseRedirect('/register/')
                if passwd != passwd:
                    mstr2 = 'Email and Confirm Email are not same.'
                    messages.error(request, mstr2)
                    return HttpResponseRedirect('/register/')

                user = User.objects.create_user(username=cemail, email=cemail, password=cpasswd)
                user.first_name = fname
                user.last_name = lname
                user.save()
                mstr3 = 'You account has been successfully created.'
                messages.success(request, mstr3)
                return HttpResponseRedirect("/login/")

            except Exception as e:
                messages.error(request, e)
                return HttpResponseRedirect('/register/')
        
        data={
            'title':title
        }
        return render(request, "register.html",data)


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    else:
        if request.method == "POST":
            email1 = request.POST['email1']
            passwd1 = request.POST['passwd1']

            user = authenticate(request, username=email1, password=passwd1)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                messages.error(request, "User not found.")
                return HttpResponseRedirect("/login/")

        data={
            'title':title
        }
        return render(request, 'login.html',data)


def payment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            emaill = request.user.email
            trainno = request.POST.get('trainno')
            classs = request.POST.get('classs')
            date = request.POST.get('date')
            fare = int(request.POST.get('fare'))

            l1 = []  # contains the details of all passengers in a list form.
            passengers = 0
            p1 = request.POST.get(
                'p1_name')+" "+str(request.POST.get('p1_age'))+" "+request.POST.get('p1_gender')
            l1.append(p1)

            p2 = request.POST.get(
                'p2_name')+" "+str(request.POST.get('p2_age'))+" "+request.POST.get('p2_gender')
            l1.append(p2)

            p3 = request.POST.get(
                'p3_name')+" "+str(request.POST.get('p3_age'))+" "+request.POST.get('p3_gender')
            l1.append(p3)

            p4 = request.POST.get(
                'p4_name')+" "+str(request.POST.get('p4_age'))+" "+request.POST.get('p4_gender')
            l1.append(p4)

            p5 = request.POST.get(
                'p5_name')+" "+str(request.POST.get('p5_age'))+" "+request.POST.get('p5_gender')
            l1.append(p5)

            l1 = set(l1)
            l1.remove('  NULL')
            l1 = list(l1)
            passno = len(l1)  # number of passengers

            amt = fare*passno  # total amount to paid is stored in amt.
            l1.append(amt)
            traindata = Train.objects.filter(trainno=trainno)

            data = {
                'trainno': trainno,
                'classs': classs,
                'date': date,
                'amt': amt,
                'passno': passno,
                'l1': l1
            }

        return render(request, "payment.html", data)
    else:
        return HttpResponseRedirect('/')
    

def confirmtkt(request):
    emailid=request.user.email
    trainno = request.POST.get('trainno')
    classs=request.POST.get('classs')
    amt=request.POST.get('amt')
    doj=request.POST.get('doj')
    passno=request.POST.get('passno')
    list1=request.POST.get('list1')
    traindata = Train.objects.filter(trainno=trainno)
    for i in traindata:
        trainname=i.trainname
        src=i.source
        des=i.destination
        kms=i.kms
    tkt=Tickets.objects.create(email=emailid,trainno=trainno,trainname=trainname,classs=classs,amt=amt,source=src,destination=des,kms=kms,doj=doj,passno=passno,list1=list1)
    tkt.save()
    re=Tickets.objects.filter(email=emailid,trainno=trainno,doj=doj,passno=passno,list1=list1)
    print(re)
    for i in re:
        pnr=i.pnr
        transactionid=i.transactionid
        data={
            'pnr':pnr,
            'transactionid':transactionid
        }
    return render(request,"Confirmation.html",data)
    
def booking_history(request):
    if request.user.is_authenticated:
        emailid=request.user.email
        records=Tickets.objects.all().filter(email=emailid)
        data={
            'records':records,
            'title':title
        }
        return render(request,'booking_history.html',data)
    else:
        return HttpResponseRedirect('/')

def cancel(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            p=request.POST.get('pnr')
            rec=Tickets.objects.filter(pnr=p)
            rec.delete()
            return HttpResponseRedirect('/booking-history/')
    else:
        return HttpResponseRedirect('/booking-history/')

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


# Aarsh Saxena (21bec001)