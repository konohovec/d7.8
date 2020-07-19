from django.contrib import admin
from django.urls import path, reverse_lazy
from p_library import views
from p_library.views import user, AuthorEdit, AuthorList, BookEdit, FriendList, FriendUpdate, FriendEdit, BookDetailView, RegisterView, CreateUserProfile, UserProfileUpdate
from allauth.account.views import login, logout

app_name = 'p_library'  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('redactions/', views.redactions),
    path('book/create', BookEdit.as_view(), name='book_create'),
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
  	path('authors', AuthorList.as_view(), name='author_list'),    
    path('friends', FriendList.as_view(), name='friend_list'),
    path('<pk>/friend_update', FriendUpdate.as_view(), name='friend_update'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(
        template_name='account/register.html',
        success_url=reverse_lazy('p_library:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    path('user/<int:pk>', user, name='user'),
    path('update_user_profile/<pk>', UserProfileUpdate.as_view(), name='update_user_profile'),

]
