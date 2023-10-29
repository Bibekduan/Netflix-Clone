from django.urls import path
from .import views
from .views import Home,profileList,ProfileCreate,MovisList,MoviesDetail,PlayMovie
# from .views import index
urlpatterns = [
    path('',Home.as_view(),name="Home"),
    path('profiles/',profileList.as_view(),name="profile-list"),
    path('profiles/create/',ProfileCreate.as_view(),name="profile-creaet"),
    path('watch/<str:profile_id>/',MovisList.as_view(),name="movie-list"),
    path('watch/detail/<str:movie_id>/',MoviesDetail.as_view(),name="movie-detail"),
    path('movie/play/<str:movie_id>/',PlayMovie.as_view(),name="play-movie"),


]
