#!/usr/bin/python3

from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen 

#cmdGen = cmdgen.CommandGenerator() 
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
    CommunityData('pri'),
    UdpTransportTarget(('172.16.209.233', 161)), 
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0))))

# Check for errors and print out results
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

g = setCmd(SnmpEngine(),
  CommunityData('pri'),
  UdpTransportTarget(('172.16.209.233', 161)),
  ContextData(),
  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0), 'Test Linux i386'))

next(g)

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
    CommunityData('pri'),
    UdpTransportTarget(('172.16.209.233', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0))))


if errorIndication: 
    print(errorIndication) 
else: 
    if errorStatus: 
        print('%s at %s' % ( 
            errorStatus.prettyPrint(), 
            errorIndex and varBinds[int(errorIndex)-1] or '?' 
            ) 
        ) 
    else: 
        for name, val in varBinds: 
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint())) 
