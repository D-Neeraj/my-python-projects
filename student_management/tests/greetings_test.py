from student_management.model.settings import Settings
from student_management.utils.view import View


def test_welcome_message():
    welcome_message = View.display_welcome_sms()
    assert welcome_message == Settings().welcome_sms_text


def test_display_select_user_option():
    user_option_text = View.display_select_user_option()
    assert user_option_text == Settings().select_user_option_text
