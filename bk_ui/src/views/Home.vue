<template>
  <div class="common-layout">
    <el-row :gutter="1">
      <!-- 左边栏 -->
      <el-col :md="8" >
        <div class="grid-content bg-purple">
          <el-row :gutter="1" justify="center" class="distance">
              <el-col :span="10">
                <el-form :rules="rules" ref="form" :model="form">
                  <el-form-item label="备份IP" prop="input_ip">
                    <el-input v-model="form.input_ip" placeholder="请输入IP" />
                  </el-form-item>
                </el-form> 
              </el-col>
              <el-col :span="2">
                <el-button type="primary" @click="add(form.input_ip)">添加</el-button>
              </el-col>
          </el-row>
          
          <el-row justify="center" >
             <el-col :span="23">
                <el-table :data="get_ip" style="width: 100%">
                  <el-table-column prop="bk_ip" width="250%" ></el-table-column>
                  <el-table-column >
                      <template #default="scope">
                        <el-button type="text" size="small" @click="addcron(get_ip[scope.$index].id)">添加定时</el-button>   
                        <el-button type="text" size="small" @click="sysnc(get_ip[scope.$index].id)">同步</el-button>
                        <el-button type="text" size="small" @click="cronshow(get_ip[scope.$index].id)">查看任务</el-button>
                        <el-button type="text" size="small" @click="logshow(get_ip[scope.$index].id)">查看日志</el-button>
                        <el-button type="danger" plain @click="delIP(get_ip[scope.$index].id)">删除</el-button>
                     </template>
                  </el-table-column>
                </el-table>  
              </el-col>
          </el-row>
        </div>
      </el-col>


      <!-- 右边栏 -->
      <el-col :md="16" >
        <div class="grid-content bg-purple-light">
          <el-row justify="center" class="distance">
             <el-col :span="23">
                <el-table :data="log_data" style="width: 100%">
                  <el-table-column prop="log"  ></el-table-column>           
                </el-table>
              </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>

    <!-- 子组件 -->
    <cronadd   v-show="cronadd"  :cronid="cronid"   @closecron="closecron"  @confirm="confirm"></cronadd>  
    <task v-show="showtask"   :showtask_data="showtask_data"  @closeme="closeme"></task>
  </div>

</template>

<script>
import { getBkIp,postBkIp,getLogShow,getCronShow,getCronCreate,delBkIp } from "../api/index.js"
import { Delete } from '@element-plus/icons-vue'
import task from '../components/task.vue';
import cronadd from '../components/cronadd.vue';

export default{
  components: { task,cronadd },

  data() {
    return {
      cronid:"",
      form: {
        input_ip: ''
      },
      get_ip:"",
      log_data:[],
      showtask_data:[],
      showtask:false,
      cronadd:false,
      rules:{
        input_ip:[
          {
          required: true,
          message: '请输入备份IP',
          trigger: 'blur',
          }
        ]
      }
    }
  },


  methods:{
    //获取服务IP
    getIP(){
      getBkIp().then((res)=>{
      this.get_ip=res.data
    }).catch((err)=>{
      console.log(err);
      })
    },
    

    //新增服务器IP
    add(data){
      // console.log(typeof ip);
      postBkIp(data).then(()=>{
        this.getIP()
        })
    },
   
    //删除服务器IP
    delIP(idx){
        this.$confirm('此操作将永久删除该记录, 是否继续?', '删除',{
          confirmButtonText:'确定',
          cancelButtonText:'取消',
          type: 'warning'
        }).then(()=>{
          delBkIp(idx).then(()=>{
            this.getIP()
          })
          this.$message({
            type:'success',
            message:'删除成功！'
          })
        }).catch(()=>{
          this.$message({
            type:'info',
            message:'已取消删除'
          })
        })
    },




  //查看日志
    logshow(idx){
       getLogShow(idx).then((res)=>{
         console.log(res.data);
         this.log_data=res.data
       })
    },


     //查看任务
      cronshow(idx){
      getCronShow(idx).then((res)=>{
        this.showtask_data=res.data
        this.showtask=!this.showtask
      })
   },


    //添加定时
      addcron(idx){
        this.cronid=idx
        console.log(this.cronid)
        this.cronadd=!this.cronadd
      },

    //创建定时任务并同步到服务器
    sysnc(idx){
      getCronCreate(idx).then(()=>{
          this.$message({
          type:"success",
          message:"同步完成"
        })   
      })
    },


    //查看定时任务子组件传递父组件的事件(关闭)
      closeme(){ 
        this.$message({
          type:"success",
          message:"查看完成"
      })
      this.showtask=!this.showtask
    },


    //提交定时数据子组件传递父组件的取消事件（关闭）
    closecron(){
      this.$message({
          type:"info",
          message:"取消操作"
      })
      this.cronadd=!this.cronadd
    },

     //提交定时数据子组件传递父组件的确认事件（关闭）
    confirm(){
      this.$message({
          type:"success",
          message:"提交成功"
      })
      this.cronadd=!this.cronadd
    },


  },


 


  mounted(){
    this.getIP()
    this.logshow(1)
    },
}
</script>









<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
 .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    height: 100vh;
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .distance{
  padding:10px  ;
  }
</style>
