from jnpr.junos import Device
import sys
dev = Device(host="10.8.241.31", user="jdearborn", passwd="zRGRcwy5")
from jnpr.junos.utils.config import Config
cu = Config(dev)
dev.open()
rsp = cu.load( path="config-example.conf" )
cu.commit()
dev.close()
