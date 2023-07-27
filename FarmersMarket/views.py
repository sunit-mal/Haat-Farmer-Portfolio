from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import product, FarmarDetail, PlaceOrder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from twilio.rest import Client
import random


def index(request):
    if request.user.is_staff:
        productData = product.objects.filter(
            userName=request.user.username).order_by('id').reverse()
    else:
        productData = product.objects.all().order_by('id').reverse()
    return render(request, 'index.html', {'img': productData})


def deleteProduct(request, id):
    data = product.objects.filter(id=id)
    data.delete()
    return HttpResponseRedirect('/')


def ProductPost(request):
    if request.user.is_authenticated:
        return render(request, 'ProductUpload.html')
    else:
        return HttpResponseRedirect('/login/')


def uploadProduct(request, name):
    if request.method == 'POST':
        img = request.FILES.get('img')
        title = request.POST.get('title')
        about = request.POST.get('details')

        saveData = product(productImg=img, ImgTitel=title,
                           about=about, userName=name)
        saveData.save()
    return HttpResponseRedirect('/')


def OrderDetails(request):
    if request.user.is_authenticated:
        PlaceOrderData = PlaceOrder.objects.filter(
            FarmerUsername=request.user.username).order_by('id').reverse()
        if FarmarDetail.objects.filter(userName=request.user.username).exists():
            userDetail = FarmarDetail.objects.get(
                userName=request.user.username)
            number = userDetail.number
        else:
            number = 'Add'
        return render(request, 'OrderDetails.html', {'yourDetails': number, 'data': PlaceOrderData})
    else:
        return HttpResponseRedirect('/login/')


def myorder(request):
    if request.user.is_authenticated:
        PlaceOrderData = PlaceOrder.objects.filter(
            orderuser=request.user.username).order_by('id').reverse()
        return render(request, 'MyOrder.html', {'data': PlaceOrderData})
    else:
        return HttpResponseRedirect('/login/')


def DeleteMyOrder(request, id):
    data = PlaceOrder.objects.filter(id=id)
    data.delete()
    return HttpResponseRedirect('/')


def orderPlace(request, id):
    # print(id)
    if request.user.is_authenticated:
        return render(request, 'placeOrder.html', {'id': id})
    else:
        return HttpResponseRedirect('/login/')


def placeOrder(request, id):
    if request.method == 'POST':
        productdata = product.objects.get(id=id)

        orderid = request.POST.get('title')
        farmerName = productdata.userName
        orderUsername = request.POST.get('username')
        orderaddress = request.POST.get('address')
        number = request.POST.get('number')
        amount = request.POST.get('amount')

        data = PlaceOrder(orderId=id, orderuser=orderUsername, orderaddress=orderaddress,
                          number=number, amount=amount, FarmerUsername=farmerName, productTitle=productdata.ImgTitel)
        data.save()

        if FarmarDetail.objects.filter(userName=productdata.userName).exists():
            farmerdata = FarmarDetail.objects.get(
                userName=productdata.userName)
            try:
                account_sid = 'ACf28401468eb08992f2e5bce883d5351a'
                auth_token = '048fefbd35f286ee17453d5c346cb88c'
                twilio_number = '+16073576039'
                target_number = '+91'+str(farmerdata.number)

                client = Client(account_sid, auth_token)
                massage = client.messages.create(
                    body=f'''You Got a Order
                    Order Titel = {productdata.ImgTitel},
                    Order Place By {orderUsername},
                    Delevery Address {orderaddress},
                    Contect Number {number},
                    Amount {amount},
                    ''',
                    from_=twilio_number,
                    to=target_number
                )
            except:
                print('SomeThing went wrong')
        return HttpResponseRedirect('/payment/')


def paymentProcess(request):
    return render(request, 'PaymentPage.html')


def detailsDelete(request, username):
    if FarmarDetail.objects.filter(userName=username).exists():
        data = FarmarDetail.objects.filter(userName=username)
        data.delete()
    return HttpResponseRedirect('/orderdetails/')

#  farmer details add and Otp verification


def farmerDetails(request):
    if request.user.is_staff:
        return render(request, 'farmerdetails.html')
    return HttpResponseRedirect('/')


def detailsAdd(request):
    if request.user.is_staff:
        if request.method == 'POST':
            username = request.user.username
            phNo = request.POST.get('phnumber')
            vill = request.POST.get('vill')
            post = request.POST.get('post')
            dist = request.POST.get('dist')
            state = request.POST.get('state')

            address = 'Village - '+vill+',Post - ' + \
                post+',District - '+dist+',State - '+state
            data = FarmarDetail(userName=username,
                                number=phNo, address=address)
            data.save()
            try:
                account_sid = 'ACf28401468eb08992f2e5bce883d5351a'
                auth_token = '048fefbd35f286ee17453d5c346cb88c'
                twilio_number = '+16073576039'
                target_number = '+91'+str(phNo)
                otpNo = random.randint(1000, 9999)

                client = Client(account_sid, auth_token)
                massage = client.messages.create(
                    body=f"Thanks For Register a user, Your Otp is {otpNo}",
                    from_=twilio_number,
                    to=target_number
                )
            except:
                print('Some Thing went wrong')
            return HttpResponseRedirect(f'/otp/{otpNo}')


def otp(request, otp):
    userDetail = FarmarDetail.objects.get(userName=request.user.username)

    if request.method == 'POST':
        otpNo = request.POST.get('OTP')
        if otp == int(otpNo):
            return HttpResponseRedirect('/')
        else:
            userDetail.delete()
            return HttpResponseRedirect('/Mydetails/')
    else:
        return render(request, 'otp.html', {'otpNo': otp})

#  farmer details add and Otp verification end

# For Authenticate


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/')


def uesr_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user = request.POST['uname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        UserType = request.POST['userType']
        if(pass1 == pass2):
            user_exist = User.objects.filter(username=user).exists()
            if user_exist:
                messages.success(
                    request, 'This username already exists. Please use a different one.')
                return HttpResponseRedirect("/signup/")
            else:
                if UserType == 'F':
                    myuser = User.objects.create_user(
                        user, email, pass1, is_staff=True)
                else:
                    myuser = User.objects.create_user(user, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                # for login after signup
                user = authenticate(request, username=user, password=pass1)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')

        else:
            messages.success(
                request, "Password Not match. Re-enter password correctly.")
            return HttpResponseRedirect("/signup/")
    else:
        return render(request, 'sign_up.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# End Authenticate process
