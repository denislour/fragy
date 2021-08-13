from flask import Blueprint, flash, redirect, request, url_for, render_template, current_app
from pallets.blueprints.contact.forms import ContactForm
from pallets.blueprints.contact.tasks import deliver_contact_email


contact = Blueprint("contact", __name__, template_folder="templates")


@contact.route("/contact", methods=["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():

        # Run background
        deliver_contact_email.submit(
            mail_from=request.form.get("email"),
            mail_to=current_app.config.get("MAIL_USERNAME"),
            message=request.form.get("message"),
        )

        flash("Thanks, expect a response shortly", "success")
        return redirect(url_for("contact.index"))

    return render_template("index.j2", form=form)
