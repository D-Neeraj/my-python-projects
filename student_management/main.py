from student_management.utils.view import View

# A special condition that gets executed only when you run the Python file from the command line.
if __name__ == "__main__":
    # Calling the `display_welcome_sms` and `get_application_inputs` methods of the `View` class.
    View.display_welcome_sms()
    View.get_application_inputs()
