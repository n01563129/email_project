from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.mail.backends.smtp import EmailBackend
from .forms import EmailForm
from .models import Email

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            # Get sender credentials
            sender_email = form.cleaned_data['sender_email']
            sender_password = form.cleaned_data['sender_password']

            # Use provided credentials for email backend
            email_backend = EmailBackend(
                host='smtp.gmail.com',
                port=587,
                username=sender_email,
                password=sender_password,
                use_tls=True
            )

            # Email sending logic
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            receiver = form.cleaned_data['receiver'].split(',')  # Assuming multiple receivers are separated by comma
            cc = form.cleaned_data['cc'].split(',') if form.cleaned_data['cc'] else []
            attachment = request.FILES.get('attachment')

            # Create the email
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=sender_email,
                to=receiver,
                cc=cc,
                connection=email_backend
            )

            # Attach the file if present
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            # Send the email
            email.send()

            # Handle success 
            return render(request, 'email_app/email_sent.html')

    else:
        form = EmailForm()

    return render(request, 'email_app/email_form.html', {'form': form})

# Simple view to handle success message
def email_sent(request):
    return render(request, 'email_app/email_sent.html')
