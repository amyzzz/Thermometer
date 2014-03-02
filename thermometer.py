
import csv
import graphics
import json
import urllib.request

class Thermometer(object):

    color = 'Red'
    url = "http://www.kimonolabs.com/api/6gdqjftg?apikey=0781dcd19879b0e07c2b2f88444c6f0c"

    def __init__(self):
        self.image = graphics.Canvas(150, 450)
        thermometer = 'therm.gif'
        self.image.draw_image((0, 0), thermometer)
    
    def find_value(self, str, data):
        index = data.index(str)
        start = index + len(str) + 4
        end = data.index('"', start)
        currency = data[start]
        temp = data[start+1:end]
        return temp.replace(',', ''), currency
    

    
    def update(self):
        results = urllib.request.urlopen(self.url).read().decode()

        amt_raised = int(self.find_value("Raised", results)[0])
        goal = int(self.find_value("Goal", results)[0])


        y_bars = amt_raised*335//goal

        count = 350

        while (count > (350-y_bars) and count > 15):
            pos = (26, count)
            points = graphics.rectangle_points(pos, 4, 1)
            self.image.draw_polygon(points, self.color, self.color)
            count -= 1
    
        if y_bars > 335:
            y_bars = 335
            self.image.draw_image((0, 0), 'burst.gif')
  
        self.image.draw_text(amt_raised, (60, 350-y_bars))
        self.image.draw_text(goal, (5, 405))


        wait = input("PRESS ENTER TO CONTINUE.")
        
thermometer = Thermometer()


