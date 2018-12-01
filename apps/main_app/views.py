from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# import stripe

# Create your views here.
def index(request):
    return render(request, "main_app/index.html")

def register(request):
    errors = User.objects.registrationValidate(request.POST)
    if len(errors):
        for key in errors:
            messages.error(request, errors[key])
        return redirect('/')
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    final_hashed_pw = hashed_pw.decode('utf-8')
    user = User.objects.create(user_level = 1, first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = final_hashed_pw)
    request.session['user_id'] = user.id
    request.session['logged'] = True
    return redirect('/home')

def login(request):
    errors = User.objects.loginValidate(request.POST)
    if len(errors):
        for key in errors:
            messages.error(request, errors[key])
        return redirect('/')
    request.session['user_id'] = User.objects.get(email = request.POST['email']).id
    request.session['logged'] = True
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')

def home(request):
    if request.session['logged'] != True:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level == 9:
        return redirect('/admin')
    return render(request, "main_app/home.html")

def user(request, id):
    return HttpResponse('welcome to the user show page!')

# DISPLAYS A CREATE TRIP PAGE BASED ON THE TRAIL ADDED
def addtrip(request, id):
    return render(request, "main_app/addtrip.html", {'trail': id})

# CREATING A TRIP DEPENDING ON OVERNIGHT OR NOT
def process(request):
    api_id = request.POST['trail_id']
    user = User.objects.get(id = request.session['user_id'])
    if request.POST['overnight'] == '1':
        errors = Trip.objects.overnightValidate(request.POST)
        if len(errors):
            for key in errors:
                messages.error(request, errors[key])
            return redirect('/trail/'+api_id+'/addtrip')
        trip = Trip.objects.create(planner = user, comment = request.POST['description'], trail_api_id = api_id, start_date = request.POST['start'], end_date = request.POST['end'], overnight = 1)
        trip.crew.add(user)
    else:
        errors = Trip.objects.tripValidate(request.POST)
        if len(errors):
            for key in errors:
                messages.error(request, errors[key])
            return redirect('/trail/'+api_id+'/addtrip')
        trip = Trip.objects.create(planner = user, comment = request.POST['description'], trail_api_id = api_id, start_date = request.POST['start'], end_date = request.POST['start'], overnight = 0)
        trip.crew.add(user)
    return redirect('/home')

def addpic(request, id):
    if request.method == 'POST' and request.FILES['picture']:
        picture = request.FILES['picture']
        # fs = FileSystemStorage()
        # filename = fs.save(picture.name, picture)
        # uploaded_file_url = fs.url(filename)
        Picture.objects.create(uploader = User.objects.get(id=request.session['user_id']),trippic = Trip.objects.get(id=id) , picture = picture, caption = request.POST['caption'])
        return redirect('/trip/'+str(id))
    else:
        return redirect('/trip/'+str(id))
    return redirect('/home')

def addreview(request, id):
    return HttpResponse('welcome to the addreview page for trips')

def trail(request, id):
    return HttpResponse('welcome to the show page for trails')

def jointrip(request, id):
    Trip.objects.get(id=id).crew.add(User.objects.get(id = request.session['user_id']))
    return redirect('/mytrip')

def tripedit(request, id):
    return HttpResponse('welcome to the page for editing trips')

def trip(request):
    context = {
        'trips' : Trip.objects.exclude(crew = User.objects.get(id=request.session['user_id']))
    }
    return render(request, "main_app/alltrip.html", context)

def mytrip(request):
    context = {
        'user_id' : request.session['user_id'],
        'mytrips' : Trip.objects.filter(crew = User.objects.get(id=request.session['user_id']))
    }
    return render(request, "main_app/mytrip.html", context)

def tripshow(request,id):
    context = {
        'trip' : Trip.objects.get(id = id),
        'crews': Trip.objects.get(id = id).crew.all(),
        'pictures' : Picture.objects.filter(trippic = Trip.objects.get(id=id))
    }
    return render(request, 'main_app/tripdetail.html', context)

def processdono(request):
    stripe.api_key = "sk_test_5yc2EkJimuUtEz32vQTT7zNn"

    charge = stripe.Charge.create(

    )
    return HttpResponse('processing donos')

def admin(request):
    return render(request, "main_app/admin.html")

def emergency(request):
    return HttpResponse('welcome to the emergency contact page')

def deleteuser(request):
    return HttpResponse('here is the page where you can delete users')

def donation(request):
    return render(request, "main_app/donation.html")


# // TESTING OUT OAUTH ROUTES //
def oauth(request):
    return render(request, "main_app/oauthpractice.html")

def oauthprocess(request):
    return render(request, "main_app/oatuhpractice.html")