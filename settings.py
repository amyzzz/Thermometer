import thermometer

def set_color(new_color):
    thermometer.color = new_color
    
def set_url(url):
    thermometer.url = url
    
thermometer = Thermometer()

set_color(input("Set color")
set_url(input("Set url")
thermometer.update()
