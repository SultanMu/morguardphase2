from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('list-folders/',views.list_s3_folders,name='list-drive'), # should check if a file_name is in our database before processing it, only read the file names which are new
    path('expand-folder/',views.expand_s3_folder,name='expand-drive'),
    path('process-files/', views.index_files, name='index-files'),
    path('get-files/', views.get_file_data, name='get-files'),
    path('register/',views.RegisterView.as_view(),name='register-user'),
    path('login/',views.LoginView.as_view(),name='login-user'),
    path('logout',views.LogoutView.as_view(),name='logout-user')
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth')
    # path('list-drive-time-flag',views.list_s3_folders,name='list-drive-time-flag'),
    # path('list-drive-time-flag-sorted',views.list_s3_folders,name='list-drive-time-flag-sorted'),
    # path('file-edit',views.LogoutView.as_view(),name='file-edit') # this will require folder name and file name to pull data from database to display yhe form
    # path('save',views.LogoutView.as_view(),name='save') #save the edited file in database
    # path('push_to_refined_data',views.LogoutView.as_view(),name='push_to_refined_data') # either push one file at a time or all in folder or all in the entire directory


]