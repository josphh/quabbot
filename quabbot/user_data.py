import os
import shutil
import jsons


def delete_user_files(user):
    shutil.rmtree(f"./quabbot/users/{user.id}")


def get_user_file(user, name):
    os.makedirs(f"./quabbot/users/{user.id}", exist_ok=True)
    return f"./quabbot/users/{user.id}/{name}"


def save_user_data(user, data):
    with open(get_user_file(user, "data.json"), "w") as user_file:
        user_file.write(jsons.dumps(data))


def load_user_data(user):
    with open(get_user_file(user, "data.json")) as user_file:
        return jsons.loads(user_file.read())


def has_user_data(user):
    return os.path.exists(get_user_file(user, "data.json"))
