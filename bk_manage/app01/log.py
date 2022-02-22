# coding:utf-8
import subprocess

# dict = {}
currfile = "find  /tmp/bk_logs/10.2.1.35 -type f |xargs -n10 tail -n 2"





#res = subprocess.Popen(currfile,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
res = subprocess.Popen(currfile,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")

out,err = res.communicate()
result = out.split("\n\n")
print(result)
print(err)

# result = res.stdout.read()
# result = str(result,encoding="gbk")
# print(result)`