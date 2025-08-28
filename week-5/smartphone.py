# Base Class (Parent)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"📞 Calling {number} from {self.device_info()}..."

    def charge(self):
        return f"🔋 Charging {self.device_info()}..."

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh"


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 4200)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 5000)

print(phone1.phone_info())
print(phone1.make_call("+251911000000"))
print(phone2.charge())
