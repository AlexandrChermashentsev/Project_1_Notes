import Generate_UUID

class Note():
    def __init__(self, uuid, format_file, body):
        self._uuid = uuid
        self._format_file = format_file
        self._body = body

    @property
    def uuid(self):
        self._uuid = Generate_UUID.Create_uuid()
        return self._uuid
      
    @property
    def fomat_file(self):
        return self._format_file
    
    @property
    def body(self):
        return self._body
    
    # @body.setter # сеттер
    # def body(self, headline, body):
        # with open()