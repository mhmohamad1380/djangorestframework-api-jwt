from celery import shared_task
from templated_mail.mail import BaseEmailMessage

@shared_task
def send_mail_for_new_posts(post_title,emails):
    
    message = BaseEmailMessage(
        template_name="emails/new_product.html",
        context = {
            "product_title":post_title
        }
    )
    message.attach_file("./templates/emails/21.png")
    message.send(emails)