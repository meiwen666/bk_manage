/*


*/

module.exports = {
  lintOnSave: false,
  devServer:{
    open:true,
    host:"0.0.0.0",
    port:8080,
    https:false,
    hotOnly:false,
    proxy:{
      '^/api':{
        target:"http://10.2.1.106:8001",
        changeOrigin:true,
        secure:false,
        pathRewrite:{
          '^/api':'/api'
        }
      }
    },
  }
};
