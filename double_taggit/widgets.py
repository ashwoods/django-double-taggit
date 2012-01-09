# -*- coding: utf-8 -*-
#
#  This file is part of django-taggit-autocomplete-modified.
#
#  django-taggit-autocomplete-modified provides autocomplete functionality
#  to the tags form field of django-taggit.
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-taggit-autocomplete-modified
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-taggit-autocomplete-modified
#
#  Copyright 2011 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


from django.forms.widgets import Input
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from taggit.utils import edit_string_for_tags

from django.conf import settings

class TagAutocomplete(Input):
    input_type = 'text'

    def __init__(self, attrs={}):
        """source can be a list containing the autocomplete values or a
        string containing the url used for the XHR request.

        For available options see the autocomplete sample page::
        http://jquery.bassistance.de/autocomplete/"""

        self.attrs = {'class': 'taggit'}
        self.attrs.update(attrs)

    class Media:
        css = {
            'all': (
                'tag-it/css/jquery.tagit.css',
               'http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/flick/jquery-ui.css',
            ),

        }
        js = (
            "tag-it/js/jquery-1.7.1.min.js",
            "tag-it/js/jquery-ui.min.js",
            "tag-it/js/tag-it.js",
            "tag-it/js/django-taggit.js",

        )

    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            # value contains a list a TaggedItem instances
            # Here we retrieve a comma-delimited list of tags suitable for editing by the user.
            value = edit_string_for_tags([o.tag for o in value.select_related('tag')])
        json_view = reverse('taggit_tag_it_tag_list')
        html = super(TagAutocomplete, self).render(name, value, attrs)

        return mark_safe("\n".join([html,]))

