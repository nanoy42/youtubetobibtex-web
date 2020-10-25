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

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtubetobibtex_web.settings")

application = get_wsgi_application()
