from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Package, Booking
from .forms import BookingForm
from contact.models import SiteSettings  

def packages_view(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'booking/packages.html', context)

def book_event_view(request, package_id=None):
    pkg = None
    if package_id:
        pkg = get_object_or_404(Package, pk=package_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        # --- ADD THESE DEBUG PRINTS ---
        print("--- FORM SUBMISSION ATTEMPT ---")
        if form.is_valid():
            print("Form is VALID. Proceeding to save and email...")
            booking = form.save(commit=False)
            if pkg:
                booking.selected_package = pkg
            booking.save()
            print("Booking saved successfully to database!")
            
            recipient_email = 'soumikmaity54555@gmail.com'
            try:
                site_settings = SiteSettings.objects.first()
                if site_settings and site_settings.booking_notification_email:
                    recipient_email = site_settings.booking_notification_email
            except Exception as e:
                print(f"SiteSettings fetch error: {e}")
            
            print(f"Attempting to send mail to: {recipient_email}")
            try:
                send_mail(
                    subject="Test Subject", 
                    message="Test Body", 
                    from_email=settings.DEFAULT_FROM_EMAIL, 
                    recipient_list=[recipient_email], 
                    fail_silently=False
                )
                print("Mail sent function executed without crashing!")
            except Exception as mail_err:
                print(f"EXACT EMAIL ERROR: {mail_err}")

            messages.success(request, "Your booking inquiry has been sent successfully!")
            return redirect('packages')
        else:
            # THIS WILL PRINT WHY THE FORM FAILED
            print(f"Form is INVALID! Errors: {form.errors}")
            
    else:
        initial_data = {'selected_package': pkg} if pkg else {}
        form = BookingForm(initial=initial_data)

    context = {
        'form': form,
        'package': pkg,
    }
    return render(request, 'booking/book_form.html', context)