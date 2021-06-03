# 生成rsa密钥
# $ openssl genrsa -des3 -out server.key 1024
# 去除掉密钥文件保护密码
# $ openssl rsa -in server.key -out server.key
# 生成ca对应的csr文件
# $ openssl req -new -key server.key -out server.csr
# 自签名
# $ openssl x509 -req -days 1024 -in server.csr -signkey server.key -out server.crt
# $ cat server.crt server.key > server.pem

#!/usr/bin/python

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/path/to/server.pem', server_side=True)
httpd.serve_forever()
