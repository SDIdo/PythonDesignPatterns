# The Bridge Pattern : Device and Controller
from abc import ABC, abstractmethod

class AbstractController:
    def __init__(self, abstractDevice):
        self.abstractDevice = abstractDevice

    def press(self, button):
        return f"Pressed {button} and {self.abstractDevice.pressed(button)}"
    
    def operation(self):
        return f"{self.abstractDevice.deviceName()}"

class ConcreteControllerA(AbstractController):
    def operation(self):
        return (f"Controller A with: "
                f"{self.abstractDevice.deviceName()}")

    def press(self, button):
        return f"Pressed {button} but it's broken! so no change in {self.abstractDevice.deviceName()}"

class ConcreteControllerB(AbstractController):
    def operation(self):
        return (f"Controller B with: "
                f"{self.abstractDevice.deviceName()}")

class AbstractDevice(ABC):
    @abstractmethod
    def deviceName(self):
        pass

    def pressed(self, button):
        pass

class ConcreteDeviceA(AbstractDevice):
    def deviceName(self):
        return "platform A"

    def pressed(self, button):
        return "Device A was muted" if button == 9 else "Device A no change"

class ConcreteDeviceB(AbstractDevice):
    def deviceName(self):
        return "platform B"

    def pressed(self, button):
        return "Device B was shutdown" if button == 9 else "Device B no change"

# def client_code(abstraction: AbstractController):
#     print(abstraction.operation(), end="")

# Driver
controller = AbstractController(ConcreteDeviceB())
print(controller.press(9))
print("\n")
controller = ConcreteControllerA(ConcreteDeviceB())
print(controller.press(9))
# print("\n")
# device = ConcreteDeviceB()
# abstraction = AbstractController(device)
# client_code(abstraction)

# abstraction = AbstractDevice
# abstraction.deviceOperation()

