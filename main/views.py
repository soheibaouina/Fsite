from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required

@login_required
def note_home(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'main/note_home.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # create note and redirect to home
        Note.objects.create(title=title, content=content, author=request.user)
        return redirect('note_home')

    return render(request, 'main/add_note.html')


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_home')
    return render(request, 'main/edit_note.html', {'note': note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_home')
    return render(request, 'main/delete_note.html', {'note': note})


def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    return render(request, 'main/view_note.html', {'note': note})

