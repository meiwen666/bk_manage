<template>
    <div class="modal-backdrop">
      <div class="modal" >
        <div class="modal-header">
          <h3>定时任务</h3>
        </div>
        <div class="modal-body">
            <el-row justify="center" class="distance">
             <el-col :span="23">
                <el-table :data="showtask_data" style="width: 100%">
                  <el-table-column prop="cron"  ></el-table-column>           
                </el-table>
              </el-col>
          </el-row>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn-confirm" @click="closeme">关闭</button>
        </div>
      </div>


    </div>
</template>

<script>
export default {
  name:'task',

  props:{
      showtask_data:{
        typeof:Object
      }
   },

  data(){
   return {
      
   }
  },

  methods: {
    closeme(){
      this.$emit("closeme"); 
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

.btn-confirm {
    color: #fff; 
    background-color: #2d8cf0;
}

</style>

