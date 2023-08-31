const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  devServer: { // 自定义服务配
    host: 'localhost',
    port: 8002, // 修改的端口号
    open: true
  }
})

 