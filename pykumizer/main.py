import requests
import json
import urllib.parse
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Kuma:
  def __init__(self, url, login, password):
    self.login = login
    self.password = password
    self.url = "https://"+url+":7220"

    url = self.url+"/api/login"

    payload = json.dumps({
      "login": login,
      "password": password
    })
    headers = {}
    self.session = requests.Session()
    self.session.headers.update(headers)
    response = self.session.post(url, data=payload, verify=False)

    self.session.headers.update({
      'X-XSRF-TOKEN': urllib.parse.unquote(self.session.cookies['XSRF-TOKEN'])
    })

  def logout(self):
    url = self.url+"/api/logout"
    response = self.session.post(url, verify=False)
    print(response)
    print(response.text)

  def add_correlation_rule(self, rule):
    url = self.url+"/api/private/resources/correlationRule"
    payload = json.dumps(rule)
    response = self.session.post(url, data=payload)
    print(response)
    correlation_rule_id = self.get_rule_id_by_name(rule['name'], rule['tenantID'])
    return correlation_rule_id

  def get_tenant_id_by_name(self, name):
    url = self.url+"/api/private/tenants/"
    response = self.session.get(url)
    for tenant in response.json():
      if tenant['name'] == name:
        return tenant['id']

  def get_rule_id_by_name(self, name, tenant_id):
    url = self.url+"/api/private/resources/correlationRule?tenantID="+tenant_id
    response = self.session.get(url)
    for rule in response.json():
      if rule['name'] == name:
        return rule['id']
  def delete_rule(self, rule_id):
    url = self.url+"/api/private/resources/correlationRule"
    payload = json.dumps({"ids": [rule_id]})
    print(json.dumps(payload))
    response = self.session.delete(url, data=payload)
    print(response.text)

  def get_correlator_id_by_name(self, name, tenant_id):
    url = self.url+"/api/private/resources/correlator?tenantID="+tenant_id
    response = self.session.get(url)
    for correlator in response.json():
      if correlator['name'] == name:
        return correlator['id']

  def link_rule(self, correlator_id, correlation_rule_id):
      url = self.url+"/api/private/resources/correlator/"+correlator_id
      correlation_rule_payload = self.get_correlation_rule_by_id(correlation_rule_id)
      correlator_data = self.get_correlator_by_id(correlator_id)

     # chek if correlator has no linked rules
      if 'rules' not in correlator_data['payload']:
        correlator_data['payload']['rules'] = []

      for cor_rul in correlator_data['payload']['rules']:
        if cor_rul['id'] == correlation_rule_id:
          print('duplicate, skip')
          return

      correlator_data['payload']['rules'].append(correlation_rule_payload)
      response = self.session.put(url, data=json.dumps(correlator_data))

  def get_resource_by_id(self, resource_id):
    url = self.url+"/api/private/resources/"
    response = self.session.get(url)
    for resource in response.json():
      if resource['id'] == resource_id:
        return resource

  def get_correlation_rule_by_id(self, correlation_rule_id):
    url = self.url+"/api/private/resources/correlationRule/"+correlation_rule_id
    response = self.session.get(url)
    data = response.json()
    return data['payload']

  def get_destination_by_id(self, destination_id):
    url = self.url+"/api/private/resources/destination/" + destination_id
    response = self.session.get(url)
    data = response.json()
    return data['payload']

  def get_dependences(self, resource_id):
    url = self.url+"/api/private/resources/dependencies/"+resource_id
    response = self.session.get(url)
    return (response.json())

  def get_correlator_by_id(self, correlator_id):
    url = self.url+"/api/private/resources/correlator/"+correlator_id
    response = self.session.get(url)
    return (response.json())

  def get_service_id_by_resouce_id(self, resource_id):
    url = self.url+"/api/private/services/"
    response = self.session.get(url)
    for service in response.json():
      if service['resourceID'] == resource_id:
        return service['id']

  def reload_service(self, service_id):
    url = self.url+"/api/private/services/id/"+service_id+"/reload"
    payload = json.dumps({})
    response = self.session.post(url, data=payload)