class Animal:
	def speak(self):
		raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
	def speak(self):
		return "guhk guhk!"

class Cat(Animal):
	def speak(self):
		return "meong"

animals = [Dog(), Cat()]


for animal in animals:
	print(animal.speak())
