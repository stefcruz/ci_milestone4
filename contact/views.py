from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ A view to enable user to submit contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request sent '
                                      'successfully, thank you!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Contact request not sent, '
                                    'please ensure the form is valid.')
    else:
        form = ContactForm

    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
