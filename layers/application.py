import json

class ApplicationLayer:
    def send(self, data):
        request = {'Request': 'GET', 'Payload': data}
        print(f"[APPLICATION] Sending request: {request}")
        return json.dumps(request)
    
    def receive(self, request):
        request_data = json.loads(request)
        print(f"[APPLICATION] Received request: {request_data}")
        return request_data['Payload']