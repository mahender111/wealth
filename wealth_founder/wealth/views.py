from django.shortcuts import render,redirect
from wealth.models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth import login


# Create your views here.
def error(request):
    return render(request,"404.html")

def about(request):
    return render(request,"about-us.html")

def add_listing(request):
    return render(request,"add-listing.html")


def add_cart(request):
    return render(request,"add-to-cart.html")

def allcourses(request):
    return render(request,"all-courses.html")

def blogdetail(request):
    return render(request,"blog-detail.html")

def blog(request):
    return render(request,"blog.html")

def checkout(request):
    return render(request,"checkout.html")

def component(request):
    return render(request,"component.html")

def contact(request):
    return render(request,"contact.html")

def coursedetail(request):
    return render(request,"course-detail.html")

def dashboard(request):
    return render(request,"dashboard.html")

def detail2(request):
    return render(request,"detail-2.html")

def detail3(request):
    return render(request,"detail-3.html")

def detail4(request):
    return render(request,"detail-4.html")

def detail5(request):
    return render(request,"detail-5.html")

def detail(request):
    return render(request,"detail.html")

def faq(request):
    return render(request,"faq.html")

def find_instructor(request):
    return render(request,"find-instructor.html")

def forget_password(request):
    return render(request,"forget-password.html")

def full_width_course_2(request):
    return render(request,"full-width-course-2.html")

def full_width_course_3(request):
    return render(request,"full-width-course-3.html")

def grid_with_sidebar_2(request):
    return render(request,"grid-with-sidebar-2.html")

def grid_with_sidebar_3(request):
    return render(request,"grid-with-sidebar-3.html")

def grid_with_sidebar(request):
    return render(request,"grid-with-sidebar.html")

def home_2(request):
    return render(request,"home-2.html")

def home_3(request):
    return render(request,"home-3.html")

def home_4(request):
    return render(request,"home-4.html")

def home_5(request):
    return render(request,"home-5.html")

def home_6(request):
    return render(request,"home-6.html")

def home_7(request):
    return render(request,"home-7.html")

def home_8(request):
    return render(request,"home-8.html")

def home_9(request):
    return render(request,"home-9.html")

def home_10(request):
    return render(request,"home-10.html")


def index(request):
    return render(request,"index.html")


def instructor_detail(request):
    return render(request,"instructor-detail.html")

def signin(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/index")
        # A backend authenticated the credentials
        else:
            print("hf")
            return render(request,"login.html",{'flag':1})
        # No backend authenticated the credentials
        # print(username)
    return render(request,"login.html")

# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
             

def my_order(request):
    return render(request,"my-order.html")

def my_profile(request):
    return render(request,"my-profile.html")

def new_home_1(request):
    return render(request,"new-home-1.html")

def new_home_2(request):
    return render(request,"new-home-2.html")

def new_home_3(request):
    return render(request,"new-home-3.html")

def pricing(request):
    return render(request,"pricing.html")

def privacy(request):
    return render(request,"privacy.html")

def product_detail(request):
    return render(request,"product-detail.html")


def product_wishlist(request):
    return render(request,"product-wishlist.html")

def register(request):
    if request.method =='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username =request.POST.get('username') 
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        country = request.POST.get("country")
        state = request.POST.get("state")
        dob = request.POST.get('dob')
        # city = request.POST.get('city')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        print(username)
        if password != confirm_password:
            print("password not match")
            return render(request,"register.html",{'flag':1} )
        obj = Profile.objects.create_user(firstname=firstname,lastname = lastname,username= username,email = email, mobile = mobile, country = country,state = state,dob= dob,password = password)
        obj.save()
        return redirect("/signin")
    return render(request,"register.html")

def reviews(request):
    return render(request,"reviews.html")

def settings(request):
    return render(request,"settings.html")

def shop_full_width(request):
    return render(request,"shop-full-width.html")


def saved_courses(request):
    return render(request,"saved-courses.html")



def shop_left_sidebar(request):
    return render(request,"shop-left-sidebar.html")

def shop_order(request):
    return render(request,"shop-order.html")

def shop_right_sidebar(request):
    return render(request,"shop-right-sidebar.html")









