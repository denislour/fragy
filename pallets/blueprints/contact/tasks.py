from pallets.core.mail import send_template_message
from pallets.core.extensions import executor


@executor.job
def deliver_contact_email(mail_from, mail_to, message):
    """
        Send a contact e-mail.

        :param mail_from: E-mail address of the visitor
        :param message: E-mail message
        :param mail_to: E-mail message of the receiver
        :return: None
    """
    ctx = {'email': mail_from, 'message': message}

    send_template_message(
        subject='[Pallets] Contact',
        sender=mail_from,
        recipients=[mail_to],
        reply_to=mail_from,
        template='mail/index', ctx=ctx
    )

    return None
