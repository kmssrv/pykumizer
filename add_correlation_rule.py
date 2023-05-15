from pykumizer import Kuma
import json

with open('rule.json') as f:
    rule = json.load(f)

kuma = Kuma("kuma.kogorta.lab", "komissarov", "KLaapt-M1")
tenant_id = kuma.get_tenant_id_by_name('Main')
correlation_rule_id = kuma.add_correlation_rule(rule)
correlator_id = kuma.get_correlator_id_by_name('test name234', tenant_id)
kuma.link_rule(correlator_id, correlation_rule_id)
service_id = kuma.get_service_id_by_resouce_id(correlator_id)
kuma.reload_service(service_id)