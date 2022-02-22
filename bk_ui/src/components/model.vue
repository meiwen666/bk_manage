<template>
    <div class="modal-backdrop">
      <div class="modal" >
          <div class="modal-header">
            <h3>编辑定时任务</h3>
          </div>
          <div class="modal-body">
            <el-form :label-position="labelPosition" label-width="80px">
              <el-form-item label="分钟">
                <el-input v-model="editdata.minute"></el-input>
              </el-form-item>
              <el-form-item label="小时">
                <el-input v-model="editdata.hour"></el-input>
              </el-form-item>
              <el-form-item label="日/天">
                <el-input v-model="editdata.day"></el-input>
              </el-form-item>
              <el-form-item label="月份">
                <el-input v-model="editdata.month"></el-input>
              </el-form-item>
              <el-form-item label="周">
                <el-input v-model="editdata.week"></el-input>
              </el-form-item>
              <el-form-item label="用户">
                <el-input v-model="editdata.user"></el-input>
              </el-form-item>
              <el-form-item label="IP">
                <el-input v-model="editdata.ip"></el-input>
              </el-form-item>
              <el-form-item label="备份路径">
                <el-input v-model="editdata.bk_path"></el-input>
              </el-form-item>
              <el-form-item label="日志路径">
                <el-input v-model="editdata.log_path"></el-input>
              </el-form-item>
            </el-form>
          </div>
          <div class="modal-footer">
              <button type="button" class="btn-close" @click="closeSelf">取消</button>
              <button type="button" class="btn-confirm" @click="confirm(editdata)">提交</button>
          </div>
      </div>
    </div>
</template>

<script>
export default {
  name:'model',

  props:{
    editdata:{
      type:Object
    }
   },

  data(){
   return {
     labelPosition:"left",
     data:this.editdata
   }
  },

  methods: {
    closeSelf(){      //子组件传递父组件的关闭事件
      this.$emit("closeme")
    },
    confirm(changdata){        //子组件传递父组件的提交事件
      this.$emit("confirm",changdata)           //changdata的数据其实就是editdata编辑后的数据通过字传父发送给父组件
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
    box-shadow: 1px 1px 1px 1px; 
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

