from student_management.model.settings import Settings


class FileManager:

    @staticmethod
    def write_json(users):
        user_json = users.json()
        try:

            with open(Settings().user_sample_path, "w") as outfile:
                outfile.write(user_json)
        except Exception as e:
            print("Oops!", e, "occurred.")
            print("Next entry.")
