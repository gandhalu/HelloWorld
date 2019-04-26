import os
env = os.environ
print("TYPE=",env['TYPE'])
cmd1 = "echo sending to docker image1"
cmd2 = "echo sending to docker image2"
type = env['TYPE']
if (type == 'QA'):
    os.system(cmd1)
elif (type == 'TEST'):
    os.system(cmd2)

