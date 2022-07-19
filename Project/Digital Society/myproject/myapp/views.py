from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from .utils import sendmail
# Create your views here.


def home(request):
    if "email" in request.session:
        print("inside if")
        data = user.objects.get(email=request.session["email"])
        print(request.session["email"])

        print(data.role)
        if data.role == "Chairman":
            cid = chairman.objects.get(user_id=data)
            context = {
                "data": data,
                "cid": cid
            }
            print(cid.pic.url)
            return render(request, "myapp/index.html", context)

        elif data.role == "Member":
            mid = member.objects.get(member_id=data)
            context = {"data": data, "mid": mid}
            return render(request, "myapp/member_index.html", context)

        else:
            return render(request, "myapp/login.html")

    else:
        return render(request, "myapp/login.html")


@csrf_exempt
def login(request):
    if "email" in request.session:
        return redirect("home")
    else:

        if request.POST:
            v_email = request.POST['email']
            v_password = request.POST['password']
            try:

                data = user.objects.get(email=v_email)
                print(data.email)
                print(data.password)
                print(data.role)

                if data.password == v_password and data.role == "Chairman":
                    print("----------------->1")
                    cid = chairman.objects.get(user_id=data)
                    request.session['email'] = v_email
                    # print(f"---------------->firstname:{cid.firstname}")
                    # print(f"---------------->lastname:{cid.lastname}")
                    # print(f"----------------->role:{data.role}")
                    context = {"data": data, "cid": cid}
                    return render(request, "myapp/index.html", context)

                elif data.password == v_password and data.role == "Member":
                    print("----------------->2")
                    print(f"------------------>{data}")
                    if data.is_verfied:
                        print("---------------->3")
                        mid = member.objects.get(member_id=data)
                        request.session['email'] = v_email
                        context = {"data": data, "mid": mid}
                        return render(request, "myapp/member_index.html", context)
                    else:
                        print("-------------------->4")
                        context = {"data":data}
                        return render(request, "myapp/OTP.html",context)

                else:
                    context = {
                        "msg": "Invalid Creditionals!!"
                    }
                return render(request, "myapp/login.html", context)

            except Exception as e:

                context = {"msg": "Invalid Email address"}
                print(f"------------------------------------->{e}")
                return render(request, "myapp/login.html", context)
        else:

            return render(request, "myapp/login.html")


def register(request):
    return HttpResponse("<h1> register page</h1>")


def profile(request):
    if "email" in request.session:
        data = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=data)
        if cid:
            context = {
                "data": data,
                "cid": cid
            }
            return render(request, "myapp/profile.html", context)
        else:
            return render(request, "myapp/login.html")
    else:
        return render(request, "myapp/login.html")


def logout(request):
    if "email" in request.session:
        del request.session['email']

        return render(request, "myapp/login.html")

    else:
        return render(request, "myapp/login.html")


def changepassword(request):
    if "email" in request.session:
        data = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=data)
        if request.POST:
            v_email = request.POST["email"]
            c_password = request.POST["password"]
            n_password = request.POST["newpassword"]
            data = user.objects.get(email=v_email)
            if data.password == c_password:
                data.password = n_password
                data.save()
                context = {
                    "smsg": "Password Successfully changed",
                    "cid": cid
                }
                return render(request, "myapp/profile.html", context)
            else:
                context = {
                    "emsg": "password does not match",
                    "cid": cid
                }
                return render(request, "myapp/profile.html", context)
        else:
            return render(request, "myapp/login.html")


def editprofile(request):
    if "email" in request.session:
        data = user.objects.get(email=request.session["email"])
        if request.POST:
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            contact = request.POST['contact']
            block_no = request.POST['blockno']
            house_no = request.POST['house_no']
            pic = request.FILES['pic']
            aboutme = request.POST['aboutme']
            cid = chairman.objects.get(user_id=data)
            if cid:
                cid.firstname = firstname
                cid.lastname = lastname
                cid.contact = contact
                cid.block_no = block_no
                cid.house_no = house_no
                cid.aboutme = aboutme
                cid.save()
                if "pic" in request.FILES:
                    cid.pic = pic
                    cid.save()
                context = {
                    "s_msg": "data successfully updated",
                    "cid": cid,
                    "data": data
                }
                return render(request, "myapp/profile.html", context)
            else:
                context = {
                    "e_msg": "Error while updating data",
                    "cid": cid
                }
            return render(request, "myapp/profile.html", context)


def add_notice(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=uid)

        if request.POST:
            # fetch data
            N_title = request.POST["title"]
            N_content = request.POST["content"]
            img = request.FILES.get('image')
            video = request.FILES.get('video')

            # store data
            data = notice.objects.create(user_id=chairman.objects.get(firstname=cid.firstname),
                                         notice_title=N_title,
                                         notice_content=N_content,
                                         img=img,
                                         video=video)
            # check if data stored in database or not
            if data:
                messages.success(request, "Notice Added Successfully")
                context = {"notice_msg": "notice added successfully",
                           "cid": cid,
                           "uid": uid,
                           }
                return render(request, "myapp/Add-notice.html", context)
            else:
                messages.error(request, "Error While Adding Notice!")
                context = {"notice_error_msg": "Error While Adding Notice!",
                           "cid": cid,
                           "uid": uid}
                return render(request, "myapp/Add-notice.html", context)
        else:
            context = {"cid": cid, "uid": uid}
            return render(request, "myapp/Add-notice.html", context)
    else:

        return render(request, "myapp/login.html")


def viewnotice(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=uid)
        show_notice = notice.objects.all()
        context = {"uid": uid,
                   "cid": cid,
                   "show_notice": show_notice}
        return render(request, "myapp/View-notice.html", context)
    else:
        return render(request, "myapp/login.html")


def add_member(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=uid)
        context = {"uid": uid, "cid": cid}
        if request.POST:
            email = request.POST['email']
            firstname=request.POST['fname']

            data = member.objects.create(firstname=request.POST.get('fname'),
                                         lastname=request.POST['lname'],
                                         DOB=request.POST['DOB'],
                                         total_member=request.POST['member'],
                                         number_of_vehicle=request.POST['vehicle'],
                                         gender=request.POST['gender'],
                                         phone=request.POST['phone'],
                                         work_info=request.POST['workinfo'],
                                         Email=request.POST['email'])
            if "photo" in request.FILES:
                data.photo = request.FILES.get('photo')
                data.save()

            password = get_random_string()
            data1 = user.objects.create(
                email=email, password=password, role="Member")
            if data1:
                data.member_id = user.objects.get(email=email)
                data.save()
                subject="Digital Society Authnitication"
                sendmail(subject,"Email_otp",email,{"password":password,"firstname":firstname})
                # content = "your one time password for Digital Society is: "+password
                # from_email = settings.EMAIL_HOST_USER
                # to_email = [email]
                # send_mail("Digital Society password",
                #           content, from_email, to_email)
                messages.success(request, 'SuccessFully Add details')
                return render(request, "myapp/Add-member.html", context)
            else:
                messages.error(request, 'Error While Adding Member')
            return render(request, "myapp/Add-member.html", context)
        else:
            return render(request, "myapp/Add-member.html", context)


def notfound(request):
    return render(request, "myapp/page404.html")


def all_notice(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=uid)
        nid = notice.objects.all()
        context = {"uid": uid,
                   "cid": cid,
                   "nid": nid}
        return render(request, "myapp/All Notice.html", context)
    else:
        return render(request, "myapp/login.html")


def all_member(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session["email"])
        cid = chairman.objects.get(user_id=uid)
        mid = member.objects.all()
        context = {"uid": uid,
                   "cid": cid,
                   "mid": mid}
        return render(request, "myapp/All Member.html", context)
    else:
        return render(request, "myapp/login.html")


def demo(request):
    return render(request, "myapp/OTP.html")


def update_OTP(request):
        if request.POST:
            email= request.POST["email"]
            cpass= request.POST["cpass"]
            new_pass= request.POST["npass1"]
            re_pass= request.POST["npass2"]
            uid= user.objects.get(email=email)
            if email==uid.email:
                print("------------------------>UO1")
                if cpass==uid.password:
                    print("------------------------>UO2")
                    if new_pass==re_pass:
                        print("------------------------>UO3")
                        uid.password=new_pass
                        uid.is_verfied=True
                        uid.is_active=True
                        uid.save()
                        return render(request, "myapp/login.html")
                    else:
                        context={"emsg": "new password and confirm password are not same"}
                        return render(request, "myapp/OTP.html",context)
                else:
                    context={"emsg":"Invalid OTP password"}
                    return render(request,'myapp/OTP.html',context)
            else:
                context={"emsg":"Invalid Email id"}
                return render(request, 'myapp/OTP.html',context)         


def profileM(request):
    if "email" in request.session:
        data= user.objects.get(email=request.session["email"])
        mid= member.objects.get(member_id=data)
        context= {"data": data, "mid": mid}
        return render(request, "myapp/Member_profile.html", context)                


def view_notice_M(request):
    if "email" in request.session:
        uid= user.objects.get(email=request.session["email"])
        mid= member.objects.get(member_id=uid)
        nid=notice.objects.all()
        context= {"uid":uid,"mid":mid,"nid":nid}
        return render (request, "myapp/M_All_Notice.html",context)
    else:
        return render(request, "myapp/login.html")


def update_password_M(request):
    if "email" in request.session:
        uid= user.objects.get(email=request.session["email"])
        mid=member.objects.get(member_id=uid)
        context= {"uid":uid,"mid":mid}
        if request.POST:
            cpass= request.POST['password']
            npass= request.POST['newpassword']

            if uid.password==cpass:
                if cpass!=npass:
                    uid.password=npass
                    uid.save()
                else:
                    context = {"msg":"new password and  old password not be same"}
            else:
                context={"msg":"Invalid credentials!!!!"}
                
        return render(request, "myapp/Member-profile.html", context)
    else:
        return render(request, "myapp/login.html")