# Pykumizer
English version below.

Здесь мои наработки для автоматизации работы с KUMA 2.1. В KUMA 3.0 ожиадаются улучщения API, а пока жду, подготовил некоторые скрипты.

Красивое описание на английском ниже.



Pykumizer is a repository containing tools and examples that cover various approaches to automating actions when working with the SIEM KUMA (Kaspersky Unified and Analysis Platform).
Wrapper for working with the private API of Kaspersky Unified and Analysis Platform 2.1.
# KUMA private API
The Python package pykumizer-0.0.1-py3-none-any.whl contains methods for accessing the hidden private API of KUMA for various actions.
## Usage
Example 1. Add corelation rule to resources, link rule to correlator and update correlator config.
```
git clone https://github.com/kmssrv/pykumizer.git
cd pykumizer/
python3 -m pip install dist/pykumizer-0.0.1-py3-none-any.whl
python3 add_correlation_rule.py

```