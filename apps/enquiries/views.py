from smtplib import SMTPException

from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
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

        # Ensure all necessary fields are present in the data
        required_fields = ["subject", "name", "email", "message"]
        for field in required_fields:
            if field not in data:
                raise KeyError(f"{field} is required")

        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )
        except SMTPException as e:
            return Response(
                {"fail": f"Email could not be sent due to SMTP error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except BadHeaderError:
            return Response(
                {"fail": "Invalid email header found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
            enquiry.save()
        except ValidationError as e:
            return Response(
                {"fail": f"Invalid data for the enquiry: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"success": "Your enquiry was successfully submitted"},
            status=status.HTTP_200_OK,
        )

    except KeyError as e:
        return Response(
            {"fail": f"Missing field: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except TypeError:
        return Response(
            {"fail": "Invalid data format."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        return Response(
            {"fail": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
