import {request} from "./axiosConfig";



//获取数据库定时选项
export function getCronData(){
    return request({
        url:"/api/cron",
        method:"get",
    })
}


//新增定时选项任务
export function postCronData(crondata){
    return request({
        url:"/api/cron/",
        method:"post",
        data:crondata,
    })
}

//获取备份服务器ip
export function getBkIp(){
    return request({
        url:"/api/bkip",
        method:"get",
    })
}



//新增备份服务器ip
export function postBkIp(ip){
    return request({
        url:"/api/bkip/",
        method:"post",
        data:{
            bk_ip:ip
        }
    })
}

//删除备份服务器ip
export function delBkIp(id){
    return request({
        url:"/api/bkipdetail/"+id+"/",
        method:"delete"
    })
}


//点击同步按钮创建定时任务并同步数据到备份服务器
export function getCronCreate(id){
    return request({
        url:"/api/croncreate/"+id,
        method:"get"
    })
}


//定时任务展示
export function getCronShow(id){
    return request({
        url:"/api/cronshow/"+id,
        method:"get",
    })
}


//日志展示
export function getLogShow(id){
    return request({
        url:"/api/logshow/"+id,
        method:"get",
    })
}