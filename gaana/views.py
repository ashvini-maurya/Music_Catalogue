from django.shortcuts import render
# from django.http import HttpResponse
from gaana.models import Song
from gaana.models import Artist
from gaana.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# from gaana.models import Song
#
# Song.get_year
#
# print Song.get_year


def index(request):
    context_list = Artist.objects.all()
    context_dict = {'artists': context_list}
    return render(request, 'gaana/index.html', context_dict)


def artist(request, artist_name_slug):
    context_dict = {}
    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        context_dict['artist_name'] = artist.name
        songs = Song.objects.filter(artist=artist)
        context_dict['songs'] = songs
        context_dict['artist'] = artist
    except Artist.DoesNotExist:
        pass

    return render(request, 'gaana/artist.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'gaana/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gaana/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid Login details supplied.")
    else:
        return render(request, 'gaana/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/gaana/')