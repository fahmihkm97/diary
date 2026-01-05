from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Entry

# 1. HALAMAN UTAMA (READ & CREATE)
def index(request):
    if request.method == "POST":
        # Hanya admin yang boleh nulis
        if request.user.is_authenticated:
            content = request.POST.get('content')
            if content:
                # Judul otomatis dari 30 karakter pertama
                title = content[:30] + "..." 
                Entry.objects.create(content=content, title=title)
                return redirect('index')
            
    # Tampilkan semua catatan urut dari yang terbaru
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'diaries/index.html', {'entries': entries})

# 2. HALAMAN LOGIN
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'diaries/login.html', {'form': form})

# 3. LOGOUT
def logout_view(request):
    logout(request)
    return redirect('index')

# 4. HAPUS CATATAN (DELETE)
@login_required
def delete_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    entry.delete()
    return redirect('index')

# 5. EDIT CATATAN (UPDATE)
@login_required
def edit_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    
    if request.method == "POST":
        new_content = request.POST.get('content')
        if new_content:
            entry.content = new_content
            entry.save()
            return redirect('index')

    return render(request, 'diaries/edit.html', {'entry': entry})