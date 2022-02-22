

import subprocess

y  = "scp cron_{0}  {0}:/var/spool/cron/root".format()


i = {'minute': 5, 'hour': 5, 'day': '*', 'month': 9, 'week': 6, 'ip': '10.2.1.108', 's_path': '/data','d_path': '/tmp', 'log_path': '/data/log'}



x=  """cat >>/var/spool/cron/root   << EOF 
{0} {1} {2} {3} {4} rsync -avzP --delete root@{5}::{6} {7} > {8}/{5}.log 2>&1  \n\n""".format(i['minute'],i['hour'],i['day'],i['month'],i['week'],i['ip'],i['s_path'],i['d_path'],i['log_path'])

print(x)

obj = subprocess.Popen(x,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
return_code = obj.wait()
if return_code == 0:
    print("任务执行成功")
else:
    print("任务执行失败")



if i["day"] == "*":
    i["day"] = 0
if i["month"] == "*":
    i["month"] = 0
if i["week"] == "*":
    i["week"] = 0
if i["day"] == "*" and i["month"] == "*" and i["week"] == "*":
    i["day"] = 0
    i["month"] = 0
    i["week"] = 0

print(i)
