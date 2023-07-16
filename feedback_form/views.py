from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action

from feedback_form.models import FeedbackForm
from feedback_form.serializers import FeedbackFormSerializer
from teya_chem_backend.settings import EMAIL_HOST_USER


def generate_email_object(title='', message='') -> EmailMessage:
    email = EmailMessage(
        title,
        message,
        EMAIL_HOST_USER,
        [EMAIL_HOST_USER]
    )

    return email


class FeedbackFormViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackFormSerializer

    queryset = FeedbackForm.objects.all()

    @action(detail=False, methods=['POST'])
    def send_to_email(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer_data = serializer.validated_data

        sender_name = serializer.validated_data.get('full_name', 'Аноним')
        date = timezone.now()

        message = f'''
            Имя: {sender_name}
            Email: {serializer_data.get('email', '—')}
            Номер телефона: {serializer_data.get('phone', '—')}
            Комментарий: {serializer_data.get('comment', '—')}
        '''

        email_object = generate_email_object(
            title=f'Форма обратной связи от "{sender_name}" ({date})',
            message=message
        )

        attachment_file = serializer_data.get('attachment_file', None)

        if attachment_file is not None:
            email_object.attach(attachment_file.name, attachment_file.read(), attachment_file.content_type)

        try:
            email_object.send()
            return HttpResponse("OK")
        except:
            return HttpResponseBadRequest('Failed to send the form')
