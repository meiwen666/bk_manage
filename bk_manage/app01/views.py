from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
import subprocess
from rest_framework.response import Response
from rest_framework import  status
#from rest_framework_jwt.utils import
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

class get_user_info(APIView):
    def get(self,request):
        print('entering ...')
        User = get_user_model()
        print(request.headers)
        print('GET: ', request.GET)
        print(request.GET.get("token"))
        token = request.GET.get("token")
        #用一个空数组来接收token解析后的值
        token_user=[]
        #token_user = jwt_decode_handler(token)

        print(request.user.username)
        print(request.user.id)
        print(request.user.date_joined)
        return Response('success:{}'.format(token))




#提交定时任务到数据库
class cron(APIView):

    #permission_classes = []
    def get(self,request,*args,**kwargs):
        cron = Cron.objects.all()
        serializer = CronSerializer(cron,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CronSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#获取个别定时任务
class crondetail(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get_cron(self,id):
        try:
            cron = Cron.objects.get(id=id)
            return cron
        except Exception as  e:
            raise Http404

    # def get(self,request,*args,**kwargs):
    #     cron = self.get_cron(kwargs.get('id'))
    #     serializer = CronSerializer(cron)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    #
    # def put(self,request,*args,**kwargs):
    #     cron = self.get_cron(kwargs.get('id'))
    #     serializer = CronSerializer(cron,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self,request,*args,**kwargs):
    #     cron = self.get_cron(kwargs.get('id'))
    #     serializer = CronSerializer(cron, data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        cron = self.get_cron(kwargs.get('id'))
        cron.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#新增定时备份服务器的ip列表到数据库
class Bkip(APIView):

    #permission_classes = []
    def get(self,request,*args,**kwargs):
        ip = Address.objects.all()
        serializer = IPSerializer(ip,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = IPSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BkipDetail(APIView):
    def get_ip(self,id):
        try:
            ip = Address.objects.get(id=id)
            return ip
        except Exception as e:
            raise Http404

    def get(self,request,*args,**kwargs):
        ip = self.get_ip(kwargs.get('id'))
        serializer = IPSerializer(ip)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        ip = self.get_ip(kwargs.get('id'))
        serializer = IPSerializer(ip,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        ip = self.get_ip(kwargs.get('id'))
        serializer = IPSerializer(ip, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        ip = self.get_ip(kwargs.get('id'))
        ip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








#创建定时任务并同步到备份服务器
class croncreate(APIView):
    def get_ip(self,id):
        try:
            ip = Address.objects.get(id=id)
            return ip
        except Exception as e:
            raise Http404

    def get(self,request,*args,**kwargs):
        msg = {"code": None}
        id = kwargs.get('id')
        ip = self.get_ip(kwargs.get('id'))
        cron = Cron.objects.filter(bkip=id)
        file_path = "/tmp/cron_{0}".format(ip.bk_ip)
        ssh = "scp {0}  {1}:/var/spool/cron/root".format(file_path,ip.bk_ip)
        print(ssh)
        with open(file_path,"w") as f:
            for i in cron:
                f.write("#{0} \n".format(i.comments))
                f.write("{0} {1} {2} {3} {4} rsync -avzP --delete root@{5}::{6} {7} > {8}/{5}.log 2>&1  \n\n".format(i.minute,i.hour,i.day,i.month,i.week,i.ip,i.s_path,i.d_path,i.log_path))
        res = subprocess.Popen(ssh,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
        out,err = res.communicate()
        return_code = res.wait()
        if return_code ==0:
            msg["code"]="定时任务创建成功{0}".format(out)
        else:
            msg["code"]=err
        return Response(msg,status=status.HTTP_200_OK)



#定时任务展示查看
class cronshow(APIView):
    def get_ip(self,id):
        try:
            ip = Address.objects.get(id=id)
            return ip
        except Exception as e:
            raise Http404

    def get(self,request,*args,**kwargs):
        list = []
        ip = self.get_ip(kwargs.get('id'))
        file_path = "/tmp/cron_{0}".format(ip.bk_ip)
        with open(file_path, 'r') as f:
            res = f.read().strip()
            data = res.split("\n\n")
            for i in data:
                dic = {}
                dic["cron"] = i
                list.append(dic)
        return Response(list,status=status.HTTP_200_OK)


#日志展示查看
class logshow(APIView):
    def get_ip(self,id):
        ip = Address.objects.get(id=id)
        return ip

    def get(self,request,*args,**kwargs):
        ip = self.get_ip(kwargs.get("id"))
        path = "/tmp/bk_logs/{0}".format(ip.bk_ip)
        currfile = "find  {0} -type f |xargs -n10 tail -n 2".format(path)
        res = subprocess.Popen(currfile, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        out, err = res.communicate()
        result = out.split("\n\n")
        list=[]
        for i in result:
            data={}
            data["log"]=i
            list.append(data)
        return Response(list,status=status.HTTP_200_OK)
