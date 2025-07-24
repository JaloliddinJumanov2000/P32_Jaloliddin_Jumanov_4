from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Suggestion
from .forms import SuggestionForm, SuggestionSearchForm, CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Muvaffaqiyatli ro\'yxatdan o\'tdingiz!')
            return redirect('suggestion_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def suggestion_list(request):
    form = SuggestionSearchForm(request.GET)
    suggestions = Suggestion.objects.filter(user=request.user)

    if form.is_valid():
        query = form.cleaned_data.get('query')
        status = form.cleaned_data.get('status')

        if query:
            suggestions = suggestions.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

        if status:
            suggestions = suggestions.filter(status=status)

    paginator = Paginator(suggestions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_obj': page_obj,
        'suggestions': page_obj,
    }
    return render(request, 'suggestions/suggestion_list.html', context)


@login_required
def suggestion_create(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            messages.success(request, 'Fikr va taklif muvaffaqiyatli qo\'shildi!')
            return redirect('suggestion_list')
    else:
        form = SuggestionForm()
    return render(request, 'suggestions/suggestion_form.html', {
        'form': form,
        'title': 'Yangi Fikr va Taklif Qo\'shish'
    })


@login_required
def suggestion_update(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fikr va taklif muvaffaqiyatli yangilandi!')
            return redirect('suggestion_list')
    else:
        form = SuggestionForm(instance=suggestion)
    return render(request, 'suggestions/suggestion_form.html', {
        'form': form,
        'title': 'Fikr va Taklifni Tahrirlash'
    })


@login_required
def suggestion_delete(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, user=request.user)
    if request.method == 'POST':
        suggestion.delete()
        messages.success(request, 'Fikr va taklif muvaffaqiyatli o\'chirildi!')
        return redirect('suggestion_list')
    return render(request, 'suggestions/suggestion_confirm_delete.html', {
        'suggestion': suggestion
    })


@login_required
def suggestion_detail(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk, user=request.user)
    return render(request, 'suggestions/suggestion_detail.html', {
        'suggestion': suggestion
    })