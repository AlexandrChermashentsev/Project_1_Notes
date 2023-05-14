from uuid import uuid4

def Create_uuid():
    UUID = str(uuid4())[:13] # В имя файла записываю первые 13 символов
    return UUID