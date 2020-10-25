# youtubetobibtex_web - Export bibtex from youtube videos online
# Copyright (C) 2020 Yoann Piétri

# youtubetobibtex_web is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# youtubetobibtex_web is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with youtubetobibtex_web. If not, see <https://www.gnu.org/licenses/>.

"""Views of youtubetobibtex_web
"""

from django.shortcuts import render
from django.contrib import messages

from django.conf import settings

from youtubetobibtex.client import YoutubetobibtexClient
from youtubetobibtex.errors import ChannelNotFound, UrlNotSupported, VideoNotFound

from .forms import URLForm


def home(request):
    form = URLForm(request.POST or None)
    bibtex = None
    video_id = None
    if form.is_valid():
        url = form.cleaned_data["url"]
        client = YoutubetobibtexClient(settings.YOUTUBE_API_KEY)
        try:
            video_id = client.get_video_id(url)
        except UrlNotSupported:
            messages.error(request, "The given URL was not recognized as a YouTube URL")

        if video_id:
            try:
                bibtex = client.get_bibtex(video_id)
            except ChannelNotFound:
                messages.error(request, "Error on YouTube side")
            except VideoNotFound:
                messages.error(request, "Video not found")

            # Clean the bibtex
            # May be useless in a future version of youtubetobibtex
            if bibtex:
                bibtex = bibtex[:-9]
    return render(
        request,
        "home.html",
        {"form": form, "bibtex": bibtex},
    )
