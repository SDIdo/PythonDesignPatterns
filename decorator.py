class Notifier:
    def send(self,msg):
        print(f"Snail: {msg} has been sent")

class BaseDecorator(Notifier):
    def __init__(self, notifier):
        self.notifier = notifier
    
class FacebookNotifier(BaseDecorator):
    def send(self,msg):
        print(f"Facebook: {msg} has ben sent!")
        self.notifier.send(msg)

class SMSNotifier(BaseDecorator):
    def send(self,msg):
        print(f"SMS: {msg} has ben sent!")
        self.notifier.send(msg)

class SlackNotifier(BaseDecorator):
    def send(self,msg):
        print(f"Slack: {msg} has ben sent!")
        self.notifier.send(msg)


class Application:
    def __init__(self, notifier):
        self.__notifier = notifier
    
    def setNotifier(self, notifier):
        self.__notifier = notifier

    def doSomething(self, msg):
        self.__notifier.send(msg)

stack = Notifier()
stack = FacebookNotifier(SMSNotifier(SlackNotifier(stack)))
app = Application(stack)
app.doSomething('Hey!')