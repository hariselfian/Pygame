from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
lightblue = (192, 222, 255)

new_sense = SenseHat()
sense = SenseHat()

temp = sense.get_temperature()
temp = (int(temp))

if (temp > 23):
    print ("Suhu Panas: %s C" %temp)
    new_sense.show_message("Suhu Panas: %s C" % temp, text_colour=red, scroll_speed=0.07)
elif (temp > 15 & temp <= 23):
    print ("Suhu Nyaman: %s C" %temp)
    new_sense.show_message("Suhu Nyaman: %s C" % temp, text_colour=green, scroll_speed=0.07)
elif (temp <= 15):
    print ("Suhu Dingin: %s C" %temp)
    new_sense.show_message("Suhu Dingin: %s C" % temp, text_colour=lightblue, scroll_speed=0.07)
else:
    #Error message
    print("Suhu: %s C" %temp)
    print("Error")
    new_sense.show_message("Error, Suhu di atas tidak dapat ditampilkan")