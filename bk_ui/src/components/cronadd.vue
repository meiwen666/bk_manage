<template>
    <div class="modal-backdrop">
      <div class="modal" >
        <div class="modal-header">
          <h3>添加定时</h3>
        </div>
        <div class="modal-body">
          <el-form :inline="true" :model="crondata" ref="crondata" :rules="rules"   class="demo-form-inline" label-width="30px" labelPosition="top">
            <el-form-item label="分钟" prop="minute">
            <el-input v-model="crondata.minute" placeholder="分钟" />
           </el-form-item>
            <el-form-item label="小时" prop="hour">
              <el-input v-model="crondata.hour" placeholder="小时"></el-input>
            </el-form-item>
            <el-form-item label="天" prop="day">
              <el-input v-model="crondata.day" placeholder="天"></el-input>
            </el-form-item>
            <el-form-item label="月" prop="month">
              <el-input v-model="crondata.month" placeholder="月"></el-input>
            </el-form-item>
            <el-form-item label="周" prop="week">
              <el-input v-model="crondata.week" placeholder="周"></el-input>
            </el-form-item>
            <el-form-item label="IP" prop="ip">
              <el-input v-model="crondata.ip" placeholder="IP"></el-input>
            </el-form-item>
            <el-form-item label="模块" prop="s_path">
              <el-input v-model="crondata.s_path" placeholder="模块"></el-input>
            </el-form-item>
            <el-form-item label="备份路径" prop="d_path">
              <el-input v-model="crondata.d_path" placeholder="备份路径"></el-input>
            </el-form-item>
            <el-form-item label="日志路径" prop="log_path">
              <el-input v-model="crondata.log_path" placeholder="日志路径"></el-input>
            </el-form-item>
            <el-form-item label="描述" prop="comments">
              <el-input v-model="crondata.comments" placeholder="描述"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn-close" @click="closeCron">取消</button>
            <button type="button" class="btn-confirm" @click="commit(crondata);confirm()">提交</button>
        </div>
      </div>


    </div>
</template>

<script>
import { postCronData } from "../api/index.js"

export default {
  name:'cronadd',

  props: {
    cronid:{
    }
  },

  data(){
   return {
    crondata:{
      minute:"",
      hour:"",
      day:"",
      month:"",
      week:"",
      ip:"",
      s_path:"",
      d_path:"",
      log_path:"",
      comments:"",
    },
    rules:{
      minute:[
        {
            required: true,
            message: '请输入分钟',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 2,
            message: 'Length should be 1 to 2',
            trigger: 'blur',
          },
      ],
      hour:[
        {
            required: true,
            message: '请输入小时',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 2,
            message: 'Length should be 1 to 2',
            trigger: 'blur',
          },
      ],

      ip:[
        {
            required: true,
            message: '请输入IP',
            trigger: 'blur',
          }
      ],


      s_path:[
        {
            required: true,
            message: '请输入模块',
            trigger: 'blur',
          },
      ],
      d_path:[
        {
            required: true,
            message: '请输入备份路径',
            trigger: 'blur',
          },
      ],
       log_path:[
        {
            required: true,
            message: '请输入日志路径',
            trigger: 'blur',
          },
      ],
      comments:[
        {
            required: true,
            message: '请输入备份描述',
            trigger: 'blur',
          },
      ],
    },

   }
  },







  methods: {

  
    //提交定时数据
    commit(crondata){
      crondata['bkip']=this.cronid
      this.$refs.crondata.validate((vaild)=>{
        if (vaild) {
          alert('submit!')
        } else {
          console.log('errorr submit')
          return false
        }
      })
      // postCronData(crondata).then(()=>{
          
      // })
      console.log(crondata);
      console.log(this.cronid);
    },

   //提交确认
   confirm(){
     this.$emit("confirm");
   },

  //取消操作
    closeCron(){
      this.$emit("closecron"); 
    }
  },
}
</script>




<style scoped>
.modal-backdrop { 
    position: fixed; 
    top: 0; 
    right: 0; 
    bottom: 0; 
    left: 0; 
    background-color: rgba(0,0,0,.3); 
    display: flex; 
    justify-content: center; 
    align-items: center; 
}
.modal { 
    background-color: #fff; 
    box-shadow: 1px ; 
    overflow-x:auto; 
    display: flex; 
    flex-direction: column;
    border-radius: 16px;
    width: 700px;
} 
.modal-header { 
    border-bottom: 1px solid #eee; 
    color: #313131; 
    justify-content: space-between;
    padding: 15px; 
    display: flex; 
} 
.modal-footer { 
    border-top: 1px solid #eee; 
    justify-content: flex-end;
    padding: 15px; 
    display: flex; 
} 
.modal-body { 
    position: relative; 
    padding: 20px 10px; 
}
.btn-close, .btn-confirm {    
    border-radius: 8px;
    margin-left:16px;
    width:56px;
    height: 36px;
    border:none;
    cursor: pointer;
}
.btn-close {
    color: #313131;
    background-color:transparent;
}
.btn-confirm {
    color: #fff; 
    background-color: #2d8cf0;
}

</style>

