from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from unicodedata import category

from Suggestion.forms import SuggestionForms
from Suggestion.models import Suggestion


@login_required
def home(request):
    search_published_suggestion = request.GET.get('search_published_blog')
    type_filter = request.GET.get('category')

    suggestion = SuggestionForms.objects.filter(published=True)

    if search_published_suggestion:
        suggestion = suggestion.filter(
            Q(title__icontains=search_published_suggestion) |
            Q(content__icontains=search_published_suggestion)
        )

    if type_filter:
        suggestion = suggestion.filter(type=type_filter)

    context = {
        "suggestion": suggestion,
        "active_type": type_filter,
    }

    return render(request, 'Suggestion/home.html', context)


def tag_filter(request, tag_name):
    blog = Suggestion.objects.get(name=tag_name)
    return render(request, 'Suggestion/home.html', context={'Suggestion': blog})
