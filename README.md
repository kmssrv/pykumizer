# Pykumizer: python wrapper for KUMA API
**English version below**

Pykumizer - это инструменты и примеры работы с закрытым API KUMA 2.1.
В KUMA 3.0 ожидаются улучшения API. А пока использую python requests для некоторых задач.

Pykumizer is a repository containing tools and examples that cover various approaches to automating actions when working with the SIEM KUMA (Kaspersky Unified and Analysis Platform).

# KUMA private API
The Python package pykumizer is a wrapper for working with the private API of KUMA. It contains methods for accessing the hidden private API of KUMA for various actions.

## Usage
Install the package
```
git clone https://github.com/kmssrv/pykumizer.git
cd pykumizer/
python3 -m pip install dist/pykumizer-<version>-py3-none-any.whl
```

## Quick start
Go to examples and replace credentials in add_correlation_rule.py file with your own
```
cd examples/
vi add_correlation_rule.py
```
Execute the script
```
python3 add_correlation_rule.py
```

A test rule will be added to resources and linked to the correlator.
![example.png](img%2Fexample.png)

The rule must be in KUMA JSON format. By default, the script uses:
1. Tenant: 'Main'
2. Correlator: '[OOTB] Correlator'
3. Folder in correlation rules list: '[OOTB]'.

## Use the module in your own scripts
Import the module to your Python script
```
from pykumizer import Kuma
```
Create a Kuma object by providing the address of the KUMA core installation, username, and password
```
kuma = Kuma("kuma.kogorta.lab", "admin", "<password>")
```
### Examples
Get the tenant ID by name
```
tenant_id = kuma.get_tenant_id_by_name('Main')
```
Get the folder ID by name and subkind of resource
```
folder_id = kuma.get_folder_id_by_name('KOMISSAROV', 'correlationRule')
```
Add a correlation rule to resources. The rule is a JSON object.
```
correlation_rule_id = kuma.add_correlation_rule(rule, folder_id)
```
Get the correlator ID by name
```
correlator_id = kuma.get_correlator_id_by_name('[OOTB] Correlator', tenant_id)
```
Link the correlation rule to the correlator. The rule must be added to resources first.
```
kuma.link_rule(correlator_id, correlation_rule_id)
```
Get the service ID by resource ID
```
service_id = kuma.get_service_id_by_resource_id(correlator_id)
```
Reload the service using the service ID
```
kuma.reload_service(service_id)
```
# Updates
#### 17.05.2023 v0.0.4 
Fix: get_correlation_rule_id_by_name()

Only 250 items are returned by default. The parameter 'size' needs to be specified. Thanks to Igor!

New example: add 500 random rules.