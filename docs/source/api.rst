API Reference
=============

.. rubric:: Modules
.. autosummary::
   :template: autosummary/module.rst
   :toctree: _autosummary
   :recursive:

   verylittlewire

USB Control Transfers
---------------------

The Little Wire USB device firmware version 1.2 supports the following `Control Transfer`_ sequences. In the `Setup Packet`_ of the **Setup Stage** only the :code:`bmRequestType = 0xC0` will be accepted. That means:

:D7 Data Phase Transfer Direction: 1 = Device to Host
:D6…5 Type: 2 = Vendor
:D4…0 Recipient: 0 = Device

The number of bytes to transfer have to be constant :code:`wLength = 8` for each `Setup Packet`_. That means that each **Setup Stage** follows a **Data Stage**.

.. _`Control Transfer`: https://www.beyondlogic.org/usbnutshell/usb4.shtml
.. _`Setup Packet`: https://www.beyondlogic.org/usbnutshell/usb6.shtml

.. rubric:: USB Control Transfer Requests Overview

.. flat-table:: Little Wire Firmware all well known Control Transfer Requests
   :header-rows: 2
   :stub-columns: 1
   :widths: 1 7 1 1
   :name: lwfw12-usbctr-overview

   * - :cspan:`1` `Setup Packet`_
     - :rspan:`1` Functional Classification
     - :rspan:`1` Firmware Status
   * - :code:`bRequest`
     - Name

   * - :ref:`|UCTR_ECHO|`
     - |ENUM_ECHO|
     - :rspan:`4` :cspan:`1` |UCTR_USBTINY|
   * - :ref:`|UCTR_READ|`
     - |ENUM_READ|
   * - :ref:`|UCTR_WRITE|`
     - |ENUM_WRITE|
   * - :ref:`|UCTR_CLR|`
     - |ENUM_CLR|
   * - :ref:`|UCTR_SET|`
     - |ENUM_SET|

   * - :ref:`|UCTR_POWERUP|`
     - |ENUM_POWERUP|
     - :rspan:`7` :cspan:`1` |UCTR_USBTINY_ISPSPI|
   * - :ref:`|UCTR_POWERDOWN|`
     - |ENUM_POWERDOWN|
   * - :ref:`|UCTR_SPI|`
     - |ENUM_SPI|
   * - :ref:`|UCTR_POLL_BYTES|`
     - |ENUM_POLL_BYTES|
   * - :ref:`|UCTR_FLASH_READ|`
     - |ENUM_FLASH_READ|
   * - :ref:`|UCTR_FLASH_WRITE|`
     - |ENUM_FLASH_WRITE|
   * - :ref:`|UCTR_EEPROM_READ|`
     - |ENUM_EEPROM_READ|
   * - :ref:`|UCTR_EEPROM_WRITE|`
     - |ENUM_EEPROM_WRITE|

   * - :ref:`|UCTR_PIN_SET_INPUT|`
     - |ENUM_PIN_SET_INPUT|
     - :rspan:`1` |UCTR_LWFW_GPIO|
     - |STATE_PIN_SET_INPUT|
   * - :ref:`|UCTR_PIN_SET_OUTPUT|`
     - |ENUM_PIN_SET_OUTPUT|
     - |STATE_PIN_SET_OUTPUT|

   * - :ref:`|UCTR_READ_ADC|`
     - |ENUM_READ_ADC|
     - |UCTR_LWFW_ADC|
     - |STATE_READ_ADC|

   * - :ref:`|UCTR_SETUP_PWM|`
     - |ENUM_SETUP_PWM|
     - :rspan:`1` |UCTR_LWFW_PWM|
     - |STATE_SETUP_PWM|
   * - :ref:`|UCTR_UPDATE_PWM_COMPARE|`
     - |ENUM_UPDATE_PWM_COMPARE|
     - |STATE_UPDATE_PWM_COMPARE|

   * - :ref:`|UCTR_PIN_SET_HIGH|`
     - |ENUM_PIN_SET_HIGH|
     - :rspan:`2` |UCTR_LWFW_GPIO|
     - |STATE_PIN_SET_HIGH|
   * - :ref:`|UCTR_PIN_SET_LOW|`
     - |ENUM_PIN_SET_LOW|
     - |STATE_PIN_SET_LOW|
   * - :ref:`|UCTR_PIN_READ|`
     - |ENUM_PIN_READ|
     - |STATE_PIN_READ|

   * - :ref:`|UCTR_SINGLE_SPI|`
     - |ENUM_SINGLE_SPI|
     - |UCTR_LWFW_SPI|
     - |STATE_SINGLE_SPI|

   * - :ref:`|UCTR_CHANGE_PWM_PRESCALE|`
     - |ENUM_CHANGE_PWM_PRESCALE|
     - |UCTR_LWFW_PWM|
     - |STATE_CHANGE_PWM_PRESCALE|

   * - :ref:`|UCTR_SETUP_SPI|`
     - |ENUM_SETUP_SPI|
     - |UCTR_LWFW_SPI|
     - |STATE_SETUP_SPI|

   * - :ref:`|UCTR_SETUP_I2C|`
     - |ENUM_SETUP_I2C|
     - :rspan:`3` |UCTR_LWFW_I2C|
     - |STATE_SETUP_I2C|
   * - :ref:`|UCTR_I2C_BEGIN_TX|`
     - |ENUM_I2C_BEGIN_TX|
     - |STATE_I2C_BEGIN_TX|
   * - :ref:`|UCTR_I2C_ADD_BUFFER|`
     - |ENUM_I2C_ADD_BUFFER|
     - |STATE_I2C_ADD_BUFFER|
   * - :ref:`|UCTR_I2C_SEND_BUFFER|`
     - |ENUM_I2C_SEND_BUFFER|
     - |STATE_I2C_SEND_BUFFER|

   * - :ref:`|UCTR_SPI_ADD_BUFFER|`
     - |ENUM_SPI_ADD_BUFFER|
     - :rspan:`1` |UCTR_LWFW_SPI|
     - |STATE_SPI_ADD_BUFFER|
   * - :ref:`|UCTR_SPI_SEND_BUFFER|`
     - |ENUM_SPI_SEND_BUFFER|
     - |STATE_SPI_SEND_BUFFER|

   * - :ref:`|UCTR_I2C_REQUEST_FROM|`
     - |ENUM_I2C_REQUEST_FROM|
     - |UCTR_LWFW_I2C|
     - |STATE_I2C_REQUEST_FROM|

   * - :ref:`|UCTR_SPI_UPDATE_DELAY|`
     - |ENUM_SPI_UPDATE_DELAY|
     - |UCTR_LWFW_SPI|
     - |STATE_SPI_UPDATE_DELAY|

   * - :ref:`|UCTR_STOP_PWM|`
     - |ENUM_STOP_PWM|
     - |UCTR_LWFW_PWM|
     - |STATE_STOP_PWM|

   * - :ref:`|UCTR_DEBUG_SPI|`
     - |ENUM_DEBUG_SPI|
     - |UCTR_LWFW_SPI|
     - |STATE_DEBUG_SPI|

   * - :ref:`|UCTR_VERSION_QUERY|`
     - |ENUM_VERSION_QUERY|
     - |UCTR_LWFW|
     - |STATE_VERSION_QUERY|

   * - :ref:`|UCTR_SETUP_ADC|`
     - |ENUM_SETUP_ADC|
     - |UCTR_LWFW_ADC|
     - |STATE_SETUP_ADC|

   * - 36
     - :rspan:`3` :cspan:`2` **GAP** – spare Control Transfer Requests –
   * - 37
   * - 38
   * - 39

   * - :ref:`|UCTR_READ_RESULT|`
     - |ENUM_READ_RESULT|
     - |UCTR_LWFW|
     - |STATE_READ_RESULT|

   * - :ref:`|UCTR_OW_RESET_PULSE|`
     - |ENUM_OW_RESET_PULSE|
     - :rspan:`2` |UCTR_LWFW_OW|
     - |STATE_OW_RESET_PULSE|
   * - :ref:`|UCTR_OW_WRITE_BYTE|`
     - |ENUM_OW_WRITE_BYTE|
     - |STATE_OW_WRITE_BYTE|
   * - :ref:`|UCTR_OW_READ_BYTE|`
     - |ENUM_OW_READ_BYTE|
     - |STATE_OW_READ_BYTE|

   * - :ref:`|UCTR_I2C_INIT|`
     - |ENUM_I2C_INIT|
     - :rspan:`2` |UCTR_LWFW_I2C|
     - |STATE_I2C_INIT|
   * - :ref:`|UCTR_I2C_START|`
     - |ENUM_I2C_START|
     - |STATE_I2C_START|
   * - :ref:`|UCTR_I2C_READ|`
     - |ENUM_I2C_READ|
     - |STATE_I2C_READ|

   * - :ref:`|UCTR_SOFT_PWM_INIT|`
     - |ENUM_SOFT_PWM_INIT|
     - :rspan:`1` |UCTR_LWFW_SOFT_PWM|
     - |STATE_SOFT_PWM_INIT|
   * - :ref:`|UCTR_SOFT_PWM_UPDATE|`
     - |ENUM_SOFT_PWM_UPDATE|
     - |STATE_SOFT_PWM_UPDATE|

   * - :ref:`|UCTR_I2C_UPDATE_DELAY|`
     - |ENUM_I2C_UPDATE_DELAY|
     - |UCTR_LWFW_I2C|
     - |STATE_I2C_UPDATE_DELAY|

   * - :ref:`|UCTR_OW_READ_BIT|`
     - |ENUM_OW_READ_BIT|
     - :rspan:`1` |UCTR_LWFW_OW|
     - |STATE_OW_READ_BIT|
   * - :ref:`|UCTR_OW_WRITE_BIT|`
     - |ENUM_OW_WRITE_BIT|
     - |STATE_OW_WRITE_BIT|

   * - :ref:`|UCTR_PIC24F_PROG|`
     - |ENUM_PIC24F_PROG|
     - :rspan:`1` |UCTR_LWFW_EXP|
     - |STATE_PIC24F_PROG|
   * - :ref:`|UCTR_PIC24F_SENDSIX|`
     - |ENUM_PIC24F_SENDSIX|
     - |STATE_PIC24F_SENDSIX|

   * - :ref:`|UCTR_WS2812_EXEC|`
     - |ENUM_WS2812_EXEC|
     - |UCTR_LWFW_WS2812|
     - |STATE_WS2812_EXEC|

   * - :ref:`|UCTR_SERNUM_CHANGE|`
     - |ENUM_SERNUM_CHANGE|
     - |UCTR_LWFW|
     - |STATE_SERNUM_CHANGE|

   * - 56
     - :rspan:`3` :cspan:`2` **GAP** – spare Control Transfer Requests –
   * - 57
   * - 58
   * - … … …

   * - :ref:`|UCTR_PIC24F_TRANSFER|`
     - |ENUM_PIC24F_TRANSFER|
     - |UCTR_LWFW_EXP|
     - |STATE_PIC24F_TRANSFER|

   * - :ref:`|UCTR_I2C_TRANSFER|`
     - |ENUM_I2C_TRANSFER|
     - |UCTR_LWFW_I2C|
     - |STATE_I2C_TRANSFER|

   * - :ref:`|UCTR_SPI_TRANSFER|`
     - |ENUM_SPI_TRANSFER|
     - |UCTR_LWFW_SPI|
     - |STATE_SPI_TRANSFER|

.. |AVRD| replace:: AVR Dude V7.0
.. |LWFW| replace:: Little Wire Firmware V1.2
.. |CAPI| replace:: Little Wire C/C++ API
.. |PYAPI| replace:: Very Little Wire Python API

.. |UCTR_USBTINY| replace:: :ref:`api:USBtiny Generic`

.. |UCTR_ECHO| replace:: 0
.. |ENUM_ECHO| replace:: :lwfw12:`ECHO <65>`
.. |LWFW_ECHO| replace:: :lwfw12:`448`
.. |CAPI_ECHO| replace:: *not available*
.. |PYAPI_ECHO| replace:: *not available*

.. |UCTR_READ| replace:: 1
.. |ENUM_READ| replace:: :lwfw12:`READ <66>`
.. |LWFW_READ| replace:: :lwfw12:`455`
.. |CAPI_READ| replace:: *not available*
.. |PYAPI_READ| replace:: *not available*

.. |UCTR_WRITE| replace:: 2
.. |ENUM_WRITE| replace:: :lwfw12:`WRITE <67>`
.. |LWFW_WRITE| replace:: :lwfw12:`461`
.. |CAPI_WRITE| replace:: *not available*
.. |PYAPI_WRITE| replace:: *not available*

.. |UCTR_CLR| replace:: 3
.. |ENUM_CLR| replace:: :lwfw12:`CLR <68>`
.. |LWFW_CLR| replace:: :lwfw12:`468`
.. |CAPI_CLR| replace:: *not available*
.. |PYAPI_CLR| replace:: *not available*

.. |UCTR_SET| replace:: 4
.. |ENUM_SET| replace:: :lwfw12:`SET <69>`
.. |LWFW_SET| replace:: :lwfw12:`473`
.. |CAPI_SET| replace:: *not available*
.. |PYAPI_SET| replace:: *not available*

.. |UCTR_USBTINY_ISPSPI| replace:: :ref:`api:USBtinyISP/SPI Programming`

.. |UCTR_POWERUP| replace:: 5
.. |ENUM_POWERUP| replace:: :lwfw12:`POWERUP <71>`
.. |LWFW_POWERUP| replace:: :lwfw12:`480`
.. |AVRD_POWERUP_1| replace:: :avrdude70:`435`
.. |AVRD_POWERUP_2| replace:: :avrdude70:`458`
.. |CAPI_POWERUP| replace:: *not available*
.. |PYAPI_POWERUP| replace:: *not available*

.. |UCTR_POWERDOWN| replace:: 6
.. |ENUM_POWERDOWN| replace:: :lwfw12:`POWERDOWN <72>`
.. |LWFW_POWERDOWN| replace:: :lwfw12:`493`
.. |AVRD_POWERDOWN| replace:: :avrdude70:`534`
.. |CAPI_POWERDOWN| replace:: *not available*
.. |PYAPI_POWERDOWN| replace:: *not available*

.. |UCTR_SPI| replace:: 7
.. |ENUM_SPI| replace:: :lwfw12:`SPI <73>`
.. |LWFW_SPI| replace:: :lwfw12:`506`
.. |AVRD_SPI_1| replace:: :avrdude70:`228`
.. |AVRD_SPI_2| replace:: :avrdude70:`243`
.. |AVRD_SPI_3| replace:: :avrdude70:`261`
.. |AVRD_SPI_4| replace:: :avrdude70:`475`
.. |AVRD_SPI_5| replace:: :avrdude70:`490`
.. |AVRD_SPI_6| replace:: :avrdude70:`546`
.. |CAPI_SPI| replace:: *not available*
.. |PYAPI_SPI| replace:: *not available*

.. |UCTR_POLL_BYTES| replace:: 8
.. |ENUM_POLL_BYTES| replace:: :lwfw12:`POLL_BYTES <74>`
.. |LWFW_POLL_BYTES| replace:: :lwfw12:`512`
.. |AVRD_POLL_BYTES| replace:: :avrdude70:`723`
.. |CAPI_POLL_BYTES| replace:: *not available*
.. |PYAPI_POLL_BYTES| replace:: *not available*

.. |UCTR_FLASH_READ| replace:: 9
.. |ENUM_FLASH_READ| replace:: :lwfw12:`FLASH_READ <75>`
.. |LWFW_FLASH_READ| replace:: :lwfw12:`519`
.. |AVRD_FLASH_READ| replace:: :avrdude70:`666`
.. |CAPI_FLASH_READ| replace:: *not available*
.. |PYAPI_FLASH_READ| replace:: *not available*

.. |UCTR_FLASH_WRITE| replace:: 10
.. |ENUM_FLASH_WRITE| replace:: :lwfw12:`FLASH_WRITE <76>`
.. |LWFW_FLASH_WRITE| replace:: :lwfw12:`530`
.. |AVRD_FLASH_WRITE| replace:: :avrdude70:`713`
.. |CAPI_FLASH_WRITE| replace:: *not available*
.. |PYAPI_FLASH_WRITE| replace:: *not available*

.. |UCTR_EEPROM_READ| replace:: 11
.. |ENUM_EEPROM_READ| replace:: :lwfw12:`EEPROM_READ <77>`
.. |LWFW_EEPROM_READ| replace:: :lwfw12:`524`
.. |AVRD_EEPROM_READ| replace:: :avrdude70:`668`
.. |CAPI_EEPROM_READ| replace:: *not available*
.. |PYAPI_EEPROM_READ| replace:: *not available*

.. |UCTR_EEPROM_WRITE| replace:: 12
.. |ENUM_EEPROM_WRITE| replace:: :lwfw12:`EEPROM_WRITE <78>`
.. |LWFW_EEPROM_WRITE| replace:: :lwfw12:`535`
.. |AVRD_EEPROM_WRITE| replace:: :avrdude70:`715`
.. |CAPI_EEPROM_WRITE| replace:: *not available*
.. |PYAPI_EEPROM_WRITE| replace:: *not available*

.. |UCTR_LWFW| replace:: :ref:`api:Little Wire Generic`

.. |UCTR_VERSION_QUERY| replace:: 34
.. |ENUM_VERSION_QUERY| replace:: :lwfw12:`VERSION_QUERY <101>`
.. |LWFW_VERSION_QUERY| replace:: :lwfw12:`672`
.. |CAPI_VERSION_QUERY| replace:: |littleWire.readFirmwareVersion|
.. |PYAPI_VERSION_QUERY| replace:: |Device.readFirmwareVersion|
.. |STATE_VERSION_QUERY| replace:: *active*

.. |littleWire.readFirmwareVersion| replace::
   :lwcapi:`littleWire::readFirmwareVersion <group__General.html#gaafb8bda520f90f80ad865909a8150ff9>`
.. |Device.readFirmwareVersion| replace::
   :py:meth:`Device.readFirmwareVersion <verylittlewire.device.Device.readFirmwareVersion>`

.. |UCTR_READ_RESULT| replace:: 40
.. |ENUM_READ_RESULT| replace:: READ_RESULT
.. |LWFW_READ_RESULT| replace:: :lwfw12:`689`
.. |CAPI_READ_RESULT_1| replace:: |littleWire.debugSpi|
.. |CAPI_READ_RESULT_2| replace:: |littleWire.spi_sendMessage|
.. |CAPI_READ_RESULT_3| replace:: |littleWire.i2c_start|
.. |CAPI_READ_RESULT_4| replace:: |littleWire.i2c_read|
.. |CAPI_READ_RESULT_5| replace:: |littleWire.onewire_resetPulse|
.. |CAPI_READ_RESULT_6| replace:: |littleWire.onewire_readByte|
.. |CAPI_READ_RESULT_7| replace:: |littleWire.onewire_readBit|
.. |PYAPI_READ_RESULT| replace:: *not yet ported*
.. |STATE_READ_RESULT| replace:: *new in V1.2*

.. |UCTR_SERNUM_CHANGE| replace:: 55
.. |ENUM_SERNUM_CHANGE| replace:: SERNUM_CHANGE
.. |LWFW_SERNUM_CHANGE| replace:: :lwfw12:`808`
.. |CAPI_SERNUM_CHANGE| replace:: |littleWire.changeSerialNumber|
.. |PYAPI_SERNUM_CHANGE| replace:: *not implemented*
.. |STATE_SERNUM_CHANGE| replace:: *new in V1.2*

.. |littleWire.changeSerialNumber| replace::
   :lwcapi:`littleWire::changeSerialNumber <group__General.html#ga790ae419d6086bf757839480df92c979>`

.. |UCTR_LWFW_GPIO| replace:: :ref:`api:Little Wire GPIO`

.. |UCTR_PIN_SET_INPUT| replace:: 13
.. |ENUM_PIN_SET_INPUT| replace:: :lwfw12:`PIN_SET_INPUT <80>`
.. |LWFW_PIN_SET_INPUT| replace:: :lwfw12:`541`
.. |CAPI_PIN_SET_INPUT| replace:: |littleWire.pinMode|
.. |PYAPI_PIN_SET_INPUT| replace:: |Device.pinMode|
.. |STATE_PIN_SET_INPUT| replace:: *active*

.. |UCTR_PIN_SET_OUTPUT| replace:: 14
.. |ENUM_PIN_SET_OUTPUT| replace:: :lwfw12:`PIN_SET_OUTPUT <81>`
.. |LWFW_PIN_SET_OUTPUT| replace:: :lwfw12:`546`
.. |CAPI_PIN_SET_OUTPUT| replace:: |littleWire.pinMode|
.. |PYAPI_PIN_SET_OUTPUT| replace:: |Device.pinMode|
.. |STATE_PIN_SET_OUTPUT| replace:: *active*

.. |littleWire.pinMode| replace::
   :lwcapi:`littleWire::pinMode <group__GPIO.html#ga3d9d42ba638ea905365245113afbafef>`
.. |Device.pinMode| replace::
   :py:meth:`Device.pinMode <verylittlewire.device.Device.pinMode>`

.. |UCTR_PIN_SET_HIGH| replace:: 18
.. |ENUM_PIN_SET_HIGH| replace:: :lwfw12:`PIN_SET_HIGH <85>`
.. |LWFW_PIN_SET_HIGH| replace:: :lwfw12:`595`
.. |CAPI_PIN_SET_HIGH_1| replace:: |littleWire.digitalWrite|
.. |CAPI_PIN_SET_HIGH_2| replace:: |littleWire.internalPullup|
.. |PYAPI_PIN_SET_HIGH_1| replace:: |Device.digitalWrite|
.. |PYAPI_PIN_SET_HIGH_2| replace:: |Device.internalPullup|
.. |STATE_PIN_SET_HIGH| replace:: *active*

.. |UCTR_PIN_SET_LOW| replace:: 19
.. |ENUM_PIN_SET_LOW| replace:: :lwfw12:`PIN_SET_LOW <86>`
.. |LWFW_PIN_SET_LOW| replace:: :lwfw12:`600`
.. |CAPI_PIN_SET_LOW_1| replace:: |littleWire.digitalWrite|
.. |CAPI_PIN_SET_LOW_2| replace:: |littleWire.internalPullup|
.. |PYAPI_PIN_SET_LOW_1| replace:: |Device.digitalWrite|
.. |PYAPI_PIN_SET_LOW_2| replace:: |Device.internalPullup|
.. |STATE_PIN_SET_LOW| replace:: *active*

.. |littleWire.digitalWrite| replace::
   :lwcapi:`littleWire::digitalWrite <group__GPIO.html#gabd74ae5f01abb097e9bd627b1748b6b8>`
.. |Device.digitalWrite| replace::
   :py:meth:`Device.digitalWrite <verylittlewire.device.Device.digitalWrite>`
.. |littleWire.internalPullup| replace::
   :lwcapi:`littleWire::internalPullup <group__GPIO.html#ga78336c4bb697bd80c8fd6ba444357120>`
.. |Device.internalPullup| replace::
   :py:meth:`Device.internalPullup <verylittlewire.device.Device.internalPullup>`

.. |UCTR_PIN_READ| replace:: 20
.. |ENUM_PIN_READ| replace:: :lwfw12:`PIN_READ <87>`
.. |LWFW_PIN_READ| replace:: :lwfw12:`605`
.. |CAPI_PIN_READ| replace:: |littleWire.digitalRead|
.. |PYAPI_PIN_READ| replace:: |Device.digitalRead|
.. |STATE_PIN_READ| replace:: *active*

.. |littleWire.digitalRead| replace::
   :lwcapi:`littleWire::digitalRead <group__GPIO.html#ga41d3beeed6ef88158cd1c156a7fc8ef7>`
.. |Device.digitalRead| replace::
   :py:meth:`Device.digitalRead <verylittlewire.device.Device.digitalRead>`

.. |UCTR_LWFW_ADC| replace:: :ref:`api:Little Wire ADC`

.. |UCTR_SETUP_ADC| replace:: 35
.. |ENUM_SETUP_ADC| replace:: SETUP_ADC
.. |LWFW_SETUP_ADC| replace:: :lwfw12:`670`
.. |CAPI_SETUP_ADC| replace:: |littleWire.analog_init|
.. |PYAPI_SETUP_ADC| replace:: |Device.analogInit|
.. |STATE_SETUP_ADC| replace:: *new in V1.2*

.. |littleWire.analog_init| replace::
   :lwcapi:`littleWire::analog_init <group__ADC.html#gacf9d5c0c4f230eac945f97691c82f599>`
.. |Device.analogInit| replace::
   :py:meth:`Device.analogInit <verylittlewire.device.Device.analogInit>`

.. |UCTR_READ_ADC| replace:: 15
.. |ENUM_READ_ADC| replace:: :lwfw12:`READ_ADC <82>`
.. |LWFW_READ_ADC| replace:: :lwfw12:`551`
.. |CAPI_READ_ADC| replace:: |littleWire.analogRead|
.. |PYAPI_READ_ADC| replace:: |Device.analogRead|
.. |STATE_READ_ADC| replace:: *active*

.. |littleWire.analogRead| replace::
   :lwcapi:`littleWire::analogRead <group__ADC.html#gaa644fc71be28e975bf5732bf610e81b9>`
.. |Device.analogRead| replace::
   :py:meth:`Device.analogRead <verylittlewire.device.Device.analogRead>`

.. |UCTR_LWFW_PWM| replace:: :ref:`api:Little Wire PWM`

.. |UCTR_SETUP_PWM| replace:: 16
.. |ENUM_SETUP_PWM| replace:: :lwfw12:`SETUP_PWM <83>`
.. |LWFW_SETUP_PWM| replace:: :lwfw12:`580`
.. |CAPI_SETUP_PWM| replace:: |littleWire.pwm_init|
.. |PYAPI_SETUP_PWM| replace:: |Device.pwmInit|
.. |STATE_SETUP_PWM| replace:: *active*

.. |littleWire.pwm_init| replace::
   :lwcapi:`littleWire::pwm_init <group__PWM.html#ga4a070a716f10a3e89221d9c4f39b55ff>`
.. |Device.pwmInit| replace::
   :py:meth:`Device.pwmInit <verylittlewire.device.Device.pwmInit>`

.. |UCTR_UPDATE_PWM_COMPARE| replace:: 17
.. |ENUM_UPDATE_PWM_COMPARE| replace:: :lwfw12:`UPDATE_PWM_COMPARE <84>`
.. |LWFW_UPDATE_PWM_COMPARE| replace:: :lwfw12:`589`
.. |CAPI_UPDATE_PWM_COMPARE| replace:: |littleWire.pwm_updateCompare|
.. |PYAPI_UPDATE_PWM_COMPARE| replace:: |Device.pwmUpdateCompare|
.. |STATE_UPDATE_PWM_COMPARE| replace:: *active*

.. |littleWire.pwm_updateCompare| replace::
   :lwcapi:`littleWire::pwm_updateCompare <group__PWM.html#ga28b543e97edce467978dd57fd8dc66a8>`
.. |Device.pwmUpdateCompare| replace::
   :py:meth:`Device.pwmUpdateCompare <verylittlewire.device.Device.pwmUpdateCompare>`

.. |UCTR_CHANGE_PWM_PRESCALE| replace:: 22
.. |ENUM_CHANGE_PWM_PRESCALE| replace:: :lwfw12:`CHANGE_PWM_PRESCALE <89>`
.. |LWFW_CHANGE_PWM_PRESCALE| replace:: :lwfw12:`612`
.. |CAPI_CHANGE_PWM_PRESCALE| replace:: |littleWire.pwm_updatePrescaler|
.. |PYAPI_CHANGE_PWM_PRESCALE| replace:: |Device.pwmUpdatePrescaler|
.. |STATE_CHANGE_PWM_PRESCALE| replace:: *active*

.. |littleWire.pwm_updatePrescaler| replace::
   :lwcapi:`littleWire::pwm_updatePrescaler <group__PWM.html#gab7a85b4c3b9bab80018a0fda400346fd>`
.. |Device.pwmUpdatePrescaler| replace::
   :py:meth:`Device.pwmUpdatePrescaler <verylittlewire.device.Device.pwmUpdatePrescaler>`

.. |UCTR_STOP_PWM| replace:: 32
.. |ENUM_STOP_PWM| replace:: :lwfw12:`STOP_PWM <99>`
.. |LWFW_STOP_PWM| replace:: :lwfw12:`652`
.. |CAPI_STOP_PWM| replace:: |littleWire.pwm_stop|
.. |PYAPI_STOP_PWM| replace:: |Device.pwmStop|
.. |STATE_STOP_PWM| replace:: *active*

.. |littleWire.pwm_stop| replace::
   :lwcapi:`littleWire::pwm_stop <group__PWM.html#ga83bff9c8bfca1ea5ef21ed6b9616bc42>`
.. |Device.pwmStop| replace::
   :py:meth:`Device.pwmStop <verylittlewire.device.Device.pwmStop>`

.. |UCTR_LWFW_SPI| replace:: :ref:`api:Little Wire SPI`

.. |UCTR_SINGLE_SPI| replace:: 21
.. |ENUM_SINGLE_SPI| replace:: :lwfw12:`SINGLE_SPI <88>`
.. |LWFW_SINGLE_SPI| replace:: *not available*
.. |CAPI_SINGLE_SPI| replace:: *not available*
.. |PYAPI_SINGLE_SPI| replace:: *not available*
.. |STATE_SINGLE_SPI| replace:: *obsolete with V1.2*

.. |UCTR_SETUP_SPI| replace:: 23
.. |ENUM_SETUP_SPI| replace:: :lwfw12:`SETUP_SPI <90>`
.. |LWFW_SETUP_SPI| replace:: *not needed anymore*
.. |CAPI_SETUP_SPI| replace:: |littleWire.spi_init|
.. |PYAPI_SETUP_SPI| replace:: *not available*
.. |STATE_SETUP_SPI| replace:: *accepted*

.. |littleWire.spi_init| replace::
   :lwcapi:`littleWire::spi_init <group__SPI.html#ga8972ae84f46f4d109fee83ef7a06afad>`

.. |UCTR_SPI_ADD_BUFFER| replace:: 28
.. |ENUM_SPI_ADD_BUFFER| replace:: :lwfw12:`SPI_ADD_BUFFER <95>`
.. |LWFW_SPI_ADD_BUFFER| replace:: *not available*
.. |CAPI_SPI_ADD_BUFFER| replace:: *not available*
.. |PYAPI_SPI_ADD_BUFFER| replace:: *not available*
.. |STATE_SPI_ADD_BUFFER| replace:: *obsolete with V1.2*

.. |UCTR_SPI_SEND_BUFFER| replace:: 29
.. |ENUM_SPI_SEND_BUFFER| replace:: :lwfw12:`SPI_SEND_BUFFER <96>`
.. |LWFW_SPI_SEND_BUFFER| replace:: *not available*
.. |CAPI_SPI_SEND_BUFFER| replace:: *not available*
.. |PYAPI_SPI_SEND_BUFFER| replace:: *not available*
.. |STATE_SPI_SEND_BUFFER| replace:: *obsolete with V1.2*

.. |UCTR_SPI_UPDATE_DELAY| replace:: 31
.. |ENUM_SPI_UPDATE_DELAY| replace:: :lwfw12:`SPI_UPDATE_DELAY <98>`
.. |LWFW_SPI_UPDATE_DELAY| replace:: :lwfw12:`647`
.. |CAPI_SPI_UPDATE_DELAY| replace:: |littleWire.spi_updateDelay|
.. |PYAPI_SPI_UPDATE_DELAY| replace:: *not yet ported*
.. |STATE_SPI_UPDATE_DELAY| replace:: *active*

.. |littleWire.spi_updateDelay| replace::
   :lwcapi:`littleWire::spi_updateDelay <group__SPI.html#ga77fc1ca40b5336a2855bde16a1082f6c>`

.. |UCTR_DEBUG_SPI| replace:: 33
.. |ENUM_DEBUG_SPI| replace:: :lwfw12:`DEBUG_SPI <100>`
.. |LWFW_DEBUG_SPI| replace:: :lwfw12:`658`
.. |CAPI_DEBUG_SPI| replace:: |littleWire.debugSpi|
.. |PYAPI_DEBUG_SPI| replace:: *not yet ported*
.. |STATE_DEBUG_SPI| replace:: *active*

.. |littleWire.debugSpi| replace::
   :lwcapi:`littleWire::debugSpi <group__SPI.html#gacd555aed378114c940468a2d529466d9>`

.. |UCTR_SPI_TRANSFER| replace:: 0xFx
.. |ENUM_SPI_TRANSFER| replace:: SPI_TRANSFER
.. |LWFW_SPI_TRANSFER| replace:: :lwfw12:`848`
.. |CAPI_SPI_TRANSFER| replace:: |littleWire.spi_sendMessage|
.. |PYAPI_SPI_TRANSFER| replace:: *not yet ported*
.. |STATE_SPI_TRANSFER| replace:: *active*

.. |littleWire.spi_sendMessage| replace::
   :lwcapi:`littleWire::spi_sendMessage <group__SPI.html#gac30a17fa6b874ba0635d0e36bc02337f>`

.. |UCTR_LWFW_I2C| replace:: :ref:`api:Little Wire I²C`

.. |UCTR_SETUP_I2C| replace:: 24
.. |ENUM_SETUP_I2C| replace:: :lwfw12:`SETUP_I2C <91>`
.. |LWFW_SETUP_I2C| replace:: *not available*
.. |CAPI_SETUP_I2C| replace:: *not available*
.. |PYAPI_SETUP_I2C| replace:: *not available*
.. |STATE_SETUP_I2C| replace:: *obsolete with V1.2*

.. |UCTR_I2C_BEGIN_TX| replace:: 25
.. |ENUM_I2C_BEGIN_TX| replace:: :lwfw12:`I2C_BEGIN_TX <92>`
.. |LWFW_I2C_BEGIN_TX| replace:: *not available*
.. |CAPI_I2C_BEGIN_TX| replace:: *not available*
.. |PYAPI_I2C_BEGIN_TX| replace:: *not available*
.. |STATE_I2C_BEGIN_TX| replace:: *obsolete with V1.2*

.. |UCTR_I2C_ADD_BUFFER| replace:: 26
.. |ENUM_I2C_ADD_BUFFER| replace:: :lwfw12:`I2C_ADD_BUFFER <93>`
.. |LWFW_I2C_ADD_BUFFER| replace:: *not available*
.. |CAPI_I2C_ADD_BUFFER| replace:: *not available*
.. |PYAPI_I2C_ADD_BUFFER| replace:: *not available*
.. |STATE_I2C_ADD_BUFFER| replace:: *obsolete with V1.2*

.. |UCTR_I2C_SEND_BUFFER| replace:: 27
.. |ENUM_I2C_SEND_BUFFER| replace:: :lwfw12:`I2C_SEND_BUFFER <94>`
.. |LWFW_I2C_SEND_BUFFER| replace:: *not available*
.. |CAPI_I2C_SEND_BUFFER| replace:: *not available*
.. |PYAPI_I2C_SEND_BUFFER| replace:: *not available*
.. |STATE_I2C_SEND_BUFFER| replace:: *obsolete with V1.2*

.. |UCTR_I2C_REQUEST_FROM| replace:: 30
.. |ENUM_I2C_REQUEST_FROM| replace:: :lwfw12:`I2C_REQUEST_FROM <97>`
.. |LWFW_I2C_REQUEST_FROM| replace:: *not available*
.. |CAPI_I2C_REQUEST_FROM| replace:: *not available*
.. |PYAPI_I2C_REQUEST_FROM| replace:: *not available*
.. |STATE_I2C_REQUEST_FROM| replace:: *obsolete with V1.2*

.. |UCTR_I2C_INIT| replace:: 44
.. |ENUM_I2C_INIT| replace:: I2C_INIT
.. |LWFW_I2C_INIT| replace:: :lwfw12:`710`
.. |CAPI_I2C_INIT| replace:: |littleWire.i2c_init|
.. |PYAPI_I2C_INIT| replace:: *not yet ported*
.. |STATE_I2C_INIT| replace:: *new in V1.2*

.. |littleWire.i2c_init| replace::
   :lwcapi:`littleWire::i2c_init <group__I2C.html#ga88584118e5b0ccd7330bb092235c4e73>`

.. |UCTR_I2C_START| replace:: 45
.. |ENUM_I2C_START| replace:: I2C_START
.. |LWFW_I2C_START| replace:: :lwfw12:`715`
.. |CAPI_I2C_START| replace:: |littleWire.i2c_start|
.. |PYAPI_I2C_START| replace:: *not yet ported*
.. |STATE_I2C_START| replace:: *new in V1.2*

.. |littleWire.i2c_start| replace::
   :lwcapi:`littleWire::i2c_start <group__I2C.html#ga4cf5bd085f03b27b9ae80d10bfec50b1>`

.. |UCTR_I2C_READ| replace:: 46
.. |ENUM_I2C_READ| replace:: I2C_READ
.. |LWFW_I2C_READ| replace:: :lwfw12:`721`
.. |CAPI_I2C_READ| replace:: |littleWire.i2c_read|
.. |PYAPI_I2C_READ| replace:: *not yet ported*
.. |STATE_I2C_READ| replace:: *new in V1.2*

.. |littleWire.i2c_read| replace::
   :lwcapi:`littleWire::i2c_read <group__I2C.html#ga5c3a23af7577b89b67cb62d9e192938c>`

.. |UCTR_I2C_UPDATE_DELAY| replace:: 49
.. |ENUM_I2C_UPDATE_DELAY| replace:: I2C_UPDATE_DELAY
.. |LWFW_I2C_UPDATE_DELAY| replace:: :lwfw12:`749`
.. |CAPI_I2C_UPDATE_DELAY| replace:: |littleWire.i2c_updateDelay|
.. |PYAPI_I2C_UPDATE_DELAY| replace:: *not yet ported*
.. |STATE_I2C_UPDATE_DELAY| replace:: *new in V1.2*

.. |littleWire.i2c_updateDelay| replace::
   :lwcapi:`littleWire::i2c_updateDelay <group__I2C.html#ga29e1be10e6e628f8ad0a4a27da868a81>`

.. |UCTR_I2C_TRANSFER| replace:: 0xEx
.. |ENUM_I2C_TRANSFER| replace:: I2C_TRANSFER
.. |LWFW_I2C_TRANSFER| replace:: :lwfw12:`836`
.. |CAPI_I2C_TRANSFER| replace:: |littleWire.i2c_write|
.. |PYAPI_I2C_TRANSFER| replace:: *not yet ported*
.. |STATE_I2C_TRANSFER| replace:: *new in V1.2*

.. |littleWire.i2c_write| replace::
   :lwcapi:`littleWire::i2c_write <group__I2C.html#ga9f47567fc7fb0ae1a32b62c7cb228c4c>`

.. |UCTR_LWFW_SOFT_PWM| replace:: :ref:`api:Little Wire Soft-PWM`

.. |UCTR_SOFT_PWM_INIT| replace:: 47
.. |ENUM_SOFT_PWM_INIT| replace:: SOFT_PWM_INIT
.. |LWFW_SOFT_PWM_INIT| replace:: :lwfw12:`742`
.. |CAPI_SOFT_PWM_INIT| replace:: |littleWire.softPWM_state|
.. |PYAPI_SOFT_PWM_INIT| replace:: *not yet ported*
.. |STATE_SOFT_PWM_INIT| replace:: *new in V1.2*

.. |littleWire.softPWM_state| replace::
   :lwcapi:`littleWire::softPWM_state <group__SOFT__PWM.html#ga2195c36e8a0a1a8e5fd980e368e92d19>`

.. |UCTR_SOFT_PWM_UPDATE| replace:: 48
.. |ENUM_SOFT_PWM_UPDATE| replace:: SOFT_PWM_UPDATE
.. |LWFW_SOFT_PWM_UPDATE| replace:: :lwfw12:`729`
.. |CAPI_SOFT_PWM_UPDATE| replace:: |littleWire.softPWM_write|
.. |PYAPI_SOFT_PWM_UPDATE| replace:: *not yet ported*
.. |STATE_SOFT_PWM_UPDATE| replace:: *new in V1.2*

.. |littleWire.softPWM_write| replace::
   :lwcapi:`littleWire::softPWM_write <group__SOFT__PWM.html#gafc22bfeff36ddf9e916cb650142a875a>`

.. |UCTR_LWFW_OW| replace:: :ref:`api:Little Wire One-Wire`

.. |UCTR_OW_RESET_PULSE| replace:: 41
.. |ENUM_OW_RESET_PULSE| replace:: OW_RESET_PULSE
.. |LWFW_OW_RESET_PULSE| replace:: :lwfw12:`694`
.. |CAPI_OW_RESET_PULSE| replace:: |littleWire.onewire_resetPulse|
.. |PYAPI_OW_RESET_PULSE| replace:: *not yet ported*
.. |STATE_OW_RESET_PULSE| replace:: *new in V1.2*

.. |littleWire.onewire_resetPulse| replace::
   :lwcapi:`littleWire::onewire_resetPulse <group__Onewire.html#ga1da45189d08a3c6e030a53c0f936cb0a>`

.. |UCTR_OW_WRITE_BYTE| replace:: 42
.. |ENUM_OW_WRITE_BYTE| replace:: OW_WRITE_BYTE
.. |LWFW_OW_WRITE_BYTE| replace:: :lwfw12:`699`
.. |CAPI_OW_WRITE_BYTE| replace:: |littleWire.onewire_writeByte|
.. |PYAPI_OW_WRITE_BYTE| replace:: *not yet ported*
.. |STATE_OW_WRITE_BYTE| replace:: *new in V1.2*

.. |littleWire.onewire_writeByte| replace::
   :lwcapi:`littleWire::onewire_writeByte <group__Onewire.html#ga97530a60cae61320e5a9cd87788b97ef>`

.. |UCTR_OW_READ_BYTE| replace:: 43
.. |ENUM_OW_READ_BYTE| replace:: OW_READ_BYTE
.. |LWFW_OW_READ_BYTE| replace:: :lwfw12:`705`
.. |CAPI_OW_READ_BYTE| replace:: |littleWire.onewire_readByte|
.. |PYAPI_OW_READ_BYTE| replace:: *not yet ported*
.. |STATE_OW_READ_BYTE| replace:: *new in V1.2*

.. |littleWire.onewire_readByte| replace::
   :lwcapi:`littleWire::onewire_readByte <group__Onewire.html#ga8056dd5d6ee015abfdf10d0b1533c2c5>`

.. |UCTR_OW_READ_BIT| replace:: 50
.. |ENUM_OW_READ_BIT| replace:: OW_READ_BIT
.. |LWFW_OW_READ_BIT| replace:: :lwfw12:`754`
.. |CAPI_OW_READ_BIT| replace:: |littleWire.onewire_readBit|
.. |PYAPI_OW_READ_BIT| replace:: *not yet ported*
.. |STATE_OW_READ_BIT| replace:: *new in V1.2*

.. |littleWire.onewire_readBit| replace::
   :lwcapi:`littleWire::onewire_readBit <group__Onewire.html#ga7d6330de45dfa5527a48813a7d7ab4f3>`

.. |UCTR_OW_WRITE_BIT| replace:: 51
.. |ENUM_OW_WRITE_BIT| replace:: OW_WRITE_BIT
.. |LWFW_OW_WRITE_BIT| replace:: :lwfw12:`759`
.. |CAPI_OW_WRITE_BIT| replace:: |littleWire.onewire_sendBit|
.. |PYAPI_OW_WRITE_BIT| replace:: *not yet ported*
.. |STATE_OW_WRITE_BIT| replace:: *new in V1.2*

.. |littleWire.onewire_sendBit| replace::
   :lwcapi:`littleWire::onewire_sendBit <group__Onewire.html#gad9a7968da3c0e6a22c93a2f861f56308>`

.. |UCTR_LWFW_WS2812| replace:: :ref:`api:Little Wire WS2812`

.. |UCTR_WS2812_EXEC| replace:: 54
.. |ENUM_WS2812_EXEC| replace:: WS2812_EXEC
.. |LWFW_WS2812_EXEC| replace:: :lwfw12:`786`
.. |CAPI_WS2812_EXEC_1| replace:: |littleWire.ws2812_flush|
.. |CAPI_WS2812_EXEC_2| replace:: |littleWire.ws2812_preload|
.. |CAPI_WS2812_EXEC_3| replace:: |littleWire.ws2812_write|
.. |PYAPI_WS2812_EXEC| replace:: *not yet ported*
.. |STATE_WS2812_EXEC| replace:: *new in V1.2*

.. |littleWire.ws2812_flush| replace::
   :lwcapi:`littleWire::ws2812_flush <group__WS2812.html#ga798699b963dd977184343ef1af3a1657>`
.. |littleWire.ws2812_preload| replace::
   :lwcapi:`littleWire::ws2812_preload <group__WS2812.html#ga27675acf1b16a2e0bb00de3cd9054065>`
.. |littleWire.ws2812_write| replace::
   :lwcapi:`littleWire::ws2812_write <group__WS2812.html#ga5928ec0807212de630389bbb2d5db7ae>`

.. |UCTR_LWFW_EXP| replace:: :ref:`api:Little Wire Experimental`

.. |UCTR_PIC24F_PROG| replace:: 52
.. |ENUM_PIC24F_PROG| replace:: PIC24F_PROG
.. |LWFW_PIC24F_PROG| replace:: :lwfw12:`766`
.. |CAPI_PIC24F_PROG| replace:: *not available*
.. |PYAPI_PIC24F_PROG| replace:: *not available*
.. |STATE_PIC24F_PROG| replace:: *experimental in V1.2*

.. |UCTR_PIC24F_SENDSIX| replace:: 53
.. |ENUM_PIC24F_SENDSIX| replace:: PIC24F_SENDSIX
.. |LWFW_PIC24F_SENDSIX| replace:: :lwfw12:`774`
.. |CAPI_PIC24F_SENDSIX| replace:: *not available*
.. |PYAPI_PIC24F_SENDSIX| replace:: *not available*
.. |STATE_PIC24F_SENDSIX| replace:: *experimental in V1.2*

.. |UCTR_PIC24F_TRANSFER| replace:: 0xDx
.. |ENUM_PIC24F_TRANSFER| replace:: PIC24F_TRANSFER
.. |LWFW_PIC24F_TRANSFER| replace:: :lwfw12:`836`
.. |CAPI_PIC24F_TRANSFER| replace:: *not available*
.. |PYAPI_PIC24F_TRANSFER| replace:: *not available*
.. |STATE_PIC24F_TRANSFER| replace:: *experimental in V1.2*

USBtiny Generic
```````````````

.. flat-table:: Little Wire Firmware USBtiny Generic Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-usbtiny

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_ECHO|:

       .. rubric:: |UCTR_ECHO|

     - :cspan:`1` |ENUM_ECHO|
     - :rspan:`1` echo all content in **Data Stage** back to host
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: ECHO
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_ECHO| – :code:`bRequest` changed hard to :code:`0x21` in response

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_ECHO|

       .. rubric:: |PYAPI|

       * |PYAPI_ECHO|



   * - :rspan:`1`

       .. _|UCTR_READ|:

       .. rubric:: |UCTR_READ|

     - :cspan:`1` |ENUM_READ|
     - :rspan:`1` read :token:`READ:value` from memory :token:`READ:address`
   * - .. wValue not used
     - :token:`READ:address`
   * - :cspan:`1`
     - .. productionlist:: READ
          OUTPUT: `value`
          INPUT: `address`
          value: (uint8)0…0xFF
          address: (uint16)0…0xFFFF
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_READ| – ignores :token:`READ:address`, uses the I/O port instead

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_READ|

       .. rubric:: |PYAPI|

       * |PYAPI_READ|



   * - :rspan:`1`

       .. _|UCTR_WRITE|:

       .. rubric:: |UCTR_WRITE|

     - :cspan:`1` |ENUM_WRITE|
     - :rspan:`1` write :token:`WRITE:value` to memory :token:`WRITE:address`
   * - :token:`WRITE:value`
     - :token:`WRITE:address`
   * - :cspan:`1`
     - .. productionlist:: WRITE
          OUTPUT:
          INPUT: `address` & `value`
          value: (uint8)0…0xFF
          address: (uint16)0…0xFFFF
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_WRITE| – ignores :token:`WRITE:address`, uses the I/O port instead

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_WRITE|

       .. rubric:: |PYAPI|

       * |PYAPI_WRITE|



   * - :rspan:`1`

       .. _|UCTR_CLR|:

       .. rubric:: |UCTR_CLR|

     - :cspan:`1` |ENUM_CLR|
     - :rspan:`1` clear bit :token:`CLR:bitno` on memory :token:`CLR:address`
   * - :token:`CLR:bitno`
     - :token:`CLR:address`
   * - :cspan:`1`
     - .. productionlist:: CLR
          OUTPUT:
          INPUT: `address` & `bitno`
          bitno: (uint8)0…7
          address: (uint16)0…0xFFFF
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_CLR| – ignores :token:`CLR:address`, uses the I/O port instead

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_CLR|

       .. rubric:: |PYAPI|

       * |PYAPI_CLR|



   * - :rspan:`1`

       .. _|UCTR_SET|:

       .. rubric:: |UCTR_SET|

     - :cspan:`1` |ENUM_SET|
     - :rspan:`1` set bit :token:`SET:bitno` on memory :token:`SET:address`
   * - :token:`SET:bitno`
     - :token:`SET:address`
   * - :cspan:`1`
     - .. productionlist:: SET
          OUTPUT:
          INPUT: `address` & `bitno`
          bitno: (uint8)0…7
          address: (uint16)0…0xFFFF
   * - :cspan:`1` Implementation
     - .. rubric:: Firmware

       * |LWFW_SET| – ignores :token:`SET:address`, uses the I/O port instead

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SET|

       .. rubric:: |PYAPI|

       * |PYAPI_SET|



USBtinyISP/SPI Programming
``````````````````````````

.. flat-table:: Little Wire Firmware USBtiny Generic Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-usbtiny-isbspi

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_POWERUP|:

       .. rubric:: |UCTR_POWERUP|

     - :cspan:`1` |ENUM_POWERUP|
     - :rspan:`1`
   * - :token:`POWERUP:period`
     - :token:`POWERUP:reset`
   * - :cspan:`1`
     - .. productionlist:: POWERUP
          OUTPUT:
          INPUT: `period` & `reset`
          period:
          reset:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_POWERUP|

       .. rubric:: |AVRD|

       * |AVRD_POWERUP_1|
       * |AVRD_POWERUP_2|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_POWERUP|

       .. rubric:: |PYAPI|

       * |PYAPI_POWERUP|



   * - :rspan:`1`

       .. _|UCTR_POWERDOWN|:

       .. rubric:: |UCTR_POWERDOWN|

     - :cspan:`1` |ENUM_POWERDOWN|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: POWERDOWN
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_POWERDOWN|

       .. rubric:: |AVRD|

       * |AVRD_POWERDOWN|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_POWERDOWN|

       .. rubric:: |PYAPI|

       * |PYAPI_POWERDOWN|



   * - :rspan:`1`

       .. _|UCTR_SPI|:

       .. rubric:: |UCTR_SPI|

     - :cspan:`1` |ENUM_SPI|
     - :rspan:`1`
   * - :token:`SPI:c1c0`
     - :token:`SPI:c3c2`
   * - :cspan:`1`
     - .. productionlist:: SPI
          OUTPUT:
          INPUT: `c1c0` & `c3c2`
          c1c0:
          c3c2:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_SPI|

       .. rubric:: |AVRD|

       * |AVRD_SPI_1|
       * |AVRD_SPI_2|
       * |AVRD_SPI_3|
       * |AVRD_SPI_4|
       * |AVRD_SPI_5|
       * |AVRD_SPI_6|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SPI|

       .. rubric:: |PYAPI|

       * |PYAPI_SPI|



   * - :rspan:`1`

       .. _|UCTR_POLL_BYTES|:

       .. rubric:: |UCTR_POLL_BYTES|

     - :cspan:`1` |ENUM_POLL_BYTES|
     - :rspan:`1`
   * - :token:`POLL_BYTES:p1p2`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: POLL_BYTES
          OUTPUT:
          INPUT: `p1p2`
          p1p2:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_POLL_BYTES|

       .. rubric:: |AVRD|

       * |AVRD_POLL_BYTES|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_POLL_BYTES|

       .. rubric:: |PYAPI|

       * |PYAPI_POLL_BYTES|



   * - :rspan:`1`

       .. _|UCTR_FLASH_READ|:

       .. rubric:: |UCTR_FLASH_READ|

     - :cspan:`1` |ENUM_FLASH_READ|
     - :rspan:`1`
   * - .. wValue not used
     - :token:`FLASH_READ:address`
   * - :cspan:`1`
     - .. productionlist:: FLASH_READ
          OUTPUT:
          INPUT: `address`
          address:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_FLASH_READ|

       .. rubric:: |AVRD|

       * |AVRD_FLASH_READ|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_FLASH_READ|

       .. rubric:: |PYAPI|

       * |PYAPI_FLASH_READ|



   * - :rspan:`1`

       .. _|UCTR_FLASH_WRITE|:

       .. rubric:: |UCTR_FLASH_WRITE|

     - :cspan:`1` |ENUM_FLASH_WRITE|
     - :rspan:`1`
   * - :token:`FLASH_WRITE:timeout`
     - :token:`FLASH_WRITE:address`
   * - :cspan:`1`
     - .. productionlist:: FLASH_WRITE
          OUTPUT:
          INPUT: `timeout` & `address`
          timeout:
          address:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_FLASH_WRITE|

       .. rubric:: |AVRD|

       * |AVRD_FLASH_WRITE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_FLASH_WRITE|

       .. rubric:: |PYAPI|

       * |PYAPI_FLASH_WRITE|



   * - :rspan:`1`

       .. _|UCTR_EEPROM_READ|:

       .. rubric:: |UCTR_EEPROM_READ|

     - :cspan:`1` |ENUM_EEPROM_READ|
     - :rspan:`1`
   * - .. wValue not used
     - :token:`EEPROM_READ:address`
   * - :cspan:`1`
     - .. productionlist:: EEPROM_READ
          OUTPUT:
          INPUT: `address`
          address:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_EEPROM_READ|

       .. rubric:: |AVRD|

       * |AVRD_EEPROM_READ|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_EEPROM_READ|

       .. rubric:: |PYAPI|

       * |PYAPI_EEPROM_READ|



   * - :rspan:`1`

       .. _|UCTR_EEPROM_WRITE|:

       .. rubric:: |UCTR_EEPROM_WRITE|

     - :cspan:`1` |ENUM_EEPROM_WRITE|
     - :rspan:`1`
   * - :token:`EEPROM_WRITE:timeout`
     - :token:`EEPROM_WRITE:address`
   * - :cspan:`1`
     - .. productionlist:: EEPROM_WRITE
          OUTPUT:
          INPUT: `timeout` & `address`
          timeout:
          address:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW|

       * |LWFW_EEPROM_WRITE|

       .. rubric:: |AVRD|

       * |AVRD_EEPROM_WRITE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_EEPROM_WRITE|

       .. rubric:: |PYAPI|

       * |PYAPI_EEPROM_WRITE|



Little Wire Generic
```````````````````

.. flat-table:: Little Wire Firmware Generic Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_VERSION_QUERY|:

       .. rubric:: |UCTR_VERSION_QUERY|

     - :cspan:`1` |ENUM_VERSION_QUERY|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: VERSION_QUERY
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_VERSION_QUERY|

       * |LWFW_VERSION_QUERY|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_VERSION_QUERY|

       .. rubric:: |PYAPI|

       * |PYAPI_VERSION_QUERY|



   * - :rspan:`1`

       .. _|UCTR_READ_RESULT|:

       .. rubric:: |UCTR_READ_RESULT|

     - :cspan:`1` |ENUM_READ_RESULT|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: READ_RESULT
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_READ_RESULT|

       * |LWFW_READ_RESULT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_READ_RESULT_1|
       * |CAPI_READ_RESULT_2|
       * |CAPI_READ_RESULT_3|
       * |CAPI_READ_RESULT_4|
       * |CAPI_READ_RESULT_5|
       * |CAPI_READ_RESULT_6|
       * |CAPI_READ_RESULT_7|

       .. rubric:: |PYAPI|

       * |PYAPI_READ_RESULT|



   * - :rspan:`1`

       .. _|UCTR_SERNUM_CHANGE|:

       .. rubric:: |UCTR_SERNUM_CHANGE|

     - :cspan:`1` |ENUM_SERNUM_CHANGE|
     - :rspan:`1`
   * - :token:`SERNUM_CHANGE:snb1snb0`
     - :token:`SERNUM_CHANGE:snb2`
   * - :cspan:`1`
     - .. productionlist:: SERNUM_CHANGE
          OUTPUT:
          INPUT: `snb1snb0` & `snb2`
          snb1snb0:
          snb2:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SERNUM_CHANGE|

       * |LWFW_SERNUM_CHANGE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SERNUM_CHANGE|

       .. rubric:: |PYAPI|

       * |PYAPI_SERNUM_CHANGE|



Little Wire GPIO
````````````````

.. flat-table:: Little Wire Firmware GPIO Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-gpio

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_PIN_SET_INPUT|:

       .. rubric:: |UCTR_PIN_SET_INPUT|

     - :cspan:`1` |ENUM_PIN_SET_INPUT|
     - :rspan:`1`
   * - :token:`PIN_SET_INPUT:pin`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: PIN_SET_INPUT
          OUTPUT:
          INPUT: `pin`
          pin:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIN_SET_INPUT|

       * |LWFW_PIN_SET_INPUT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIN_SET_INPUT|

       .. rubric:: |PYAPI|

       * |PYAPI_PIN_SET_INPUT|



   * - :rspan:`1`

       .. _|UCTR_PIN_SET_OUTPUT|:

       .. rubric:: |UCTR_PIN_SET_OUTPUT|

     - :cspan:`1` |ENUM_PIN_SET_OUTPUT|
     - :rspan:`1`
   * - :token:`PIN_SET_OUTPUT:pin`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: PIN_SET_OUTPUT
          OUTPUT:
          INPUT: `pin`
          pin:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIN_SET_OUTPUT|

       * |LWFW_PIN_SET_OUTPUT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIN_SET_OUTPUT|

       .. rubric:: |PYAPI|

       * |PYAPI_PIN_SET_OUTPUT|



   * - :rspan:`1`

       .. _|UCTR_PIN_SET_HIGH|:

       .. rubric:: |UCTR_PIN_SET_HIGH|

     - :cspan:`1` |ENUM_PIN_SET_HIGH|
     - :rspan:`1`
   * - :token:`PIN_SET_HIGH:pin`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: PIN_SET_HIGH
          OUTPUT:
          INPUT: `pin`
          pin:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIN_SET_HIGH|

       * |LWFW_PIN_SET_HIGH|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIN_SET_HIGH_1|
       * |CAPI_PIN_SET_HIGH_2|

       .. rubric:: |PYAPI|

       * |PYAPI_PIN_SET_HIGH_1|
       * |PYAPI_PIN_SET_HIGH_2|



   * - :rspan:`1`

       .. _|UCTR_PIN_SET_LOW|:

       .. rubric:: |UCTR_PIN_SET_LOW|

     - :cspan:`1` |ENUM_PIN_SET_LOW|
     - :rspan:`1`
   * - :token:`PIN_SET_LOW:pin`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: PIN_SET_LOW
          OUTPUT:
          INPUT: `pin`
          pin:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIN_SET_LOW|

       * |LWFW_PIN_SET_LOW|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIN_SET_LOW_1|
       * |CAPI_PIN_SET_LOW_2|

       .. rubric:: |PYAPI|

       * |PYAPI_PIN_SET_LOW_1|
       * |PYAPI_PIN_SET_LOW_2|



   * - :rspan:`1`

       .. _|UCTR_PIN_READ|:

       .. rubric:: |UCTR_PIN_READ|

     - :cspan:`1` |ENUM_PIN_READ|
     - :rspan:`1`
   * - :token:`PIN_READ:pin`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: PIN_READ
          OUTPUT: `state`
          INPUT: `pin`
          pin:
          state:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIN_READ|

       * |LWFW_PIN_READ|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIN_READ|

       .. rubric:: |PYAPI|

       * |PYAPI_PIN_READ|



Little Wire ADC
```````````````

.. flat-table:: Little Wire Firmware ADC Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-adc

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_SETUP_ADC|:

       .. rubric:: |UCTR_SETUP_ADC|

     - :cspan:`1` |ENUM_SETUP_ADC|
     - :rspan:`1`
   * - :token:`SETUP_ADC:vref`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: SETUP_ADC
          OUTPUT:
          INPUT: `vref`
          vref:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SETUP_ADC|

       * |LWFW_SETUP_ADC|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SETUP_ADC|

       .. rubric:: |PYAPI|

       * |PYAPI_SETUP_ADC|



   * - :rspan:`1`

       .. _|UCTR_READ_ADC|:

       .. rubric:: |UCTR_READ_ADC|

     - :cspan:`1` |ENUM_READ_ADC|
     - :rspan:`1`
   * - :token:`READ_ADC:channel`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: READ_ADC
          OUTPUT: `value`
          INPUT: `channel`
          channel:
          value:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_READ_ADC|

       * |LWFW_READ_ADC|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_READ_ADC|

       .. rubric:: |PYAPI|

       * |PYAPI_READ_ADC|



Little Wire PWM
```````````````

.. flat-table:: Little Wire Firmware PWM Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-pwm

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_SETUP_PWM|:

       .. rubric:: |UCTR_SETUP_PWM|

     - :cspan:`1` |ENUM_SETUP_PWM|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: SETUP_PWM
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SETUP_PWM|

       * |LWFW_SETUP_PWM|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SETUP_PWM|

       .. rubric:: |PYAPI|

       * |PYAPI_SETUP_PWM|



   * - :rspan:`1`

       .. _|UCTR_UPDATE_PWM_COMPARE|:

       .. rubric:: |UCTR_UPDATE_PWM_COMPARE|

     - :cspan:`1` |ENUM_UPDATE_PWM_COMPARE|
     - :rspan:`1`
   * - :token:`UPDATE_PWM:chAcomp`
     - :token:`UPDATE_PWM:chBcomp`
   * - :cspan:`1`
     - .. productionlist:: UPDATE_PWM
          OUTPUT:
          INPUT: `chAcomp` & `chBcomp`
          chAcomp:
          chBcomp:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_UPDATE_PWM_COMPARE|

       * |LWFW_UPDATE_PWM_COMPARE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_UPDATE_PWM_COMPARE|

       .. rubric:: |PYAPI|

       * |PYAPI_UPDATE_PWM_COMPARE|



   * - :rspan:`1`

       .. _|UCTR_CHANGE_PWM_PRESCALE|:

       .. rubric:: |UCTR_CHANGE_PWM_PRESCALE|

     - :cspan:`1` |ENUM_CHANGE_PWM_PRESCALE|
     - :rspan:`1`
   * - :token:`CHANGE_PWM:prescale`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: CHANGE_PWM
          OUTPUT:
          INPUT: `prescale`
          prescale:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_CHANGE_PWM_PRESCALE|

       * |LWFW_CHANGE_PWM_PRESCALE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_CHANGE_PWM_PRESCALE|

       .. rubric:: |PYAPI|

       * |PYAPI_CHANGE_PWM_PRESCALE|



   * - :rspan:`1`

       .. _|UCTR_STOP_PWM|:

       .. rubric:: |UCTR_STOP_PWM|

     - :cspan:`1` |ENUM_STOP_PWM|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: STOP_PWM
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_STOP_PWM|

       * |LWFW_STOP_PWM|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_STOP_PWM|

       .. rubric:: |PYAPI|

       * |PYAPI_STOP_PWM|



Little Wire SPI
```````````````

.. flat-table:: Little Wire Firmware SPI Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-spi

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_SINGLE_SPI|:

       .. rubric:: |UCTR_SINGLE_SPI|

     - :cspan:`1` |ENUM_SINGLE_SPI|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_SINGLE_SPI|
     - .. productionlist:: SINGLE_SPI
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SINGLE_SPI|

       * |LWFW_SINGLE_SPI|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`427`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SINGLE_SPI|

       .. rubric:: |PYAPI|

       * |PYAPI_SINGLE_SPI|



   * - :rspan:`1`

       .. _|UCTR_SETUP_SPI|:

       .. rubric:: |UCTR_SETUP_SPI|

     - :cspan:`1` |ENUM_SETUP_SPI|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_SETUP_SPI|
     - .. productionlist:: SETUP_SPI
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SETUP_SPI|

       * |LWFW_SETUP_SPI|

       .. rubric:: last time implemented by firmware V1.1

       * :lwfw11:`480`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SETUP_SPI|

       .. rubric:: |PYAPI|

       * |PYAPI_SETUP_SPI|



   * - :rspan:`1`

       .. _|UCTR_SPI_ADD_BUFFER|:

       .. rubric:: |UCTR_SPI_ADD_BUFFER|

     - :cspan:`1` |ENUM_SPI_ADD_BUFFER|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_SPI_ADD_BUFFER|
     - .. productionlist:: SPI_ADD_BUFFER
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SPI_ADD_BUFFER|

       * |LWFW_SPI_ADD_BUFFER|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`513`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SPI_ADD_BUFFER|

       .. rubric:: |PYAPI|

       * |PYAPI_SPI_ADD_BUFFER|



   * - :rspan:`1`

       .. _|UCTR_SPI_SEND_BUFFER|:

       .. rubric:: |UCTR_SPI_SEND_BUFFER|

     - :cspan:`1` |ENUM_SPI_SEND_BUFFER|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_SPI_SEND_BUFFER|
     - .. productionlist:: SPI_SEND_BUFFER
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SPI_SEND_BUFFER|

       * |LWFW_SPI_SEND_BUFFER|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`522`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SPI_SEND_BUFFER|

       .. rubric:: |PYAPI|

       * |PYAPI_SPI_SEND_BUFFER|



   * - :rspan:`1`

       .. _|UCTR_SPI_UPDATE_DELAY|:

       .. rubric:: |UCTR_SPI_UPDATE_DELAY|

     - :cspan:`1` |ENUM_SPI_UPDATE_DELAY|
     - :rspan:`1`
   * - :token:`SPI_UPDATE:duration`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: SPI_UPDATE
          OUTPUT:
          INPUT: `duration`
          duration:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SPI_UPDATE_DELAY|

       * |LWFW_SPI_UPDATE_DELAY|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SPI_UPDATE_DELAY|

       .. rubric:: |PYAPI|

       * |PYAPI_SPI_UPDATE_DELAY|



   * - :rspan:`1`

       .. _|UCTR_DEBUG_SPI|:

       .. rubric:: |UCTR_DEBUG_SPI|

     - :cspan:`1` |ENUM_DEBUG_SPI|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: DEBUG_SPI
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_DEBUG_SPI|

       * |LWFW_DEBUG_SPI|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_DEBUG_SPI|

       .. rubric:: |PYAPI|

       * |PYAPI_DEBUG_SPI|



   * - :rspan:`1`

       .. _|UCTR_SPI_TRANSFER|:

       .. rubric:: |UCTR_SPI_TRANSFER|

     - :cspan:`1` |ENUM_SPI_TRANSFER|
     - :rspan:`1`
   * - :token:`SPI_TRANSFER:c1c0`
     - :token:`SPI_TRANSFER:c3c2`
   * - :cspan:`1`
     - .. productionlist:: SPI_TRANSFER
          OUTPUT:
          INPUT: `c1c0` & `c3c2`
          c1c0:
          c3c2:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SPI_TRANSFER|

       * |LWFW_SPI_TRANSFER|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SPI_TRANSFER|

       .. rubric:: |PYAPI|

       * |PYAPI_SPI_TRANSFER|



Little Wire I²C
```````````````

.. flat-table:: Little Wire Firmware I²C Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-i2c

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_SETUP_I2C|:

       .. rubric:: |UCTR_SETUP_I2C|

     - :cspan:`1` |ENUM_SETUP_I2C|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_SETUP_I2C|
     - .. productionlist:: SETUP_I2C
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SETUP_I2C|

       * |LWFW_SETUP_I2C|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`489`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SETUP_I2C|

       .. rubric:: |PYAPI|

       * |PYAPI_SETUP_I2C|



   * - :rspan:`1`

       .. _|UCTR_I2C_BEGIN_TX|:

       .. rubric:: |UCTR_I2C_BEGIN_TX|

     - :cspan:`1` |ENUM_I2C_BEGIN_TX|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_I2C_BEGIN_TX|
     - .. productionlist:: I2C_BEGIN_TX
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_BEGIN_TX|

       * |LWFW_I2C_BEGIN_TX|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`494`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_BEGIN_TX|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_BEGIN_TX|



   * - :rspan:`1`

       .. _|UCTR_I2C_ADD_BUFFER|:

       .. rubric:: |UCTR_I2C_ADD_BUFFER|

     - :cspan:`1` |ENUM_I2C_ADD_BUFFER|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_I2C_ADD_BUFFER|
     - .. productionlist:: I2C_ADD_BUFFER
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_ADD_BUFFER|

       * |LWFW_I2C_ADD_BUFFER|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`500`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_ADD_BUFFER|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_ADD_BUFFER|



   * - :rspan:`1`

       .. _|UCTR_I2C_SEND_BUFFER|:

       .. rubric:: |UCTR_I2C_SEND_BUFFER|

     - :cspan:`1` |ENUM_I2C_SEND_BUFFER|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_I2C_SEND_BUFFER|
     - .. productionlist:: I2C_SEND_BUFFER
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_SEND_BUFFER|

       * |LWFW_I2C_SEND_BUFFER|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`505`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_SEND_BUFFER|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_SEND_BUFFER|



   * - :rspan:`1`

       .. _|UCTR_I2C_REQUEST_FROM|:

       .. rubric:: |UCTR_I2C_REQUEST_FROM|

     - :cspan:`1` |ENUM_I2C_REQUEST_FROM|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_I2C_REQUEST_FROM|
     - .. productionlist:: I2C_REQUEST_FROM
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_REQUEST_FROM|

       * |LWFW_I2C_REQUEST_FROM|

       .. rubric:: last time supported by firmware V1.1

       * :lwfw11:`541`

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_REQUEST_FROM|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_REQUEST_FROM|



   * - :rspan:`1`

       .. _|UCTR_I2C_INIT|:

       .. rubric:: |UCTR_I2C_INIT|

     - :cspan:`1` |ENUM_I2C_INIT|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: I2C_INIT
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_INIT|

       * |LWFW_I2C_INIT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_INIT|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_INIT|



   * - :rspan:`1`

       .. _|UCTR_I2C_START|:

       .. rubric:: |UCTR_I2C_START|

     - :cspan:`1` |ENUM_I2C_START|
     - :rspan:`1`
   * - :token:`I2C_START:diraddr`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: I2C_START
          OUTPUT:
          INPUT: `diraddr`
          diraddr: `direction` | `address`
          direction:
          address:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_START|

       * |LWFW_I2C_START|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_START|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_START|



   * - :rspan:`1`

       .. _|UCTR_I2C_READ|:

       .. rubric:: |UCTR_I2C_READ|

     - :cspan:`1` |ENUM_I2C_READ|
     - :rspan:`1`
   * - :token:`I2C_READ:length`
     - :token:`I2C_READ:stop`
   * - :cspan:`1`
     - .. productionlist:: I2C_READ
          OUTPUT:
          INPUT: `length` & `stop`
          length:
          stop:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_READ|

       * |LWFW_I2C_READ|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_READ|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_READ|



   * - :rspan:`1`

       .. _|UCTR_I2C_UPDATE_DELAY|:

       .. rubric:: |UCTR_I2C_UPDATE_DELAY|

     - :cspan:`1` |ENUM_I2C_UPDATE_DELAY|
     - :rspan:`1`
   * - :token:`I2C_UPDATE:duration`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: I2C_UPDATE
          OUTPUT:
          INPUT: `duration`
          duration:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_UPDATE_DELAY|

       * |LWFW_I2C_UPDATE_DELAY|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_UPDATE_DELAY|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_UPDATE_DELAY|



   * - :rspan:`1`

       .. _|UCTR_I2C_TRANSFER|:

       .. rubric:: |UCTR_I2C_TRANSFER|

     - :cspan:`1` |ENUM_I2C_TRANSFER|
     - :rspan:`1`
   * - :token:`I2C_TRANSFER:c1c0`
     - :token:`I2C_TRANSFER:c3c2`
   * - :cspan:`1`
     - .. productionlist:: I2C_TRANSFER
          OUTPUT:
          INPUT: `c1c0` & `c3c2`
          c1c0:
          c3c2:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_I2C_TRANSFER|

       * |LWFW_I2C_TRANSFER|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_I2C_TRANSFER|

       .. rubric:: |PYAPI|

       * |PYAPI_I2C_TRANSFER|



Little Wire Soft-PWM
````````````````````

.. flat-table:: Little Wire Firmware Soft-PWM Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-soft-pwm

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_SOFT_PWM_INIT|:

       .. rubric:: |UCTR_SOFT_PWM_INIT|

     - :cspan:`1` |ENUM_SOFT_PWM_INIT|
     - :rspan:`1`
   * - :token:`SWPWM_INIT:state`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: SWPWM_INIT
          OUTPUT:
          INPUT: `state`
          state:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SOFT_PWM_INIT|

       * |LWFW_SOFT_PWM_INIT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SOFT_PWM_INIT|

       .. rubric:: |PYAPI|

       * |PYAPI_SOFT_PWM_INIT|



   * - :rspan:`1`

       .. _|UCTR_SOFT_PWM_UPDATE|:

       .. rubric:: |UCTR_SOFT_PWM_UPDATE|

     - :cspan:`1` |ENUM_SOFT_PWM_UPDATE|
     - :rspan:`1`
   * - :token:`SWPWM_UPDATE:ch2ch1`
     - :token:`SWPWM_UPDATE:ch3`
   * - :cspan:`1`
     - .. productionlist:: SWPWM_UPDATE
          OUTPUT:
          INPUT: `ch2ch1` & `ch3`
          ch2ch1:
          ch3:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_SOFT_PWM_UPDATE|

       * |LWFW_SOFT_PWM_UPDATE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_SOFT_PWM_UPDATE|

       .. rubric:: |PYAPI|

       * |PYAPI_SOFT_PWM_UPDATE|



Little Wire One-Wire
````````````````````

.. flat-table:: Little Wire Firmware One-Wire Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-ow

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_OW_RESET_PULSE|:

       .. rubric:: |UCTR_OW_RESET_PULSE|

     - :cspan:`1` |ENUM_OW_RESET_PULSE|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: OW_RESET_PULSE
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_OW_RESET_PULSE|

       * |LWFW_OW_RESET_PULSE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_OW_RESET_PULSE|

       .. rubric:: |PYAPI|

       * |PYAPI_OW_RESET_PULSE|



   * - :rspan:`1`

       .. _|UCTR_OW_WRITE_BYTE|:

       .. rubric:: |UCTR_OW_WRITE_BYTE|

     - :cspan:`1` |ENUM_OW_WRITE_BYTE|
     - :rspan:`1`
   * - :token:`OW_WRITE_BYTE:message`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: OW_WRITE_BYTE
          OUTPUT:
          INPUT: `message`
          message:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_OW_WRITE_BYTE|

       * |LWFW_OW_WRITE_BYTE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_OW_WRITE_BYTE|

       .. rubric:: |PYAPI|

       * |PYAPI_OW_WRITE_BYTE|



   * - :rspan:`1`

       .. _|UCTR_OW_READ_BYTE|:

       .. rubric:: |UCTR_OW_READ_BYTE|

     - :cspan:`1` |ENUM_OW_READ_BYTE|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: OW_READ_BYTE
          OUTPUT: `message`
          INPUT:
          message:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_OW_READ_BYTE|

       * |LWFW_OW_READ_BYTE|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_OW_READ_BYTE|

       .. rubric:: |PYAPI|

       * |PYAPI_OW_READ_BYTE|



   * - :rspan:`1`

       .. _|UCTR_OW_READ_BIT|:

       .. rubric:: |UCTR_OW_READ_BIT|

     - :cspan:`1` |ENUM_OW_READ_BIT|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: OW_READ_BIT
          OUTPUT: `bitval`
          INPUT:
          bitval:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_OW_READ_BIT|

       * |LWFW_OW_READ_BIT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_OW_READ_BIT|

       .. rubric:: |PYAPI|

       * |PYAPI_OW_READ_BIT|



   * - :rspan:`1`

       .. _|UCTR_OW_WRITE_BIT|:

       .. rubric:: |UCTR_OW_WRITE_BIT|

     - :cspan:`1` |ENUM_OW_WRITE_BIT|
     - :rspan:`1`
   * - :token:`OW_WRITE_BIT:bitval`
     - .. wIndex not used
   * - :cspan:`1`
     - .. productionlist:: OW_WRITE_BIT
          OUTPUT:
          INPUT: `bitval`
          bitval:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_OW_WRITE_BIT|

       * |LWFW_OW_WRITE_BIT|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_OW_WRITE_BIT|

       .. rubric:: |PYAPI|

       * |PYAPI_OW_WRITE_BIT|



Little Wire WS2812
``````````````````

.. flat-table:: Little Wire Firmware WS2812 Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-ws2812

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_WS2812_EXEC|:

       .. rubric:: |UCTR_WS2812_EXEC|

     - :cspan:`1` |ENUM_WS2812_EXEC|
     - :rspan:`1`
   * - :token:`WS2812_EXEC:cGpincmd`
     - :token:`WS2812_EXEC:cBcR`
   * - :cspan:`1`
     - .. productionlist:: WS2812_EXEC
          OUTPUT:
          INPUT: `cGpincmd` & `cBcR`
          cGpincmd: `cG` + `pin` + `cmd`
          cBcR: `cB` + `cR`
          pin:
          cmd:
          cR:
          cG:
          cB:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_WS2812_EXEC|

       * |LWFW_WS2812_EXEC|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_WS2812_EXEC_1|
       * |CAPI_WS2812_EXEC_2|
       * |CAPI_WS2812_EXEC_3|

       .. rubric:: |PYAPI|

       * |PYAPI_WS2812_EXEC|



Little Wire Experimental
````````````````````````

.. flat-table:: Little Wire Firmware Experimental Control Transfer Requests
   :header-rows: 4
   :stub-columns: 2
   :widths: 1 2 2 5
   :name: lwfw12-usbctr-lwfw-exp

   * - :cspan:`2` `Setup Packet`_
     - :rspan:`2` Description / Notes
   * - :rspan:`1` :code:`bRequest`
     - :cspan:`1` Name
   * - :code:`wValue`
     - :code:`wIndex`
   * - :cspan:`3` Implementation / Interfaces



   * - :rspan:`1`

       .. _|UCTR_PIC24F_PROG|:

       .. rubric:: |UCTR_PIC24F_PROG|

     - :cspan:`1` |ENUM_PIC24F_PROG|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_PIC24F_PROG|
     - .. productionlist:: PIC24F_PROG
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIC24F_PROG|

       * |LWFW_PIC24F_PROG|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIC24F_PROG|

       .. rubric:: |PYAPI|

       * |PYAPI_PIC24F_PROG|



   * - :rspan:`1`

       .. _|UCTR_PIC24F_SENDSIX|:

       .. rubric:: |UCTR_PIC24F_SENDSIX|

     - :cspan:`1` |ENUM_PIC24F_SENDSIX|
     - :rspan:`1`
   * - .. wValue not used
     - .. wIndex not used
   * - :cspan:`1` |STATE_PIC24F_SENDSIX|
     - .. productionlist:: PIC24F_SENDSIX
          OUTPUT:
          INPUT:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIC24F_SENDSIX|

       * |LWFW_PIC24F_SENDSIX|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIC24F_SENDSIX|

       .. rubric:: |PYAPI|

       * |PYAPI_PIC24F_SENDSIX|



   * - :rspan:`1`

       .. _|UCTR_PIC24F_TRANSFER|:

       .. rubric:: |UCTR_PIC24F_TRANSFER|

     - :cspan:`1` |ENUM_PIC24F_TRANSFER|
     - :rspan:`1`
   * - :token:`PIC24F_TRANSFER:c1c0`
     - :token:`PIC24F_TRANSFER:c3c2`
   * - :cspan:`1` |STATE_PIC24F_TRANSFER|
     - .. productionlist:: PIC24F_TRANSFER
          OUTPUT:
          INPUT: `c1c0` & `c3c2`
          c1c0:
          c3c2:
   * - :cspan:`1` Implementation
     - .. rubric:: |LWFW| – |STATE_PIC24F_TRANSFER|

       * |LWFW_PIC24F_TRANSFER|

   * - :cspan:`1` Interfaces
     - .. rubric:: |CAPI|

       * |CAPI_PIC24F_TRANSFER|

       .. rubric:: |PYAPI|

       * |PYAPI_PIC24F_TRANSFER|



.. spelling::

   GPIO
   ADC
   PWM
   SPI
   I2C
   I²C
   Soft-PWM
   One-Wire
   WS2812
   PIC24F
