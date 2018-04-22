dict = {
	"Andrey" : {
		"city" : "St.Petersburg",
		"temperature" : 12,
		"wind" : "W"
		},
	"Masha" : {
		"city" : "St.Petersburg",
		"temperature" : 13,
		"wind" : "SW"
		},
	"Oleg" : {	
		"city" : "Chelyabinsk",
		"temperature" : 20,
		"wind" : "NW"
		},
	"Dasha" : {
		"city" : "Moscow",
		"temperature" : 20,
		"wind" : "eastern"
		}
}

name = (input('Enter your name:\n')).capitalize()
#name = "Andrey1"
print(name)
#if dict.get(name)
print(dict.get(name)['city']+' '+str(dict.get(name)['temperature'])+' '+dict.get(name)['wind'])
#print(dict.get(name,'No such na,e in DB!'))
