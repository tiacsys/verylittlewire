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
"""
Mode identification number to **set a GPIO pin as input**.
"""

OUTPUT: int = 0
"""
Mode identification number to **set a GPIO pin as output**.
"""


HIGH: int = 1
"""
State identification number to **set a GPIO pin to digital high level**.
"""

LOW: int = 0
"""
State identification number to **set a GPIO pin to digital low level**.
"""


# Little Wire internal pull-up resistor states
ENABLE: int = 1
"""
State identification number to **enable internal pull-up resistor**.
"""

DISABLE: int = 0
"""
State identification number to **disable internal pull-up resistor**.
"""


# GPIO pin enumeration
PIN1: int = 1
"""
Real hardware port index of well known **GPIO pin one (1)**.
"""

PIN2: int = 2
"""
Real hardware port index of well known **GPIO pin two (2)**.
"""

PIN3: int = 5
"""
Real hardware port index of well known **GPIO pin three (3)**.
"""

PIN4: int = 0
"""
Real hardware port index of well known **GPIO pin four (4)**.
"""


# ADC voltage reference level
VREF_VCC: int = 0
"""
Voltage reference identification number to **VUSB = 5000mV (USB plug)**.
"""

VREF_1100mV: int = 1
"""
Voltage reference identification number to **internal 1100mV**.
"""

VREF_2560mV: int = 2
"""
Voltage reference identification number to **internal 2560mV**.
"""


# ADC channel enumeration
ADC_PIN3: int = 0
"""
Real hardware **ADC channel index on** well known **GPIO pin three (3)**.
"""

ADC_PIN2: int = 1
"""
Real hardware **ADC channel index on** well known **GPIO pin two (2)**.
"""

ADC_TEMP_SENS: int = 2
"""
Real hardware **ADC channel index on internal temperature sensor**.
"""


# ADC channel aliases
ADC0: int = ADC_PIN3
"""
Channel identification number to **ADC channel zero (0), alias to ADC_PIN3**.
"""

ADC1: int = ADC_PIN2
"""
Channel identification number to **ADC channel one (1), alias to ADC_PIN2**.
"""

ADC2: int = ADC_TEMP_SENS
"""
Channel identification number to **ADC channel two (2), alias to ADC_TEMP_SENS**.
"""


# PWM frequency prescaler value
PWM_FREQ_PS4: int = 1024
"""
Prescaler value to achieve **PWM base clock divided by 1024**.
"""

PWM_FREQ_PS3: int = 256
"""
Prescaler value to achieve **PWM base clock divided by 256**.
"""

PWM_FREQ_PS2: int = 64
"""
Prescaler value to achieve **PWM base clock divided by 64**.
"""

PWM_FREQ_PS1: int = 8
"""
Prescaler value to achieve **PWM base clock divided by 8**.
"""

PWM_FREQ_PS0: int = 1
"""
Prescaler value to **hold PWM base clock**.
"""


# PWM pin (channel) enumeration
PWM_PIN4: int = PIN4
"""
Real hardware **PWM channel index on** well known **GPIO pin four (4)**.
"""

PWM_PIN1: int = PIN1
"""
Real hardware **PWM channel index on** well known **GPIO pin one (1)**.
"""


# PWM pin (channel) aliases
PWMA: int = PWM_PIN4
"""
Channel identification number to **PWM channel A, alias to PWM_PIN4**.
"""

PWMB: int = PWM_PIN1
"""
Channel identification number to **PWM channel B, alias to PWM_PIN1**.
"""

PWM1: int = PWMA
"""
Channel identification number to **PWM channel zero (0), alias to channel A**.
"""

PWM2: int = PWMB
"""
Channel identification number to **PWM channel one (1), alias to channel B**.
"""


class Device:
    """
    Class to control a LittleWire USB Multi-Tool.
    """

    lw: usb.core.Device = None
    """
    Little Wire device object

    This is the USB device object returned by the `PyUSB find function`_ and
    reflects the Little Wire device that was found in association with
    |VENDOR_ID| and |PRODUCT_ID|. This object will be created whet the |Device|
    class will be used to create and initialize a new Very Little Wire device
    object.

    .. _`PyUSB find function`:
       https://github.com/pyusb/pyusb/blob/v1.2.1/docs/tutorial.rst#user-content-lets-get-it-started

    .. |VENDOR_ID| replace::
       :py:attr:`VENDOR_ID <verylittlewire.device.VENDOR_ID>`
    .. |PRODUCT_ID| replace::
       :py:attr:`PRODUCT_ID <verylittlewire.device.PRODUCT_ID>`
    .. |Device| replace::
       :py:class:`Device <verylittlewire.device.Device>`
    .. |__init__| replace::
       :py:meth:`Device.__init__ <verylittlewire.device.Device.__init__>`
    """

    def __init__(self) -> None:
        """
        Finds the first Little Wire device and attaches to it.

        With the help of the `PyUSB find function`_ and the constant values
        |VENDOR_ID| and |PRODUCT_ID| the first detectable Little Wire device
        is stored as USB device object in |lw|. If no Little Wire device can
        be found on the USB bus, the object instantiation will be aborted with
        the exception `ValueError`.

        :raises ValueError: Little Wire device can not found on USB bus.
        :rtype: None

        .. _`PyUSB find function`:
           https://github.com/pyusb/pyusb/blob/v1.2.1/docs/tutorial.rst#user-content-lets-get-it-started

        .. |VENDOR_ID| replace::
           :py:attr:`VENDOR_ID <verylittlewire.device.VENDOR_ID>`
        .. |PRODUCT_ID| replace::
           :py:attr:`PRODUCT_ID <verylittlewire.device.PRODUCT_ID>`
        .. |lw| replace::
           :py:attr:`Device.lw <verylittlewire.device.Device.lw>`
        """

        self.lw = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

        if self.lw is None:
            raise ValueError("Device not Found!")

        self.lw.set_configuration()

    def readSerialNumber(self) -> str:
        """
        Returns Little Wire serial number.

        Retrieve the Little Wire serial number directly from the USB device
        descriptor. It is an direct call into the PyUSB stack by the utility
        function to `retrive a string descriptor from the device`_.

        :return: Little Wire serial number
        :rtype: str

        .. _`retrive a string descriptor from the device`:
           https://github.com/pyusb/pyusb/blob/v1.2.1/docs/tutorial.rst#user-content-control-yourself
        """

        serial = usb.util.get_string(self.lw, self.lw.iSerialNumber)

        return str(serial)

    def readFirmwareVersion(self) -> str:
        """
        Returns Little Wire firmware version.

        Retrieve the firmware version number from the Little Wire USB device
        in following format:

        :code:`0xXY` => **X**: major version, **Y**: minor version

        :return: Little Wire firmware version number
        :rtype: str

        :USB CTR: |UCTR_VERSION_QUERY|

        .. |UCTR_VERSION_QUERY| replace:: :ref:`|UCTR_VERSION_QUERY|`
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
        Sets GPIO pin as input or output.

        :param pin: Mandatory "pin" number that have to setup and can
                    only be a well known number of:
                    |PIN1|, |PIN2|, |PIN3|, or |PIN4|
        :type pin: int
        :param mode: Mandatory "mode" identifyer that have to use for
                     the given "pin" and can only be a value of:
                     |INPUT|, or |OUTPUT|
        :type mode: int
        :rtype: None

        :USB CTR: |UCTR_PIN_SET_INPUT|, |UCTR_PIN_SET_OUTPUT|

        .. |PIN1| replace:: :py:attr:`PIN1 <verylittlewire.device.PIN1>`
        .. |PIN2| replace:: :py:attr:`PIN2 <verylittlewire.device.PIN2>`
        .. |PIN3| replace:: :py:attr:`PIN3 <verylittlewire.device.PIN3>`
        .. |PIN4| replace:: :py:attr:`PIN4 <verylittlewire.device.PIN4>`
        .. |INPUT| replace:: :py:attr:`INPUT <verylittlewire.device.INPUT>`
        .. |OUTPUT| replace:: :py:attr:`OUTPUT <verylittlewire.device.OUTPUT>`
        .. |UCTR_PIN_SET_INPUT| replace:: :ref:`|UCTR_PIN_SET_INPUT|`
        .. |UCTR_PIN_SET_OUTPUT| replace:: :ref:`|UCTR_PIN_SET_OUTPUT|`
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
        Writes a digital high or low to the selected GPIO pin.

        :param pin: Mandatory "pin" number that have to write and can
                    only be a well known number of:
                    |PIN1|, |PIN2|, |PIN3|, or |PIN4|
        :type pin: int
        :param state: Mandatory "state" identifyer that have to use for
                      the given "pin" and can only be a value of:
                      |HIGH|, or |LOW|
        :type state: int
        :rtype: None

        :USB CTR: |UCTR_PIN_SET_HIGH|, |UCTR_PIN_SET_LOW|

        .. |PIN1| replace:: :py:attr:`PIN1 <verylittlewire.device.PIN1>`
        .. |PIN2| replace:: :py:attr:`PIN2 <verylittlewire.device.PIN2>`
        .. |PIN3| replace:: :py:attr:`PIN3 <verylittlewire.device.PIN3>`
        .. |PIN4| replace:: :py:attr:`PIN4 <verylittlewire.device.PIN4>`
        .. |HIGH| replace:: :py:attr:`HIGH <verylittlewire.device.HIGH>`
        .. |LOW| replace:: :py:attr:`LOW <verylittlewire.device.LOW>`
        .. |UCTR_PIN_SET_HIGH| replace:: :ref:`|UCTR_PIN_SET_HIGH|`
        .. |UCTR_PIN_SET_LOW| replace:: :ref:`|UCTR_PIN_SET_LOW|`
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
        Returns the current digital level state of the selected GPIO.

        :param pin: Mandatory "pin" number that have to read and can
                    only be a well known number of:
                    |PIN1|, |PIN2|, |PIN3|, or |PIN4|
        :type pin: int
        :return: Digital level state of given "pin" and can only be
                 a value of: |HIGH|, or |LOW|
        :rtype: int

        :USB CTR: |UCTR_PIN_READ|

        .. |PIN1| replace:: :py:attr:`PIN1 <verylittlewire.device.PIN1>`
        .. |PIN2| replace:: :py:attr:`PIN2 <verylittlewire.device.PIN2>`
        .. |PIN3| replace:: :py:attr:`PIN3 <verylittlewire.device.PIN3>`
        .. |PIN4| replace:: :py:attr:`PIN4 <verylittlewire.device.PIN4>`
        .. |HIGH| replace:: :py:attr:`HIGH <verylittlewire.device.HIGH>`
        .. |LOW| replace:: :py:attr:`LOW <verylittlewire.device.LOW>`
        .. |UCTR_PIN_READ| replace:: :ref:`|UCTR_PIN_READ|`
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
        Sets the state of the internal pull-up resistor for the selected GPIO pin.

        Call this function after you assign the GPIO pin as an input. Otherwise
        this method has no effects.

        :param pin: Mandatory "pin" number that have to setup and can
                    only be a well known number of:
                    |PIN1|, |PIN2|, |PIN3|, or |PIN4|
        :type pin: int
        :param state: Mandatory "state" identifyer that have to use for
                      the given "pin" and can only be a value of:
                      |ENABLE|, or |DISABLE|
        :type state: int
        :rtype: None

        :USB CTR: |UCTR_PIN_SET_HIGH|, |UCTR_PIN_SET_LOW|

        .. |PIN1| replace:: :py:attr:`PIN1 <verylittlewire.device.PIN1>`
        .. |PIN2| replace:: :py:attr:`PIN2 <verylittlewire.device.PIN2>`
        .. |PIN3| replace:: :py:attr:`PIN3 <verylittlewire.device.PIN3>`
        .. |PIN4| replace:: :py:attr:`PIN4 <verylittlewire.device.PIN4>`
        .. |ENABLE| replace:: :py:attr:`ENABLE <verylittlewire.device.ENABLE>`
        .. |DISABLE| replace:: :py:attr:`DISABLE <verylittlewire.device.DISABLE>`
        .. |UCTR_PIN_SET_HIGH| replace:: :ref:`|UCTR_PIN_SET_HIGH|`
        .. |UCTR_PIN_SET_LOW| replace:: :ref:`|UCTR_PIN_SET_LOW|`
        """

        self.digitalWrite(pin, state)

    def analogInit(self, vref: int) -> None:
        """
        Initialize and sets voltage reference level for all ADC channels.

        :param vref: Mandatory "vref" voltage reference identifyer that have
                     to use for all ADC channel and can only be a value of:
                     |VREF_VCC|, |VREF_1100mV|, or |VREF_2560mV|
        :type vref: int
        :rtype: None

        :USB CTR: |UCTR_SETUP_ADC|

        .. |VREF_VCC| replace:: :py:attr:`VREF_VCC <verylittlewire.device.VREF_VCC>`
        .. |VREF_1100mV| replace::
           :py:attr:`VREF_1100mV <verylittlewire.device.VREF_1100mV>`
        .. |VREF_2560mV| replace::
           :py:attr:`VREF_2560mV <verylittlewire.device.VREF_2560mV>`
        .. |UCTR_SETUP_ADC| replace:: :ref:`|UCTR_SETUP_ADC|`
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
        Returns the current digitized analog level of the selected ADC channel.

        Analog voltage reading from |ADC0| resp. |ADC_PIN3| isn't advised
        (it is a bit noisy) but supported. Use it at your own risk.

        :param channel: Mandatory "channel" number that have to read and can
                        only be a well known number of: |ADC0| resp. |ADC_PIN3|,
                        |ADC1| resp. |ADC_PIN2|, or |ADC2| resp. |ADC_TEMP_SENS|
        :type channel: int
        :return: Digitized analog level on given "channel" and can only be
                 a value between: 0…1024
        :rtype: int

        :USB CTR: |UCTR_READ_ADC|

        .. |ADC0| replace:: :py:attr:`ADC0 <verylittlewire.device.ADC0>`
        .. |ADC_PIN3| replace:: :py:attr:`ADC_PIN3 <verylittlewire.device.ADC_PIN3>`
        .. |ADC1| replace:: :py:attr:`ADC1 <verylittlewire.device.ADC1>`
        .. |ADC_PIN2| replace:: :py:attr:`ADC_PIN2 <verylittlewire.device.ADC_PIN2>`
        .. |ADC2| replace:: :py:attr:`ADC2 <verylittlewire.device.ADC2>`
        .. |ADC_TEMP_SENS| replace::
           :py:attr:`ADC_TEMP_SENS <verylittlewire.device.ADC_TEMP_SENS>`
        .. |UCTR_READ_ADC| replace:: :ref:`|UCTR_READ_ADC|`
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

        :rtype: None

        :USB CTR: |UCTR_SETUP_PWM|

        .. |UCTR_SETUP_PWM| replace:: :ref:`|UCTR_SETUP_PWM|`
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

        :rtype: None

        :USB CTR: |UCTR_STOP_PWM|

        .. |UCTR_STOP_PWM| replace:: :ref:`|UCTR_STOP_PWM|`
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

        Update the compare values for both PWM channels. Resolution is 8 bit.

        :param channelA: Optional "channel A" compare value that have to
                         use for the update on indirect corresponding PWM
                         channel |PWM1| resp. |PWMA| resp. |PWM_PIN4| and
                         can only be a value between: 0…255,
                         **defaults to zero (0)**
        :type channelA: int
        :param channelB: Optional "channel B" compare value that have to
                         use for the update on indirect corresponding PWM
                         channel |PWM2| resp. |PWMB| resp. |PWM_PIN1| and
                         can only be a value between: 0…255,
                         **defaults to zero (0)**
        :type channelB: int
        :rtype: None

        :USB CTR: |UCTR_UPDATE_PWM_COMPARE|

        .. |PWM1| replace:: :py:attr:`PWM1 <verylittlewire.device.PWM1>`
        .. |PWMA| replace:: :py:attr:`PWMA <verylittlewire.device.PWMA>`
        .. |PWM_PIN4| replace:: :py:attr:`PWM_PIN4 <verylittlewire.device.PWM_PIN4>`
        .. |PWM2| replace:: :py:attr:`PWM2 <verylittlewire.device.PWM2>`
        .. |PWMB| replace:: :py:attr:`PWMB <verylittlewire.device.PWMB>`
        .. |PWM_PIN1| replace:: :py:attr:`PWM_PIN1 <verylittlewire.device.PWM_PIN1>`
        .. |UCTR_UPDATE_PWM_COMPARE| replace:: :ref:`|UCTR_UPDATE_PWM_COMPARE|`
        """

        self.lw.ctrl_transfer(
            bmRequestType=0xC0,
            bRequest=17,
            wValue=channelA,
            wIndex=channelB,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def pwmUpdatePrescaler(self, value: int = PWM_FREQ_PS0) -> None:
        """
        Sets the PWM prescaler value (frequency) for both channels.

        Update the prescaler of the entire PWM sub-system, therefore both
        channels. Adjust this value according to your need for speed in PWM
        output. Lower prescale means higher frequency on PWM all output
        channels.

        :param value: Optional prescaler "value" that have to use for all PWM
                      channels and can only be a value of |PWM_FREQ_PS0|,
                      |PWM_FREQ_PS1|, |PWM_FREQ_PS2|, |PWM_FREQ_PS3|, or
                      |PWM_FREQ_PS4|, **defaults to one (1)**
        :type value: int
        :rtype: None

        :USB CTR: |UCTR_CHANGE_PWM_PRESCALE|

        .. |PWM_FREQ_PS0| replace::
           :py:attr:`PWM_FREQ_PS0 <verylittlewire.device.PWM_FREQ_PS0>`
        .. |PWM_FREQ_PS1| replace::
           :py:attr:`PWM_FREQ_PS1 <verylittlewire.device.PWM_FREQ_PS1>`
        .. |PWM_FREQ_PS2| replace::
           :py:attr:`PWM_FREQ_PS2 <verylittlewire.device.PWM_FREQ_PS2>`
        .. |PWM_FREQ_PS3| replace::
           :py:attr:`PWM_FREQ_PS3 <verylittlewire.device.PWM_FREQ_PS3>`
        .. |PWM_FREQ_PS4| replace::
           :py:attr:`PWM_FREQ_PS4 <verylittlewire.device.PWM_FREQ_PS4>`
        .. |UCTR_CHANGE_PWM_PRESCALE| replace:: :ref:`|UCTR_CHANGE_PWM_PRESCALE|`
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
