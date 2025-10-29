# 💡 ESP8266 Push Button LED Control using Polling Method (MicroPython)

This project demonstrates how to control an **LED** using a **push button** on the **ESP8266** microcontroller through the **polling method**.  
The code continuously checks the button’s state in a loop and turns the LED ON or OFF accordingly.

---

## 🧠 Project Overview

| Component | Description |
|------------|-------------|
| **Board** | ESP8266 |
| **IDE** | Thonny IDE |
| **Language** | MicroPython |
| **USB Driver** | Silicon Labs CP210x USB to UART Bridge |
| **LED Pin** | GPIO2 |
| **Button Pin** | GPIO0 |

---

## ⚙️ Requirements

- ESP8266 board (NodeMCU or compatible)  
- 1 LED + 220Ω resistor  
- 1 Push Button  
- Micro USB cable  
- [Thonny IDE](https://thonny.org/)  
- [CP210x USB Driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)  
- MicroPython firmware flashed on ESP8266  

---

## 🧩 Circuit Connections

| ESP8266 Pin | Component | Description |
|--------------|------------|--------------|
| GPIO2 | LED | Output (Active LOW) |
| GPIO0 | Push Button | Input (Active LOW) |
| GND | LED (-) and Button GND | Common Ground |

💡 **Tip:** Use an internal or external pull-up resistor on GPIO0 to prevent floating input values.

---

## 💻 Code

```python
import machine

# GPIO2 = one LED connected
# GPIO0 = pushbutton

led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN)

def button_function():
    if button.value() == 0:   # Button pressed
        led.value(0)          # Turn LED ON
    else:                     # Button released
        led.value(1)          # Turn LED OFF

while True:
    button_function()         # Polling method
