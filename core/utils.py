import uuid


def get_upload_path(instance, filename):
    folder = instance.folder.full_path
    ext = filename.split(".").pop(-1)
    name = str(uuid.uuid4())
    new_name = f"{name}.{ext}"
    return f"{folder}{new_name}"
