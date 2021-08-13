from flask import url_for

from pallets.core.mail import mail
from pallets.core.tests import assert_status_with_message


class TestContact(object):
    def test_contact_page(self, client):
        """ Contact page should respond with a success 200. """
        response = client.get(url_for('contact.index'))
        assert response.status_code == 200

    def test_contact_form(self, client):
        """ Contact form should redirect with a message. """
        form = {
          'email': 'foo@bar.com',
          'message': 'Test message from Pallets'
        }
        response = client.post(url_for('contact.index'), data=form, follow_redirects=True)
        assert_status_with_message(200, response, 'Thanks')

    def test_deliver_support_email(self, client):
        """ Deliver a contact email. """
        form = {
          'email': 'foo@bar.com',
          'message': 'Test message from Pallets'
        }

        with mail.record_messages() as outbox:
            client.post(url_for('contact.index'), data=form, follow_redirects=True)
            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body
