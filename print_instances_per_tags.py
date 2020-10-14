# Python script print out all running instances filter base on tags. 
import boto3
ec2 = boto3.resource('ec2')
# Filter instances tags 
instances = ec2.instances.filter(
    Filters=[
        {'Name': 'tag:owner', 'Values': ['Engineering']},
        {'Name': 'tag:stack', 'Values': ['dev']}
    ])

def _print_intance(id, type, state, ip, lt):
    print(
             '   Instance ID: ' + id + '\n' 
             '   Type: ' + type + '\n' 
             '   State: ' + state + '\n'
             '   IP Address: ' + ip + '\n'
             '   Launch Time: ' + lt
        )
i = 0
a = 0
for instance in instances:
    state = instance.state['Name']
    if state == 'running':
        a = a + 1
        _print_intance(instance.id, instance.instance_type, state, \
            instance.private_ip_address, str(instance.launch_time))
    else:
        _print_intance(instance.id, instance.instance_type, state, \
            instance.private_ip_address, str(instance.launch_time))
    i = i + 1    
    print('-------------------------------------------')

print('There are total ' + str(i) + ' instances and ' + str(a) + ' are running')
