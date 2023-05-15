# Pykumizer
Pykumizer is a repository containing tools and examples that cover various approaches to automating actions when working with the SIEM KUMA (Kaspersky Unified and Analysis Platform).
Wrapper for working with the private API of Kaspersky Unified and Analysis Platform 2.1.
# KUMA private API
The Python package pykumizer-0.0.1-py3-none-any.whl contains methods for accessing the hidden private API of KUMA for various actions.
## Usage
Install package
```
git clone https://github.com/kmssrv/pykumizer.git
cd pykumizer/
python3 -m pip install dist/pykumizer-0.0.1-py3-none-any.whl
```
Import module to your python script
```
from pykumizer import Kuma
```
Create kuma object by providing address of KUMA core installation, username and password
```commandline
kuma = Kuma("kuma.kogorta.lab", "admin", "<password>")
```
Examples
```commandline
# Get tenant ID by name
tenant_id = kuma.get_tenant_id_by_name('Main')

# Get folder ID by name and subkind of resource
folder_id = kuma.get_folder_id_by_name('KOMISSAROV', 'correlationRule')

# Add correlation rule to resourses. Rule is json object.
correlation_rule_id = kuma.add_correlation_rule(rule, folder_id)

# Get correlatror ID by name
correlator_id = kuma.get_correlator_id_by_name('[OOTB] Correlator', tenant_id)

# Link correlation rule to correlator. Rule must be added to recorse first.
kuma.link_rule(correlator_id, correlation_rule_id)

# Get service ID by resourse ID
service_id = kuma.get_service_id_by_resouce_id(correlator_id)

# Reload service using service ID
kuma.reload_service(service_id)
```