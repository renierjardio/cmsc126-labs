import json
import uuid

class DataLinkLayer:
    def __init__(self):
        self.mac_address = self.get_mac_address()

    def get_mac_address(self):
        mac = uuid.getnode()
        mac_address = ':'.join(f'{(mac >> i) & 0xff:02x}' for i in reversed(range(0, 48, 8)))
        return mac_address
    
    def send(self, data):
        frame = {'MAC': self.mac_address, 'Payload': data}
        print(f"[DATA_LINK] Encapsulating frame: {frame}")
        return json.dumps(frame)
    
    def receive(self, frame):
        frame_data = json.loads(frame)
        print(f"[DATA_LINK] Decapsulating frame: {frame_data}")
        return frame_data['Payload']