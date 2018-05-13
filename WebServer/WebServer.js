var path = require("path");
var express = require("express");
var app = express();
app.listen(10086);
app.use(express.static(path.join(process.cwd(), "www_root")));

console.log("web服务器已经启动");