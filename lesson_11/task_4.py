class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)
        self._log_error()

    def _log_error(self):
        with open("errors.log", 'a') as file:
            file.write(f"{self.msg}\n")
