# sekiro_demo
sekiro远程服务获取js加密


原理：
	相当于部署一个jsrpc服务，在linux开一个sekiro-server服务端，在一台机器上开一个浏览器，注入你的加密代码，远程py访问接口，由浏览器去执行js代码，获取数据

实际使用
	1：首先把你需要的js代码抠出来，改造成一个返回结果的方法，相当于base64.JS文件
	2：把这个js替换base64.js文件
	3：在demo.html文件中替换src="./base64.js"为你自己的文件名称
	4：new SekiroClient("wss://sekiro.virjar.com/websocket?group=ws-group-nieyaoban&clientId=" + guid());
	修改你自己的group，不然别人会用到
	5： client.registerAction("base64_encode", function (request, resolve, reject) {
            resolve(base64_encode(request['encode_str']));
        });
	注册你自己的方法名称，第一个base64_encode是你可以调用的action
	第二个base64_encode是你的js文件中的方法名
	request['encode_str']是你发起的请求以及传入的参数
	6：调用的时候：demo.py改group	
	action：你在html中注册的方法名
	encode_str：你的参数名以及你传入的参数
	
自己开sekiro服务端
    拉docker镜像：docker pull registry.cn-beijing.aliyuncs.com/virjar/sekiro-server:latest
    启动容器：docker run -d -p 5600:5600 -p 5601:5601 -p 5602:5602 -p 5603:5603 registry.cn-beijing.aliyuncs.com/virjar/sekiro-server
    服务器的话需要开放相应的端口
    改客户端html的文件：ws://192.168.31.190:5603/websocket?
    改py文件：http://192.168.31.190:5602/invoke
