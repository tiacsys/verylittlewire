# Welcome to Little Wire Python library documentation!

````{caution}
**WORK IN PROGRESS!**
```{admonition} Multiple Device Support
---
class: important
---
For the time being, only the code of [VeryLittleWire] that was provided for Python 2 will be transferred to Python 3, with more focus on unchanged interfaces than new features or behavior. Since the previous class could only handle a single [Little Wire] USB device, the multiple device feature will be integrated at a later time. This is then where [PyFtdi's multiple and simultaneous device usage feaures] will most likely come in and require a rework of the inner and outer interfaces.
```
```{todolist}
```
````

[verylittlewire]: https://github.com/tiacsys/verylittlewire/blob/adajoh99/master/Python/library%20v1.0/littleWire.py "Little Wire access for Python 2"
[little wire]: https://github.com/littlewire/Little-Wire "multi-featured USB controlled hardware tool"
[pyftdi's multiple and simultaneous device usage feaures]: https://eblot.github.io/pyftdi/features.html#devices "Features of the FTDI device driver written in pure Python"

```{toctree}
:caption: Installation & Usage
:maxdepth: 2

installation
usage
```

```{toctree}
:caption: Project Info
:maxdepth: 2

changelog
contributing
```

```{include} ../../README.md

```
