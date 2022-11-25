from student_management.model.settings import Settings
from student_management.utils.view import View
import pytest


@pytest.fixture
def test_welcome_message():
    welcome_message = View.display_welcome_sms()
    assert welcome_message == Settings.welcome_sms_text
