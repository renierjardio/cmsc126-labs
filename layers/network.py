import json
import socket

class NetworkLayer:
    def __init__(self):
        self.ip_address = self.get_ip_address()

    def get_ip_address(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception as e:
            return "127.0.0.1"
        
    def send(self, data, dest_ip):
        packet = {'IP': self.ip_address, 'Dest_IP': dest_ip, 'Data': data}
        print(f"[NETWORK] Encapsulating packet: {packet}")
        return json.dumps(packet)
    
    def receive(self, packet):
        packet_data = json.loads(packet)
        print(f"[NETWORK] Decapsulating packet: {packet_data}")
        return packet_data['Data']