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

This file is a direct Python translation of the C/C++ library developed by Ihsan
Kehribar <ihsan@kehribar.me> and Omer Kilic <omerkilic@gmail.com>. The C/C++
library was released under the same license. Adam Johnson did the translation
based on the C/C++ library version 0.9 for Python 2. This new reimplementation
is an effort to port the Python 2 translation to Python 3 and adapt the changes
in the C/C++ library from version 0.9 to the latest version 1.2.

:license: MIT, see LICENSE for details.
"""

import usb

VENDOR_ID = 0x1781
PRODUCT_ID = 0x0C9F
USB_TIMEOUT = 5000


class Device:
    """
    Class to control a LittleWire USB Multi-Tool.
    """

    lw = None

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

        serial = usb.util.get_string(
            self.lw, self.lw.iSerialNumber  # type: ignore[union-attr]
        )

        return str(serial)

    def readFirmwareVersion(self) -> str:
        """
        Returns Little Wire firmware version.
        """

        result = self.lw.ctrl_transfer(  # type: ignore[union-attr]
            bmRequestType=0xC0,
            bRequest=34,
            wValue=0,
            wIndex=0,
            data_or_wLength=8,
            timeout=USB_TIMEOUT,
        )

        version = result.pop()

        return str((version & 0xF0) >> 4) + "." + str(version & 0x0F)


# vim: tw=80 ts=4 sw=4 sts=4 sta et ai nu
