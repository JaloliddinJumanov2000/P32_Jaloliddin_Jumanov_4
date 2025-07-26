from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Suggestion
from .forms import SuggestionForm
from django.db.models import Q

@login_required
def suggestion_list(request):
    query = request.GET.get('q')
    status_filter = request.GET.get('status')
    suggestions = Suggestion.objects.filter(user=request.user)
    if query:
        suggestions = suggestions.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if status_filter:
        suggestions = suggestions.filter(status=status_filter)
    return render(request, 'suggestions/suggestion_list.html', {'suggestions': suggestions})

@login_required
def suggestion_create(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            return redirect('suggestion_list')
    else:
        form = SuggestionForm()
    return render(request, 'suggestions/suggestion_form.html', {'form': form})

@login_required
def suggestion_edit(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            form.save()
            return redirect('suggestion_list')
    else:
        form = SuggestionForm(instance=suggestion)
    return render(request, 'suggestions/suggestion_form.html', {'form': form})

@login_required
def suggestion_delete(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, user=request.user)
    if request.method == 'POST':
        suggestion.delete()
        return redirect('suggestion_list')
    return render(request, 'suggestions/confirm_delete.html', {'suggestion': suggestion})
