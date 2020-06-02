from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

User = get_user_model()

def email_client(request):
    username = request.data.get('username')
    client = User.objects.get(username=username)
    # msg_html = render_to_string('templates/account/email/feedback.txt', {'client': client})
    template_email_text = ''
    return send_mail('Lelander work samples', template_email_text, 'zkaragoyshin1@gmail.com', [f'{client.email}'],  fail_silently=False)