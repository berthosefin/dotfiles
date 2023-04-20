

def message_notifications(n_message, n_user):
    str_message = "message"
    str_user = "user"
    if n_message != 1:
        str_message += "s"
    if str_user != 1:
        str_user += "s"
    return f"You have {n_message} {str_message} from {n_user} {str_user}"


if __name__ == "__main__":
    message_notifications(1, 1)
    message_notifications(2, 1)
    message_notifications(1, 2)
    message_notifications(2, 2)
    message_notifications(0, 0)