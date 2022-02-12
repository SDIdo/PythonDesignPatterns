class SubscriberInterface:
    def __init__(self, name):
        self.name = name
        self.obj = None

    def update(self, obj):
        pass

class SubTypeOne(SubscriberInterface):
    def update(self, obj):
        print(f"{self.name}: Ok there was a change! Now it's {obj.get_business_note()}")


class Publisher:
    def __init__(self, subscribers):
        self.subscribers = subscribers
        self._business_note = "Business"

    def add_subscriber(self, new_sub):
        self.subscribers.append(new_sub)
    
    def remove_subscriber(self, sub_to_rm):
        self.subscribers.remove(sub_to_rm)

    def notify_subscribers(self):
        for sub in self.subscribers:
            sub.update(self)

    def get_business_note(self):
        return self._business_note
    
    # Upon change in busines note notify subs
    def set_business_note(self, new_business_note):
        self._business_note = new_business_note
        self.notify_subscribers()

# Driver
subs = []
store = Publisher(subs)
toy1 = SubTypeOne("toy1")
store.add_subscriber(toy1)
store.set_business_note("Leisure")
    