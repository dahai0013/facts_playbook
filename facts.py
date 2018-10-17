import sys
import json
import yaml
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

dev = Device(host='192.168.99.111',user='ansible',passwd='ansible123')
try:
    dev.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

print("#print everything\n")
pprint (dev.facts)

#print("\n#print only the version")
#pprint (dev.facts['version'])

#print (yaml.dump(dev.facts))

#print (json.dumps(dev.facts))

dev.close()