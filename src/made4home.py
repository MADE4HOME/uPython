"""

MIT License

Copyright (c) [2023] [MADE4HOME]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from neopixel import NeoPixel

from machine import Pin, SoftI2C

from mcp23008 import MCP23008


PIN_LEDs = 16
"""Pin of the two LEDs.
"""

PIN_RELAY_1 = 4
"""Pin of the Relay 1 at the I2C expander.
"""

PIN_RELAY_2 = 5
"""Pin of the Relay 2 at the I2C expander.
"""

PIN_RELAY_3 = 6
"""Pin of the Relay 3 at the I2C expander.
"""

PIN_RELAY_4 = 7
"""Pin of the Relay 4 at the I2C expander.
"""

PIN_IN_1 = 3
"""Pin of the Input 1 at the I2C expander.
"""

PIN_IN_2 = 2
"""Pin of the Input 2 at the I2C expander.
"""

PIN_IN_3 = 1
"""Pin of the Input 3 at the I2C expander.
"""

PIN_IN_4 = 0
"""Pin of the Input 4 at the I2C expander.
"""

PIN_SDA_1 = 33
"""Pin SDA of the I2C 1.
"""

PIN_SCL_1 = 32
"""Pin SCL of the I2C 1.
"""

PIN_SDA_2 = 15
"""Pin SDA of the I2C 2.
"""

PIN_SCL_2 = 14
"""Pin SCL of the I2C 2.
"""

PIN_RS485_EN = 2
"""Pin enable of the RS485.
"""

PIN_RS485_RX = 39
"""Pin RX of the RS485.
"""

PIN_RS485_TX = 4
"""Pin TX of the RS485.
"""

PIN_ETH_PHY_ADDR = 0
"""Pin ADDR of the Ethernet.
"""

PIN_ETH_PHY_POWER = 5
"""Pin POWER of the Ethernet.
"""

PIN_ETH_PHY_MDC = 23
"""Pin MDC of the Ethernet.
"""

PIN_ETH_PHY_MDIO = 18
"""Pin MDIO of the Ethernet.
"""

# PIN_ETH_PHY_TYPE = ETH_PHY_LAN8720
"""Pin type of the Ethernet.
"""

# PIN_ETH_CLK_MODE = ETH_CLOCK_GPIO0_IN
"""Clock mode of the Ethernet.
"""

LED_COUNT = 2
"""Number of the programable LEDs at the board.
"""

LED_BRIGHTNESS = 255

IO_EXPANDER_ADDRESS = 0x20

STATE_ON = "on"

STATE_OFF = "off"

PINS_INPUTS = 4

PINS_RELAYS = 4

PinsInputs = [PIN_IN_1, PIN_IN_2, PIN_IN_3, PIN_IN_4]
"""Array that holds the inputs pins definitions.
"""

PinsRelays = [PIN_RELAY_1, PIN_RELAY_2, PIN_RELAY_3, PIN_RELAY_4]
"""Array that holds the outputs pins definitions.
"""

class Made4Home:
    """Made4Home IO board abstraction class.
    """

    __LEDs = None
    """NEO pixel instance.
    """
    
    __TWIOne = None
    """Two Wire Interface with index 0.
    """

    __MCP = None
    """MCP IO chip abstraction instance.
    """

    def __init__(self):
        """Constructor
        """        

        # self.setup()
        pass

    def setup(self):
        """Setup the IO board.
        """

        self.__LEDs = NeoPixel(Pin(PIN_LEDs), LED_COUNT)
        self.__LEDs[0] = (0,0,0)
        self.__LEDs[1] = (0,0,0)
        self.__LEDs.write()

        self.__TWIOne = SoftI2C(scl=Pin(PIN_SCL_1), sda=Pin(PIN_SDA_1), freq=100000)
        self.__MCP = MCP23008(self.__TWIOne, IO_EXPANDER_ADDRESS)
        self.__MCP.setPinDir(PIN_RELAY_1, 0)
        self.__MCP.setPinDir(PIN_RELAY_2, 0)
        self.__MCP.setPinDir(PIN_RELAY_3, 0)
        self.__MCP.setPinDir(PIN_RELAY_4, 0)
        self.__MCP.setPinDir(PIN_IN_1, 1)
        self.__MCP.setPinDir(PIN_IN_2, 1)
        self.__MCP.setPinDir(PIN_IN_3, 1)
        self.__MCP.setPinDir(PIN_IN_4, 1)

    def setLED(index, r, g, b):
        """Set the color of the LEDs.

        Args:
            index (int): Index of the LEDs [0-1]
            r (int): Red color. [0-255]
            g (int): Green color [0-255]
            b (int): Blue color [0-255]
        """

        self.__LEDs[index] = (r, g, b)
        self.__LEDs.write()

    def setL1(self, r, g, b):
        """Set the color of the L1 LED.

        Args:
            r (int): Red color. [0-255]
            g (int): Green color [0-255]
            b (int): Blue color [0-255]
        """

        self.__LEDs[0] = (r, g, b)
        self.__LEDs.write()

    def setL2(self, r, g, b):
        """Set the color of the L2 LED.

        Args:
            r (int): Red color. [0-255]
            g (int): Green color [0-255]
            b (int): Blue color [0-255]
        """

        self.__LEDs[1] = (r, g, b)
        self.__LEDs.write()

    def digitalRead(self, pin):
        """Read the digital inputs of the IO board.

        Args:
            pin (int): Pin number [PIN_IN_1 .. 4]
        """
        
        if pin > PIN_IN_1 or pin < PIN_IN_4:
            return 0

        return self.__MCP.readPin(pin)

    def digitalWrite(self, pin, state):
        """Write to the relay outputs of the IO board.

        Args:
            pin (int): Pin number [PIN_RELAY_1 .. 4]
            state (int): HIGH or LOW
        """

        if pin < PIN_RELAY_1 or pin > PIN_RELAY_4:
            return

        if state == 1:
            self.__MCP.setPinHigh(pin)

        if state == 0:
            self.__MCP.setPinLow(pin)

m4h = Made4Home()
