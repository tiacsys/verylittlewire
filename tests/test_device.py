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

PIN1 = 1
PIN2 = 2
PIN3 = 5
PIN4 = 0


class Device(unittest.TestCase):
    def test_usb_vendor(self):
        """
        UNIT TEST: use expected USB vendor identifyer
        """

        self.assertEqual(vlwd.VENDOR_ID, VENDOR_ID)

    def test_usb_product(self):
        """
        UNIT TEST: use expected USB product identifyer
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
        device.lw.set_configuration.assert_called_with()  # type: ignore[union-attr]

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

        mock_usb.util.get_string.assert_called_with(
            device.lw, device.lw.iSerialNumber  # type: ignore[union-attr]
        )

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

        device.lw.ctrl_transfer.assert_called_with(  # type: ignore[union-attr]
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

            device.lw.ctrl_transfer.assert_called_with(  # type: ignore[union-attr]
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

            device.lw.ctrl_transfer.assert_called_with(  # type: ignore[union-attr]
                bmRequestType=0xC0,
                bRequest=14,
                wValue=pin,
                wIndex=0,
                data_or_wLength=8,
                timeout=USB_TIMEOUT,
            )


# vim: tw=80 ts=4 sw=4 sts=4 sta et ai nu
