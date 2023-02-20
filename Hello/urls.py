

from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Aashutosh Ice Cream Admin"
admin.site.site_title = "Aashutosh Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Aashutosh Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))

]
