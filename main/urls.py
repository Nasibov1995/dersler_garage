from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    
    # Details Functions
    path('job_details/<int:id>',views.job_details,name='job_details'),
    path('job_details_it/<int:id>',views.job_details_it,name='job_details_it'),
    path('job_details_senaye/<int:id>',views.job_details_senaye,name='job_details_senaye'),
    path('job_details_tibb/<int:id>',views.job_details_tibb,name='job_details_tibb'),
    path('job_details_neqliyyat/<int:id>',views.job_details_neqliyyat,name='job_details_neqliyyat'),
    path('job_details_security/<int:id>',views.job_details_security,name='job_details_security'),
    path('job_details_satish/<int:id>',views.job_details_satish,name='job_details_satish'),
    path('job_details_techizat/<int:id>',views.job_details_techizat,name='job_details_techizat'),
    path('job_details_marketinq/<int:id>',views.job_details_marketinq,name='job_details_marketinq'),
    
    # Scraping Functions
    path('add_job/',views.add_job,name='add_job'),
    path('add_it/',views.add_it,name='add_it'),
    path('add_senaye/',views.add_senaye,name='add_senaye'),
    path('add_tibb/',views.add_tibb,name='add_tibb'),
    path('add_neqliyyat/',views.add_neqliyyat,name='add_neqliyyat'),
    path('add_security/',views.add_security,name='add_security'),
    path('add_satish/',views.add_satish,name='add_satish'),
    path('add_marketinq/',views.add_marketinq,name='add_marketinq'),
    path('add_techizat/',views.add_techizat,name='add_techizat'),
    
    # Category Functions
    path('it/',views.it,name='it'),
    path('satish/',views.satish,name='satish'),
    path('senaye/',views.senaye,name='senaye'),
    path('tibb/',views.tibb,name='tibb'),
    path('neqliyyat/',views.neqliyyat,name='neqliyyat'),
    path('security/',views.security,name='security'),
    path('techizat/',views.techizat,name='techizat'),
    path('marketinq/',views.marketinq,name='marketinq'),
    
    # Login
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    
    
    path('post_job/',views.post_job, name="post_job"),
    path('post_job_it/',views.post_job_it, name="post_job_it"),
    
    path('search_results/',views.search_articles, name="search_results"),



]
