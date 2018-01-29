from http.server import BaseHTTPRequestHandler, HTTPServer
from run import run
import re

HOST_ADDRESS = "0.0.0.0"
PORT_NUMBER = 80


asdf = run({"doctorfirstname": "0", "doctorlastname": "0", "patientfirstname": "0", "patientlastname": "0", "diagnosis": "0", "diagnosisdate": "0", "conditionstart": "0"})

def addBlock(data):
    asdf.parse(data)

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
            print(self.path)
            data = self.rfile.read(int(self.headers['Content-Length']))
            data = data.decode("UTF-8", "replace")
            pairs = re.findall("\"(.*?)\"", data)
            addBlock(pairs)
            while i < len(pairs):
                if pairs[i] == "patientfirstname":
                        self.patientFirstName = pairs[i+1]
            send_sms.sendMessage(self.patientPhone, "Your injury has been filed. View it at http://35.196.237.62/find?name=" + self.patientFirstName)
