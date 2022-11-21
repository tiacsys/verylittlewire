# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022 Stephan Linz <linz@li-pro.net>
# Copyright (c) 2012 Adam Johnson <apjohnson@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Very Little Wire device module.

The module provides a Python interface to the Little Wire USB Multi-Tool
developed by Ihsan Kehribar.

This file is a direct Python translation of the `C/C++ library`_ developed by
Ihsan Kehribar <ihsan@kehribar.me> and Omer Kilic <omerkilic@gmail.com>. The
C/C++ library was released under the same license. Adam Johnson did the
`translation based on the C/C++ library version 0.9 for Python 2`_. This new
reimplementation is an effort to port the Python 2 translation to Python 3 and
adapt the changes in the C/C++ library from version 0.9 to the latest version
1.2 or higher.

:license: MIT, see LICENSE for details.

.. _`C/C++ library`:
   https://github.com/littlewire/Little-Wire/tree/v1.2/software/library
.. _`translation based on the C/C++ library version 0.9 for Python 2`:
   https://github.com/adajoh99/VeryLittleWire
"""

import usb

VENDOR_ID: int = 0x1781
"""
USB vendor identifier

The USB vendor identifier that will be used to found the Little Wire devices
when the Little Wire object will be create and initialize by |__init__| together
with the USB product identifier |PRODUCT_ID|. This is an constant integer value
of `0x1781`_ and reflects the USB database entry for *Multiple Vendors*.

.. _`0x1781`: https://devicehunt.com/view/type/usb/vendor/1781

.. |PRODUCT_ID| replace::
   :py:attr:`PRODUCT_ID <verylittlewire.device.PRODUCT_ID>`
.. |__init__| replace::
   :py:meth:`Device.__init__ <verylittlewire.device.Device.__init__>`
"""

PRODUCT_ID: int = 0x0C9F
"""
USB product identifier

The USB product identifier that will be used to found the Little Wire devices
when the Little Wire object will be create and initialize by |__init__| together
with the USB vendor identifier |VENDOR_ID|. This is an constant integer value of
`0x0C9F`_ and reflects the USB database entry for *USBtiny*.

.. _`0x0C9F`: https://devicehunt.com/view/type/usb/vendor/1781/device/0C9F

.. |VENDOR_ID| replace::
   :py:attr:`VENDOR_ID <verylittlewire.device.VENDOR_ID>`
.. |__init__| replace::
   :py:meth:`Device.__init__ <verylittlewire.device.Device.__init__>`
"""

USB_TIMEOUT: int = 5000

# Little Wire pin modes and states
INPUT: int = 1
OUTPUT: int = 0

HIGH: int = 1
LOW: int = 0

# Little Wire internal pull-up resistor states
ENABLE: int = 1
DISABLE: int = 0

# GPIO pin enumeration
PIN1: int = 1
PIN2: int = 2
PIN3: int = 5
PIN4: int = 0

# ADC voltage reference level
VREF_VCC: int = 0
VREF_1100mV: int = 1
VREF_2560mV: int = 2

# ADC channel enumeration
ADC_PIN3: int = 0
ADC_PIN2: int = 1
ADC_TEMP_SENS: int = 2

# ADC channel aliases
ADC0: int = ADC_PIN3
ADC1: int = ADC_PIN2
ADC2: int = ADC_TEMP_SENS

# PWM frequency prescaler value
PWM_FREQ_PS4: int = 1024
PWM_FREQ_PS3: int = 256
PWM_FREQ_PS2: int = 64
PWM_FREQ_PS1: int = 8
PWM_FREQ_PS0: int = 1

# PWM pin (channel) enumeration
PWM_PIN4: int = PIN4
PWM_PIN1: int = PIN1

# PWM pin (channel) aliases
PWMA: int = PWM_PIN4
PWMB: int = PWM_PIN1
PWM1: int = PWMA
PWM2: int = PWMB


class Device:
    """
    Class to control a LittleWire USB Multi-Tool.
    """

    lw: usb.core.Device = None

    def __init__(self) -> None:
        """
        Finds the first Little Wire device and attaches to it.
        """

        self.lw = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

        if self.lw is None:
            raise ValueError("Device not Found!")

        self.lw.set_configuration()

    def readSerialNumber(self) -> str:
        """
        Returns Little Wire serial number.
        """

        serial = usb.util.get_string(self.lw, self.lw.iSerialNumber)

        return str(serial)

    def readFirmwareVersion(self) -> str:
        """
        Returns Little Wire firmware version.
        """

        result = self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=34,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

        version = result.pop()

        return str((version & 0xF0) >> 4) + "." + str(version & 0x0F)

    def pinMode(self, pin: int, mode: int) -> None:
        """
        Sets GPIO pins to INPUT(1) or OUTPUT(0).
        """

        if mode == INPUT:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=13,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )
        else:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=14,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    def digitalWrite(self, pin: int, state: int) -> None:
        """
        Writes a digital HIGH (1) or LOW (0) to the selected GPIO.
        """

        if state == HIGH:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=18,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )
        else:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=19,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    def digitalRead(self, pin: int) -> int:
        """
        Returns the digital status of the selected GPIO
        """

        result = self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=20,
            wValue=pin,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

        status = result.pop()

        return int(status)

    def internalPullup(self, pin: int, state: int) -> None:
        """
        Sets the state of the internal pull-up resistor for the selected GPIO.
        """

        self.digitalWrite(pin, state)

    def analogInit(self, vref: int) -> None:
        """
        Sets voltage reference level for all ADC channel.
        """

        self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=35,
            wValue=((vref << 8) | 0x07),
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def analogRead(self, channel: int) -> int:
        """
        Sets voltage reference level for all ADC channel.
        """

        result = self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=15,
            wValue=channel,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

        level = (result.pop() * 256) + result.pop()

        return int(level)

    def pwmInit(self) -> None:
        """
        Setup and initialize the PWM system.
        """

        self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=16,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def pwmStop(self) -> None:
        """
        Stops all running PWM output on both channel.
        """

        self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=32,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def pwmUpdateCompare(self, channelA: int = 0, channelB: int = 0) -> None:
        """
        Sets the PWM compare value for both channels.
        """

        self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=17,
            wValue=channelA,
            wIndex=channelB,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def pwmUpdatePrescaler(self, value: int = 1) -> None:
        """
        Sets the PWM prescaler value (frequency) for both channels.
        """

        if value == PWM_FREQ_PS4:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=22,
                wValue=4,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )
        elif value == PWM_FREQ_PS3:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=22,
                wValue=3,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )
        elif value == PWM_FREQ_PS2:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=22,
                wValue=2,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )
        elif value == PWM_FREQ_PS1:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=22,
                wValue=1,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )
        elif value == PWM_FREQ_PS0:
            self.lw.ctrl_transfer(
                bmRequestType=0xC0,
                bRequest=22,
                wValue=0,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )


# vim: tw=80 ts=4 sw=4 sts=4 sta et ai nu
