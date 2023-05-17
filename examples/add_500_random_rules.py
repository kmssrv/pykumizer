from pykumizer import Kuma
import json
import uuid

with open('mock.json') as f:
    rule = json.load(f)

kuma = Kuma("kuma.kogorta.lab", "admin", "<password>")

folder_id = kuma.get_folder_id_by_name('OOTB', 'correlationRule')

i = 1
while i < 500:
    rule['name'] = 'test_rule_' + str(i)
    rule['payload']['name'] = 'test_rule_' + str(i)
    rule['id'] = str(uuid.uuid4())
    rule['exportID'] = str(uuid.uuid4())
    rule['payload']['id'] = str(uuid.uuid4())
    correlation_rule_id = kuma.add_correlation_rule(rule, folder_id)
    i += 1


