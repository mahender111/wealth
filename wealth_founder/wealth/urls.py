from django.urls import path
from .import views

urlpatterns = [
    path('error/',views.error,name ="index"),
    path('about/',views.about,name ="about"),
    path('add_listing/',views.add_listing,name ="add_listing"),
    path('add_cart/',views.add_cart,name ="add_cart"),
    path('allcourses/',views.allcourses,name ="allcourses"),
    path('blogdetail/',views.blogdetail,name ="blogdetail"),
    path('blog/',views.blog,name ="blog"),
    path('checkout/',views.checkout,name ="checkout"),
    path('component/',views.component,name ="component"),
    path('contact/',views.contact,name ="contact"),
    path('coursedetail/',views.coursedetail,name ="coursedetail"),
    path('dashboard/',views.dashboard,name ="dashboard"),
    path('detail2/',views.detail2,name ="detail2"),
    path('detail3/',views.detail3,name ="detail3"),
    path('detail4/',views.detail4,name ="detail4"),
    path('detail5/',views.detail5,name ="detail5"),
    path('detail/',views.detail,name ="detail"),
    path('faq/',views.faq,name ="faq"),
    path('find-instructor/',views.find_instructor,name ="find_instructor"),
    path('forget-password/',views.forget_password,name ="forget_password"),
    path('full-width-course-2/',views.full_width_course_2,name ="full_width_course_2"),
    path('full-width-course-3/',views.full_width_course_3,name ="full_width_course_3"),
    path('grid-with-sidebar-2/',views.grid_with_sidebar_2,name="grid_with_sidebar_2"),
    path('grid-with-sidebar-3/',views.grid_with_sidebar_3,name ="grid_with_sidebar_3"),
    path('grid-with-sidebar/',views.grid_with_sidebar,name ="grid_with_sidebar"),
    path('home-2/',views.home_2,name ="home_2"),
    path('home-3/',views.home_3,name ="home_3"),
    path('home-4/',views.home_4,name ="home_4"),
    path('home-5/',views.home_5,name ="home_5"),
    path('home-6/',views.home_6,name ="home_6"),
    path('home-7/',views.home_7,name ="home_7"),
    path('home-8/',views.home_8,name ="home_8"),
    path('home-9/',views.home_9,name ="home_9"),
    path('home-10/',views.home_10,name ="home_10"),
    path('index/',views.index,name ="index"),
    path('instructor_detail/',views.instructor_detail,name ="instructor_detail"),
    path('signin/',views.signin,name ="signin"),
    path('my_order/',views.my_order,name ="my_order"),
    path('my_profile/',views.my_profile,name ="my_profile"),
    path('new_home_1/',views.new_home_1,name ="new_home_1"),
    path('new_home_2/',views.new_home_2,name ="new_home_2"),
    path('new_home_3/',views.new_home_3,name ="new_home_3"),
    path('pricing/',views.pricing,name ="pricing"),
    path('privacy/',views.privacy,name ="privacy"),
    path('product_detail/',views.product_detail,name ="product_detail"),
    path('product_wishlist/',views.product_wishlist,name ="product_wishlist"),
    path('register/',views.register,name ="register"),
    path('reviews/',views.reviews,name ="reviews"),
    path('saved_courses/',views.saved_courses,name ="saved_courses"),
    path('settings/',views.settings,name ="settings"),
    path('shop_full_width/',views.shop_full_width,name ="shop_full_width"),
    path('shop_left_sidebar/',views.shop_left_sidebar,name ="shop_left_sidebar"),
    path('shop_order/',views.shop_order,name ="shop_order"),
    path('shop_right_sidebar/',views.shop_right_sidebar,name ="shop_right_sidebar"),
    







    
    
]

