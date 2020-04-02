import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import logging

class MessageHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #Игнорируем favicon.ico и ставим уровень логгирования INFO
        if self.path.endswith('favicon.ico'):
            return
        
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n",str(self.path), str(self.headers))
        '''
        Обрабатываем GET запрос. Если значение меньше или равно нулю
        выводится сообщение об ошибке
        '''
        try:
            m=self.path.replace('/','')
            
            if float(m) <= 0:
                self.send_error(400,'Wrong input: %s' % self.path)
                return
    
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            a = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
            jsonResponse = json.loads(a.decode('utf-8'))
            for USD in jsonResponse ['Valute']['USD'],:
                z=USD["Value"]*float(m)
            #Отдаём JSON с результатом конвертации
            self.wfile.write(json.dumps(
                {'currency':'USD',
                'requestedValue':m,
                'resultingValue':round(z,2), #Округляем значение
                'requestVersion':self.request_version,
                'protocolVersion':self.protocol_version},
                 ensure_ascii=False).encode('utf-8'))
        except ValueError:
            self.send_error(400,'Wrong input: %s' % self.path)
        
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)       
    server_address = ('', 80)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
