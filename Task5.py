import os

# from gpiozero import DistanceSensor

# import adafruit_dht
# import board
import time
import matplotlib.pyplot as plt
import random

LogFile = open("SensorsReadingsLog.txt", 'a')

# ultra = DistanceSensor(echo = 14 , trigger = 15)
# distance = ultra.distance

# Create an instance of the DHT11 sensor connected to GPIO 17
# dht_device = adafruit_dht.DHT11(board.D17)

x1 = []
x2 = []

for i in range(5):
    try:
        # Read temperature and humidity from the sensor
        # temperature_c = dht_device.temperature
        # humidity = dht_device.humidity
        temperature_c = random.random()
        distance = random.random()

        x1.append(temperature_c)
        
        # Print the results
        

        y1 = [1,2,3,4,5]
        

        print(f"Temperature: {temperature_c}\u00b0C")
        # print(f"Humidity: {humidity}%")
    
        x2.append(distance)
        y2 = [1,2,3,4,5]
        print(f"Distance: {distance}")

        LogFile.writelines(f" Temperature: {temperature_c} Distance: {distance}\n")

    except RuntimeError as error:
        # Handle runtime errors (such as timeouts)

        print(f"Error reading sensors data: {error.args[0]}")
    

    # Wait for a short period before reading again
    time.sleep(2)


LogFile.close()



plt.scatter(x1,y1,marker = "x")


plt.scatter(x2,y2,marker = "o")

plt.show()