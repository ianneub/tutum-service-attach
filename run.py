import os
import tutum
import string
import logging
import copy

# requests_log = logging.getLogger("python-tutum")
# requests_log.setLevel(logging.DEBUG)

target = tutum.Service.fetch(os.environ["TARGET_UUID"])
me = tutum.Service.fetch(string.split(os.environ["TUTUM_SERVICE_API_URI"], "/")[-2])

links = copy.copy(target.linked_to_service)
if not any(l['to_service'] == me.resource_uri for l in links):
  links.append({"name":me.name, "to_service": me.resource_uri})
  target.linked_to_service = links
  print "Service {0} - {1} needs link to {2} - {3}".format(target.name, target.uuid, me.name, me.uuid)
  if target.save():
    print "Added link to service {0} - {1}".format(me.name, me.uuid)
else:
  print "Service {0} - {1} already has link to {2} - {3}".format(target.name, target.uuid, me.name, me.uuid)
