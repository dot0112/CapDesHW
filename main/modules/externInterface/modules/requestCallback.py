from models import singleton, ControlFlag


@singleton
class RequestCallback:
    def __init__(self):
        self.controlFlag = ControlFlag()

    def parseRequest(self):
        None
