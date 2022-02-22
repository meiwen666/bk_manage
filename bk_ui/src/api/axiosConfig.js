import axios from "axios";


export function request(config){
    const server = axios.create({
        baseURL:'',
        timeout:5000
    })



    //添加一个请求拦截器
    server.interceptors.request.use(
        function(config){
            //在发送请求之前做些什么
            return config;
        },
        function (error){
            //错误返回
            return Promise.reject(error);
        }
    );


    //添加一个响应拦截器
    server.interceptors.response.use(
        function(response){
            return response;
        },
        function(error){
            return Promise.reject(error);
        }
    )
    
    return server(config);
}




