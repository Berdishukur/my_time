from  django.urls import path
from  .views import  index_page,soat_page

urlpatterns=[
    path('',index_page,name='index'),
    path('soat/',soat_page,name='soat'),
]