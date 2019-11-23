from django.urls import path
from . import views

app_name='music'
urlpatterns = [
	path('',views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
	path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

	path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),


	# path('',views.index, name='index'),
	# path('<int:album_id>/', views.detail, name='detail'),
	path('<int:pk>/favourite', views.favourite, name='favourite'),
	#path('<int:question_id>/results/', views.results, name='results'),
	#path('<int:question_id>/vote/', views.vote, name='vote'),

	]