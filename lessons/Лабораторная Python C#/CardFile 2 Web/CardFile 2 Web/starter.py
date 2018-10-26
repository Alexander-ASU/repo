import os, threading, time
from http.server import HTTPServer, CGIHTTPRequestHandler

def launch(port):
	time.sleep(3)
	os.system("start http://localhost:{0}/cgi-bin/launcher.py".format(port))

def main():
    os.chdir('.')
    port = 80
    threading.Thread(target=launch, kwargs={'port':port}).start()
    HTTPServer(('', port), CGIHTTPRequestHandler).serve_forever()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
