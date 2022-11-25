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

from verylittlewire.device import Device as VLWDevice

VENDOR_ID = 0x1781
PRODUCT_ID = 0x0C9F
USB_TIMEOUT = 5000


class Device(unittest.TestCase):
    def test_usb_vendor(self):
        """
        UNIT TEST: use expected USB vendor identifyer
        """
        from verylittlewire.device import VENDOR_ID as DeviceVID

        self.assertEqual(DeviceVID, VENDOR_ID)

    def test_usb_product(self):
        """
        UNIT TEST: use expected USB product identifyer
        """
        from verylittlewire.device import PRODUCT_ID as DevicePID

        self.assertEqual(DevicePID, PRODUCT_ID)

    def test_usb_timeout(self):
        """
        UNIT TEST: use expected USB timeout for communication
        """
        from verylittlewire.device import USB_TIMEOUT as DeviceUTO

        self.assertEqual(DeviceUTO, USB_TIMEOUT)

    @mock.patch.object(VLWDevice, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_attach(self, mock_usb, mock_lw):
        """
        UNIT TEST: attach to the correct USB device
        """

        device = VLWDevice()

        mock_usb.core.find.assert_called_with(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        device.lw.set_configuration.assert_called_with()  # type: ignore[union-attr]

        self.assertIsNotNone(device)
        self.assertIsNotNone(device.lw)
        self.assertIsInstance(device, VLWDevice)

    @mock.patch.object(VLWDevice, "lw")
    @mock.patch("verylittlewire.device.usb")
    def test_fwvers(self, mock_usb, mock_lw):
        """
        UNIT TEST: fetch firmware version from USB device
        """

        device = VLWDevice()
        fwvers = device.readFirmwareVersion()

        device.lw.ctrl_transfer.assert_called_with(  # type: ignore[union-attr]
            bmRequestType=0xC0,
            bRequest=34,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

        self.assertIsNotNone(device)
        self.assertIsNotNone(fwvers)
        self.assertIsInstance(fwvers, str)
        # not in unit test: self.assertEqual(fwvers, "1.3")


# vim: tw=80 ts=4 sw=4 sts=4 sta et ai nu
