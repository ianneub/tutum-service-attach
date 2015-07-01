import os
import tutum
import string
import logging
import copy
import re

# requests_log = logging.getLogger("python-tutum")
# requests_log.setLevel(logging.INFO)

target = tutum.Service.fetch(os.environ["TARGET_UUID"])
me = tutum.Utils.fetch_by_resource_uri(os.environ["TUTUM_SERVICE_API_URI"])
stack = tutum.Utils.fetch_by_resource_uri(me.stack)

regex = re.compile(".+_1_ENV_TUTUM_SERVICE_API_URI")
links = copy.copy(target.linked_to_service)
for key in os.environ:
  if regex.match(key):
    service = tutum.Utils.fetch_by_resource_uri(os.environ[key])
    if not any(l['to_service'] == service.resource_uri for l in links):
      new_service_name = "{0}-{1}".format(service.name,stack.name)
      links.append({"name":new_service_name, "to_service": service.resource_uri})
      target.linked_to_service = links
      print "Service {0} - {1} needs link to {2} - {3}".format(target.name, target.uuid, new_service_name, service.uuid)
      if target.save():
        print "Added link to service {0} - {1}".format(new_service_name, service.uuid)
    else:
      print "Service {0} - {1} already has link to {2} - {3}".format(target.name, target.uuid, service.name, service.uuid)
