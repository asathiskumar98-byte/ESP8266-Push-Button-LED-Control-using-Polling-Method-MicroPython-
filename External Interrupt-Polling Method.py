import machine
#GPIO2 = one LED connected
#GPIO0 = pushbutton
led = machine.Pin(2,machine.Pin.OUT)
button = machine.Pin(0,machine.Pin.IN)

def button_function():
    if(button.value() == 0):
        led.value(0)
    else:
        led.value(1)

while True:
    button_function() #Polling Method
