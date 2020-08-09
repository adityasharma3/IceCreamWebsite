from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "Sharma Ice Creams Admin"
admin.site.site_title = "Sharma Ice Creams Admin Portal"
admin.site.index_title = "Welcome to Sharma Ice Creams Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls'))
]