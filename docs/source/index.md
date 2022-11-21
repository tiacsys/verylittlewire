# Welcome to Little Wire Python library documentation!

````{caution}
**WORK IN PROGRESS!**
```{admonition} Multiple Device Support
---
class: important
---
For the time being, only the code of [VeryLittleWire] that was provided for Python 2 will be transferred to Python 3, with more focus on unchanged interfaces than new features or behavior. Since the previous class could only handle a single [Little Wire] USB device, the multiple device feature will be integrated at a later time. This is then where [PyFtdi's multiple and simultaneous device usage feaures] will most likely come in and require a rework of the inner and outer interfaces.
```
```{admonition} Unit Test Quality
---
class: important
---
All activities on the first Python 3 transfer are only protected by rudimentary unit tests with white box character. The entire [PyUSB] stack is simply mocked away and only the expected calls to the relevant [PyUSB] objects are tested and thus protected. Only with the so far only planned improvements based on the PyFtdi design, [the test framework in practice there] is also presented here. In addition to integration tests in combination with real hardware, simulated USB devices in clearly specified topologies can then also be included in the unit tests and the quality can be improved considerably, towards black box unit tests.
```
```{todolist}
```
````

[verylittlewire]: https://github.com/tiacsys/verylittlewire/blob/adajoh99/master/Python/library%20v1.0/littleWire.py "Little Wire access for Python 2"
[little wire]: https://github.com/littlewire/Little-Wire "multi-featured USB controlled hardware tool"
[pyusb]: https://github.com/pyusb/pyusb "Easy USB access for Python"
[pyftdi's multiple and simultaneous device usage feaures]: https://eblot.github.io/pyftdi/features.html#devices "Features of the FTDI device driver written in pure Python"
[the test framework in practice there]: https://eblot.github.io/pyftdi/testing.html "Testing of the FTDI device driver written in pure Python"

```{toctree}
:caption: Installation & Usage
:maxdepth: 2

installation
usage
api
```

```{toctree}
:caption: Project Info
:maxdepth: 2

changelog
contributing
```

```{include} ../../README.md

```
