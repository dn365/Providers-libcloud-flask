#!/usr/bin/python
import json
import sys
import os
import checkStatus
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.digitalocean import DigitalOceanNodeDriver
from libcloud.compute.drivers.azure_arm import AzureNodeDriver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver
from libcloud.compute.drivers.linode import LinodeNodeDriver

def deleteNode(provider,driverUno,driverDos,driverTres,driverCuatro,nodeId):
	pass
	nodesProvider = ''
	if provider == "Digital Ocean":
		pass
		accessKey = driverUno
		driverDos = driverDos
		driverTres = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		driver = DigitalOceanNodeDriver(accessKey)
		
		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod
				nodeDelete = driver.destroy_node(idNod)

				types = 'terminated'

				node = checkStatus.checkStatus(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeDelete

	if provider == "EC2":
		pass
		accessId = driverUno
		secretKey = driverDos
		region = driverTres
		driverCuatro = driverCuatro
		nodeId = nodeId
		reg = region[0:len(region)-1]
	#	driver = BaseEC2NodeDriver(accessId,secretKey,'eu-west-1')

		cls = get_driver(Provider.EC2)
		driver = cls(accessId, secretKey, region=reg)
		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod
				public_ips = driver.ex_describe_all_addresses(only_associated = True)

				for public_ip in public_ips:

					if public_ip.instance_id == idNod.id:
						ip = public_ip
						
						nodeDelete = driver.destroy_node(idNod)

						driver.ex_release_address(ip, domain = ip.domain)

						types = 'terminated'

						node = checkStatus.checkStatus(driver, idNod.id, types)

						if node != 0:
							nodesProvider = nodeDelete
						else:
							nodesProvider = 'null'

	if provider == "Azure":
		pass
		tenantId = driverUno
		subscriptionId = driverDos
		applicationId = driverTres
		keyPaswd = driverCuatro
		nodeId = nodeId
		driver = AzureNodeDriver(tenantId,subscriptionId,applicationId,keyPaswd)

		idsNodes = driver.list_nodes()

		for idNodes in idsNodes:
			#print idsNodes
			if idNodes.id == nodeId:
				pass
				idNod = idNodes
	#			print idNod

				nodeDelete = driver.destroy_node(idNod)

				types = 'deleting'

				node = checkStatus.checkStatusAzure(driver, idNod.id, types)

				if node != 0:
					nodesProvider = nodeDelete


	return nodesProvider
