from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#from django.contrib.auth import views as auth_views
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("accounts/", include("django.contrib.auth.urls")),
    path('', include('pages.urls')),
    path('loans/', include('loans.urls')),
    path('', include('userprofile.urls')),
    # path('notifications/', include('notification.urls')),

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Change Password
    #path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html', success_url = '/'), name='change_password'),
]

# if settings.DEBUG: # new
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Shylock Services MVP"
admin.site.site_title = "Admin"
admin.site.index_title = "Shylock Services MVP"