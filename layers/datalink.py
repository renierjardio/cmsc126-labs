import json
import uuid

class DataLinkLayer:
    def __init__(self):
        self.mac_address = self.get_mac_address()

    def get_mac_address(self):
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 8)][::-1])
        return mac
    
    def receive(self, frame):
        frame_data = json.loads(frame)
        print(f"[DATA_LINK] Decapsulating frame: {frame_data}")
        return frame_data['Payload']