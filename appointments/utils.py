from django.contrib.auth.models import User


def create_user(username, password, first_name, last_name, email):
    user = User(username=username, first_name=first_name, last_name=last_name, email=email)
    user.set_password(password)
    user.save()