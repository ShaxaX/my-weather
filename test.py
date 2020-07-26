import pyowm
owm = pyowm.OWM('71c2aa5d34fb5450fdd8e44e6ee30a03')
mgr = owm.weather_manager()
a = "Fargona"
h = "Havosi"
observation = mgr.weather_at_place(a)
w = observation.weather
w = w.temperature('celsius')
print(str(a) + " " + str(h) + str(w))