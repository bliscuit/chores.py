import datetime

allChores = ["Clean cat box",5,[0,2,4],[0,1]],["Clean dog poop",5,[0,2,4],[0,1]],["Empty roomba",5,[0,1,2,3,4,5,6],[0,1,2]],["Take out trash",10,[0],[0,1,2]],["Unstack dishwasher",10,[1,3],[0,1,2]],["Stack dishwasher",15,[0,2,4],[0,1,2]],["Vaccuum stairs",15,[1],[0,1,2]],["Vaccuum upstairs",20,[0],[0,1,2]],["Clean out fridge",10,[6],[0,1,2]],["Wipe down kitchen appliances",10,[1],[0,1,2]],["Wipe down kitchen cabinets",15,[4],[0,1,2]],["Clean half bath",10,[1],[0,1,2]],["Clean guest bath",10,[3],[2]],["Clean master bath",15,[2],[0,1]],["Clean back door",5,[4],[0,1,2]],["Make bed",5,[0,1,2,3,4,5,6],[0,1,2]],["Dust fans",20,[1],[0,1,2]],["Wipe downstairs baseboards",20,[2],[0,1,2]],["Wipe upstairs baseboards",20,[3],[0,1,2]],["Dust living room",10,[ 3],[0,1,2]],["Dust front room",5,[3],[0,1,2]],["Dust bedrooms",20,[4],[0,1,2]],["Feed dogs (morning and night)",5,[0,1,2,3,4,5,6],[0,1,2]],["Shred papers",10,[0,3],[0,1,2]],["Replace hand towels (bathrooms and kitchen)",5,[6],[0,1,2]],["Wash dog beds",10,[5],[0,1,2]]
#today  = datetime.datetime.today().weekday()
today = 2
#person = 0

def minsPerDay(day):
	x = 0
	count = 0
	for item in allChores:
		if day in allChores[x][2]:
			count = count + allChores[x][1]
			x = x + 1
		else:
			x = x + 1
	return count

def choresToday(today):
	x = 0
	todaysChores = []
	for item in allChores:
		if today in allChores[x][2]:
			todaysChores.append(allChores[x])
			x = x + 1
		else:
			x = x + 1
	return todaysChores

def choresTodayPrint():
	listofChores = choresToday(today)
	for item in listofChores:
		print(item)

def choresPerson(person):
	x = 0
	listofChores = choresToday(today)
	yourChores = []
	for item in listofChores:
		if person in listofChores[x][3]:
			yourChores.append(listofChores[x][0])
			x = x + 1
		else:
			x = x + 1
	return yourChores

def choresPersonPrint():
	listofChores = choresPerson(person)
	for item in listofChores:
		print(item)


print("\nAll chores:")			
choresTodayPrint()

print("\nCasey's Chores:")
person = 0
choresPersonPrint()

print("\nMelody's Chores:")
person = 1
choresPersonPrint()

print("\nRyan's Chores:")
person = 2
choresPersonPrint()

#print ("\nToday has",minsPerDay(today),"minutes of chores.")
#print ("\nSunday:   ",minsPerDay(6))
#print ("Monday:   ",minsPerDay(0))
#print ("Tuesday:  ",minsPerDay(1))
#print ("Wednesday:",minsPerDay(2))
#print ("Thursday: ",minsPerDay(3))
#print ("Friday:   ",minsPerDay(4))
#print ("Saturday: ",minsPerDay(5))

input("Press 'Enter' to exit...")