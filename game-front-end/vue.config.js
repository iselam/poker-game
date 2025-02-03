const { defineConfig } = require('@vue/cli-service')
 module.exports = defineConfig({
//   transpileDependencies: [
//     'vuetify'
//   ],
  devServer: {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true',
      'Access-Control-Allow-Methods': 'GET,HEAD,OPTIONS,POST,PUT',
      'Access-Control-Allow-Headers':
      'Origin, X-Requested-With, Content-Type, Accept, Authorization',
    },
    proxy:'http://127.0.0.1:5000/'
  }
})
