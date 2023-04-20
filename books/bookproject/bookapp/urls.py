from . import views
from django.urls import path
app_name='bookapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('books/<int:book_id>/', views.brief,name="brief"),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]