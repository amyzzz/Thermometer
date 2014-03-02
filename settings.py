
<script type="text/javascript" src="//sslstatic.wix.com/services/js-sdk/1.24.0/js/Wix.js"></script>

import thermometer

def set_color(new_color):
    thermometer.color = new_color
    
def set_url(url):
    thermometer.url = url
    
thermometer = Thermometer()

set_color(input("Set color")
set_url(input("Set url")
thermometer.update()
