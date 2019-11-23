from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Album, Song

from django.views import generic
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# def index(request):
# 	#return HttpResponse("<h1> This is the music index page </h1>")
# 	#template = loader.get_template('music/index.html')
# 	#return HttpResponse(template.render(context,request))
	
# 	all_albums = Album.objects.all()
# 	context = {'all_albums' : all_albums}
# 	return render(request, 'music/index.html', context)

# def detail(request, album_id):
# 	#return HttpResponse("You are looking at album %s." % album_id)
	
# 	album = get_object_or_404(Album, pk=album_id)
# 	context = {'album': album}
# 	return render(request, 'music/detail.html', context)


def favourite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		context = {'album': album,
					'error_message ' : "You didn't select a choice",}
		return render(request, 'music/detail.html', context)

	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album':album})


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


