#A conditional service, suggested by Moshez, to be expanded on
class ConditionalService:
    __implements__ = service.IService
    def __init__(self, service, conditional):
        self.service, self.conditional = service, conditional
    def start(self):
        self.running = True
        if self.conditional(): self.service.start()
    def stop(self):
        self.running = False
        if self.service.running: self.service.stop()
 
s = ConditionalService(myMultiService, myConditional)
