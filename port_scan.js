/*NOTE: This has been replaced with port_scan_detect.py*/
var http = require("http")
var port =  40 //a port you want to protect
http.createServer(function(req,res){
console.log("Attack detected on port " + port)
console.log("URL requested: " + req.url)
console.log("User agent string: " + req.headers["user-agent"])
console.log("Host header: " + req["headers"].host)
res.writeHead(200,{"Content-Type":"text/plain"})
res.write("000")
res.end()
}).listen(port)