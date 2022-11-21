# SPDX-License-Identifier: MIT
#
# Copyright (c) 2022 Stephan Linz <linz@li-pro.net>
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

import unittest
from unittest import mock

from verylittlewire import device as vlwd

VENDOR_ID = 0x1781
PRODUCT_ID = 0x0C9F
USB_TIMEOUT = 5000

INPUT = 1
OUTPUT = 0

HIGH = 1
LOW = 0

ENABLE = 1
DISABLE = 0

PIN1 = 1
PIN2 = 2
PIN3 = 5
PIN4 = 0

VREF_VCC = 0
VREF_1100mV = 1
VREF_2560mV = 2

ADC_PIN3 = 0
ADC_PIN2 = 1
ADC_TEMP_SENS = 2

PWM_FREQ_PS4 = 1024
PWM_FREQ_PS3 = 256
PWM_FREQ_PS2 = 64
PWM_FREQ_PS1 = 8
PWM_FREQ_PS0 = 1


class Device(unittest.TestCase):
    def test_usb_vendor(self):
        """
        UNIT TEST: use expected USB vendor identifier
        """

        self.assertEqual(vlwd.VENDOR_ID, VENDOR_ID)

    def test_usb_product(self):
        """
        UNIT TEST: use expected USB product identifier
        """

        self.assertEqual(vlwd.PRODUCT_ID, PRODUCT_ID)

    def test_usb_timeout(self):
        """
        UNIT TEST: use expected USB timeout for communication
        """

        self.assertEqual(vlwd.USB_TIMEOUT, USB_TIMEOUT)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_attach(self, mock_usb, mock_lw):
        """
        UNIT TEST: attach to the correct USB device
        """

        device = vlwd.Device()

        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        mock_usb.core.find.assert_called_with(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        device.lw.set_configuration.assert_called_with()

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_serial(self, mock_usb, mock_lw):
        """
        UNIT TEST: fetch serial number from USB device
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        serial = device.readSerialNumber()
        self.assertIsNotNone(serial)
        self.assertIsInstance(serial, str)

        mock_usb.util.get_string.assert_called_with(device.lw, device.lw.iSerialNumber)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_fwvers(self, mock_usb, mock_lw):
        """
        UNIT TEST: fetch firmware version from USB device
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        fwvers = device.readFirmwareVersion()
        self.assertIsNotNone(fwvers)
        self.assertIsInstance(fwvers, str)
        # not in unit test: self.assertEqual(fwvers, "1.3")

        device.lw.ctrl_transfer.assert_called_with(
            bmRequestType=0xC0,
            bRequest=34,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def test_pin_modes(self):
        """
        UNIT TEST: provide all expected PIN modes
        """

        self.assertEqual(vlwd.INPUT, INPUT)
        self.assertEqual(vlwd.OUTPUT, OUTPUT)

    def test_pin_states(self):
        """
        UNIT TEST: provide all expected PIN states
        """

        self.assertEqual(vlwd.HIGH, HIGH)
        self.assertEqual(vlwd.LOW, LOW)

    def test_pin_names(self):
        """
        UNIT TEST: provide all expected PIN names
        """

        self.assertEqual(vlwd.PIN1, PIN1)
        self.assertEqual(vlwd.PIN2, PIN2)
        self.assertEqual(vlwd.PIN3, PIN3)
        self.assertEqual(vlwd.PIN4, PIN4)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pin_mode_input(self, mock_usb, mock_lw):
        """
        UNIT TEST: setup each known pin as input
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            result = device.pinMode(pin, vlwd.INPUT)  # type: ignore[func-returns-value]
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=13,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pin_mode_output(self, mock_usb, mock_lw):
        """
        UNIT TEST: setup each known pin as output
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            result = device.pinMode(  # type: ignore[func-returns-value]
                pin, vlwd.OUTPUT
            )
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=14,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_digital_write_high(self, mock_usb, mock_lw):
        """
        UNIT TEST: write out digital high to each known pin
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            result = device.digitalWrite(  # type: ignore[func-returns-value]
                pin, vlwd.HIGH
            )
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=18,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_digital_write_low(self, mock_usb, mock_lw):
        """
        UNIT TEST: write out digital low to each known pin
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            result = device.digitalWrite(  # type: ignore[func-returns-value]
                pin, vlwd.LOW
            )
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=19,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_digital_read_state(self, mock_usb, mock_lw):
        """
        UNIT TEST: read in current digital status from each known pin
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            status = device.digitalRead(pin)
            self.assertIsNotNone(status)
            self.assertIsInstance(status, int)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=20,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    def test_pullup_states(self):
        """
        UNIT TEST: provide all expected pull-up resistor states
        """

        self.assertEqual(vlwd.ENABLE, ENABLE)
        self.assertEqual(vlwd.DISABLE, DISABLE)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pullup_enable(self, mock_usb, mock_lw):
        """
        UNIT TEST: enable pull-up resistor on each known pin
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            result = device.internalPullup(  # type: ignore[func-returns-value]
                pin, vlwd.ENABLE
            )
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=18,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pullup_disable(self, mock_usb, mock_lw):
        """
        UNIT TEST: disable pull-up resistor on each known pin
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for pin in [vlwd.PIN1, vlwd.PIN2, vlwd.PIN3, vlwd.PIN4]:

            result = device.internalPullup(  # type: ignore[func-returns-value]
                pin, vlwd.DISABLE
            )
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=19,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    def test_analog_vref_levels(self):
        """
        UNIT TEST: provide all expected analog voltage reference levels
        """

        self.assertEqual(vlwd.VREF_VCC, VREF_VCC)
        self.assertEqual(vlwd.VREF_1100mV, VREF_1100mV)
        self.assertEqual(vlwd.VREF_2560mV, VREF_2560mV)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_analog_init_levels(self, mock_usb, mock_lw):
        """
        UNIT TEST: setup ADC with each known voltage reference level
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for vref in [vlwd.VREF_VCC, vlwd.VREF_1100mV, vlwd.VREF_2560mV]:

            result = device.analogInit(vref)  # type: ignore[func-returns-value]
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=35,
                wValue=((vref << 8) | 0x07),
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    def test_analog_channel_names(self):
        """
        UNIT TEST: provide all expected analog channel names
        """

        self.assertEqual(vlwd.ADC_PIN3, ADC_PIN3)
        self.assertEqual(vlwd.ADC_PIN2, ADC_PIN2)
        self.assertEqual(vlwd.ADC_TEMP_SENS, ADC_TEMP_SENS)

    def test_analog_channel_aliases(self):
        """
        UNIT TEST: provide all expected analog channel aliases
        """

        self.assertEqual(vlwd.ADC0, ADC_PIN3)
        self.assertEqual(vlwd.ADC1, ADC_PIN2)
        self.assertEqual(vlwd.ADC2, ADC_TEMP_SENS)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_analog_read_level(self, mock_usb, mock_lw):
        """
        UNIT TEST: read in current analog level from each known channel
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for channel in [
            vlwd.ADC_PIN3,
            vlwd.ADC0,
            vlwd.ADC_PIN2,
            vlwd.ADC1,
            vlwd.ADC_TEMP_SENS,
            vlwd.ADC2,
        ]:

            level = device.analogRead(channel)
            self.assertIsNotNone(level)
            self.assertIsInstance(level, int)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=15,
                wValue=channel,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )

    def test_pwm_pin_names(self):
        """
        UNIT TEST: provide all expected PWM pin (channel) names
        """

        self.assertEqual(vlwd.PWM_PIN4, PIN4)
        self.assertEqual(vlwd.PWM_PIN1, PIN1)

    def test_pwm_pin_aliases(self):
        """
        UNIT TEST: provide all expected PWM pin (channel) aliases
        """

        self.assertEqual(vlwd.PWMA, PIN4)
        self.assertEqual(vlwd.PWMB, PIN1)
        self.assertEqual(vlwd.PWM1, PIN4)
        self.assertEqual(vlwd.PWM2, PIN1)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_init(self, mock_usb, mock_lw):
        """
        UNIT TEST: setup and initialize the PWM system
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        result = device.pwmInit()  # type: ignore[func-returns-value]
        self.assertIsNone(result)

        device.lw.ctrl_transfer.assert_called_with(
            bmRequestType=0xC0,
            bRequest=16,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_stop(self, mock_usb, mock_lw):
        """
        UNIT TEST: stop all running PWM output on both channel
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        result = device.pwmStop()  # type: ignore[func-returns-value]
        self.assertIsNone(result)

        device.lw.ctrl_transfer.assert_called_with(
            bmRequestType=0xC0,
            bRequest=32,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_update_compare_default(self, mock_usb, mock_lw):
        """
        UNIT TEST: sets the PWM compare value to default zero for both channels
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        result = device.pwmUpdateCompare()  # type: ignore[func-returns-value]
        self.assertIsNone(result)

        device.lw.ctrl_transfer.assert_called_with(
            bmRequestType=0xC0,
            bRequest=17,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_update_compare_maximum(self, mock_usb, mock_lw):
        """
        UNIT TEST: sets the PWM compare value to maximum for both channels
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        channelA = 2 ^ 15
        channelB = 2 ^ 15
        result = device.pwmUpdateCompare(  # type: ignore[func-returns-value]
            channelA, channelB
        )
        self.assertIsNone(result)

        device.lw.ctrl_transfer.assert_called_with(
            bmRequestType=0xC0,
            bRequest=17,
            wValue=channelA,
            wIndex=channelB,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    def test_pwm_prescaler_values(self):
        """
        UNIT TEST: provide all expected PWM prescaler values
        """

        self.assertEqual(vlwd.PWM_FREQ_PS4, PWM_FREQ_PS4)
        self.assertEqual(vlwd.PWM_FREQ_PS3, PWM_FREQ_PS3)
        self.assertEqual(vlwd.PWM_FREQ_PS2, PWM_FREQ_PS2)
        self.assertEqual(vlwd.PWM_FREQ_PS1, PWM_FREQ_PS1)
        self.assertEqual(vlwd.PWM_FREQ_PS0, PWM_FREQ_PS0)

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_update_prescaler_default(self, mock_usb, mock_lw):
        """
        UNIT TEST: sets the PWM prescaler value to default one (2⁰) for both channels
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        result = device.pwmUpdatePrescaler()  # type: ignore[func-returns-value]
        self.assertIsNone(result)

        device.lw.ctrl_transfer.assert_called_with(
            bmRequestType=0xC0,
            bRequest=22,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_update_prescaler_maximum(self, mock_usb, mock_lw):
        """
        UNIT TEST: sets the PWM prescaler value to maximum (2¹⁵) for both channels
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        value = 2 ^ 15
        result = device.pwmUpdatePrescaler(value)  # type: ignore[func-returns-value]
        self.assertIsNone(result)

        device.lw.ctrl_transfer.assert_not_called()

    @mock.patch.object(vlwd.Device, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_pwm_update_prescaler_value(self, mock_usb, mock_lw):
        """
        UNIT TEST: sets the PWM prescaler with each known value for both channels
        """

        device = vlwd.Device()
        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, vlwd.Device)

        for value in [
            (vlwd.PWM_FREQ_PS0, 0),
            (vlwd.PWM_FREQ_PS1, 1),
            (vlwd.PWM_FREQ_PS2, 2),
            (vlwd.PWM_FREQ_PS3, 3),
            (vlwd.PWM_FREQ_PS4, 4),
        ]:

            result = device.pwmUpdatePrescaler(  # type: ignore[func-returns-value]
                value[0]
            )
            self.assertIsNone(result)

            device.lw.ctrl_transfer.assert_called_with(
                bmRequestType=0xC0,
                bRequest=22,
                wValue=value[1],
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )


# vim: tw=80 ts=4 sw=4 sts=4 sta et ai nu
