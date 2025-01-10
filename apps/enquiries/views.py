from django.core.mail import send_mail
from real_estate.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def send_enquiry_email_api_view(request):
    try:
        data = request.data
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=True,
        )

        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "your enquiry was successfully submitted"}, status=status.HTTP_200_OK)
    except:
        return Response({"fail": "enquiry was not sent please try again"}, status=status.HTTP_400_BAD_REQUEST)
