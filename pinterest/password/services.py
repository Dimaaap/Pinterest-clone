from django.contrib.auth.hashers import check_password


def check_if_new_password_service(user, new_password: str):
    current_password = user.password
    return check_password(new_password, current_password)