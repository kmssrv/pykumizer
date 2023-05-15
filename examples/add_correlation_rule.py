from pykumizer import Kuma
import json

with open('detect_powershell_download.json') as f:
    rule = json.load(f)

kuma = Kuma("kuma.kogorta.lab", "admin", "<password>")

folder_id = kuma.get_folder_id_by_name('OOTB', 'correlationRule')

correlation_rule_id = kuma.add_correlation_rule(rule, folder_id)

correlator_id = kuma.get_correlator_id_by_name('[OOTB] Correlator')

kuma.link_rule(correlator_id, correlation_rule_id)

service_id = kuma.get_service_id_by_resouce_id(correlator_id)

kuma.reload_service(service_id)

kuma.logout()
