# Tugas 2 encapsulation

class Hero:

	def __init__(self,name,health,attackPower):
		self.__name = name
		self.__health = health
		self.__attPower = attackPower

	# getter
	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	# setter

	def diserang(self,serangPower):
		self.__health -= serangPower

	def setAttPower(self,nilaibaru):
		self.__attPower = nilaibaru

# awal dari game
luki = Hero("luki",50, 5)

# game berjalan

print(luki.getName())
print(luki.getHealth())
luki.diserang(5)
print(luki.getHealth())
