const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: "/static",
  transpileDependencies: true,
  pages: {
    index: {
      entry: "src/entries/login.js",
      template: "public/index.html",
      filename: "index.html",
      title: "Kemppi software management portal – Login",
      chunks: ["chunk-vendors", "chunk-common", "index"],
    },
    app: {
      entry: "src/entries/app.js",
      template: "public/index.html",
      filename: "app.html",
      title: "Kemppi software management portal – Application",
      chunks: ["chunk-vendors", "chunk-common", "app"],
    },
    admin: {
      entry: "src/entries/admin.js",
      template: "pubic/index.html",
      filename: "admin.html",
      title: "Kemppi software management portal – Administration",
      chunks: ["chunk-vendors", "chunk-common", "admin"],
    },
  },
})
