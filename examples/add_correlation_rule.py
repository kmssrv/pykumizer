from pykumizer import Kuma
import json

with open('detect_powershell_download.json') as f:
    rule = json.load(f)

kuma = Kuma("kuma.kogorta.lab", "komissarov", "<password>")
tenant_id = kuma.get_tenant_id_by_name('Main')
folder_id = kuma.get_folder_id_by_name('KOMISSAROV', 'correlationRule')
correlation_rule_id = kuma.add_correlation_rule(rule, folder_id)
correlator_id = kuma.get_correlator_id_by_name('[OOTB] Correlator', tenant_id)
kuma.link_rule(correlator_id, correlation_rule_id)
service_id = kuma.get_service_id_by_resouce_id(correlator_id)
kuma.reload_service(service_id)