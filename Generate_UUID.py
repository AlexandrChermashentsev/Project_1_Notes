import uuid


def Create_uuid():
    UUID = str(uuid.uuid4())[:13]
    return UUID