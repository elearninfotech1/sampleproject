class SmallAgeError(Exception):
	def __init__(self, msg):
		self.msg = msg

	
age = int(input("Enter your age: "))

if age < 20:
	raise SmallAgeError("your age is less than 20")
elif age > 30:
	raise BigAgeError("your age is more than 30")
else:
	print("you are eligible for the job")
	
print("thank you!!!")

