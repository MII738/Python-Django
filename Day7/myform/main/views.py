from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm


@login_required
def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('success')  # or some other page
    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
