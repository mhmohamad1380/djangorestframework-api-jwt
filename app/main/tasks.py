from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_mail_for_new_posts(post_title,emails):
    
    send_mail("a new Post has been Created",
                f"a new Post has been Created with title: {post_title}",
                "from@madmail.com",
                emails
                )