from .services import send_email_service, check_if_new_password_service, set_user_new_password_service
from .db_service import get_data_from_model
from .data_storage import DataStorage

data_storage = DataStorage()


class PasswordFormsHandler:

    @staticmethod
    def find_user_form_handler(request, form):
        user_email = form.cleaned_data["email"]
        current_user = get_data_from_model(data_storage.USER_MODEL, "email", user_email)
        token = current_user.get_reset_password_token()
        request.session["token"], request.session["email"] = token, user_email
        send_email_service(user_email, token)

    @staticmethod
    def reset_password_form_handler(user, form):
        password = form.cleaned_data["new_password"]
        if not check_if_new_password_service(user, password):
            set_user_new_password_service(password, user)


