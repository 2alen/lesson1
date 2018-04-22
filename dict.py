weather = {
	"city" : "Moscow",
	"temperature" : 20,
	"wind" : "eastern"
}
#2
print(weather['city'])
print(weather.get('city'))
#3
weather['temperature']=30
print(weather.get('temperature'))
#4
print('Length is {} elements'.format(len(weather)))
#5
print('country' in weather)
#6
weather['date']='27.05.2017'
print(weather)
#7
weather_list = []
weather_list.append(weather)
weather_list.append({
	"city" : "Chelyabinsk",
	"temperature" : 20,
	"wind" : "NW",
	"date": "12.06.2017"	
	})
weather_list.append({
	"city" : "St.Petersburg",
	"temperature" : 12,
	"wind" : "W",
	"date": "13.03.2017"	
	})
print(weather_list)