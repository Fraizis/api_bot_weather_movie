from database.models import User


def user_create(user_id, message, date):
    User.create(user_id=user_id, user_message=message, date=date)


