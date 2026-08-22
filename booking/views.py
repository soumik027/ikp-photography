from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Package, Booking
from .forms import BookingForm
from contact.models import SiteSettings  # <-- Import SiteSettings from contact app

def packages_view(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'booking/packages.html', context)

def book_event_view(request, package_id=None):
    initial_data = {}
    if package_id:
        pkg = get_object_or_404(Package, pk=package_id)
        initial_data['selected_package'] = pkg

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            # Dynamically fetch the client's receiving email from the database settings
            site_settings = SiteSettings.objects.first()
            recipient_email = site_settings.booking_notification_email if site_settings and site_settings.booking_notification_email else 'karmakar.indrajit02@gmail.com'
            
            # Send Email Notification to Photographer / Client
            subject = f"New Wedding Booking Inquiry: {booking.name}"
            message = (
                f"You have received a new booking inquiry!\n\n"
                f"Name: {booking.name}\n"
                f"Phone: {booking.phone}\n"
                f"Email: {booking.email}\n"
                f"Event Date: {booking.event_date}\n"
                f"Venue: {booking.venue}\n"
                f"Package: {booking.selected_package if booking.selected_package else 'None selected'}\n"
                f"Message:\n{booking.message}\n\n"
                f"Log in to Django Admin to view and confirm."
            )
            
            recipient_list = [recipient_email]  # <-- Points directly to admin setting or default email
            
            try:
                send_mail(
                    subject, 
                    message, 
                    settings.DEFAULT_FROM_EMAIL, 
                    recipient_list, 
                    fail_silently=False
                )
            except Exception as e:
                print(f"Email error: {e}")

            messages.success(request, "Your booking inquiry has been sent successfully! We will get in touch with you shortly.")
            return redirect('packages')
    else:
        form = BookingForm(initial=initial_data)

    context = {
        'form': form,
    }
    return render(request, 'booking/book_form.html', context)