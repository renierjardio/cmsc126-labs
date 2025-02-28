import json

class DataLinkLayer:
    def __init__(self, mac_address):
        self.mac_address = mac_address
        
    def send(self, data):
        frame = {'MAC': self.mac_address, 'Payload': data}
        print(f"[DATA_LINK] Encapsulating frame: {frame}")
        return json.dumps(frame)
    
    def receive(self, frame):
        frame_data = json.loads(frame)
        print(f"[DATA_LINK] Decapsulating frame: {frame_data}")
        return frame_data['Payload']