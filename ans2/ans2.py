from azure.mgmt.compute import ComputeManagementClient
from azure.identity import ClientSecretCredential
from collections import defaultdict
# provide these values with your service principal properties
subscription = ""
tenant = ""
appId = ""
password = ""

credential = ClientSecretCredential(client_id=appId,client_secret=password,tenant_id=tenant)

compute_client = ComputeManagementClient(credential, subscription)

vm_list = compute_client.virtual_machines.list('try')
windows_machines = defaultdict(lambda: 0)
linux_machines = defaultdict(lambda: 0)
for vm in vm_list:
    vm.hardware_profile.vm_size
    if vm.os_profile.windows_configuration is not None:
        key = ('Windows', vm.hardware_profile.vm_size)
        windows_machines[key] += 1
    else:
        key = ('Linux', vm.hardware_profile.vm_size)
        linux_machines[key] += 1
print("OS", "\t", "Machine Type", "\t", "Count")
print("----------------------------------------------")
for k,v in windows_machines.items():
    print(k[0],"\t",k[1],"\t",v)
for k,v in linux_machines.items():
    print(k[0],"\t",k[1],"\t",v)
