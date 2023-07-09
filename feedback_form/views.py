from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import timezone
from rest_framework import viewsets

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

    def create(self, request, *args, **kwargs):
        data: {str, any} = request.data

        sender_name = data.get('full_name', 'Аноним')
        date = timezone.now()

        message = f'''
            Имя: {sender_name}
            Email: {data.get('email', 'Почта отсутствует')}
            Номер телефона: {data.get('phone', 'Номер телефона отсутствует')}
            Комментарий: {data.get('comment', 'Комментарий отсутствует')}
        '''

        email_object = generate_email_object(
            title=f'Форма обратной связи от "{sender_name}" ({date})',
            message=message
        )

        try:
            attachment_file = request.FILES['attachment_file']
            email_object.attach(attachment_file.name, attachment_file.read(), attachment_file.content_type)
        except:
            print('No file attached')

        try:
            email_object.send(fail_silently=True)
            return HttpResponse("OK")
        except:
            return HttpResponseBadRequest('Failed to retrieve the form')
