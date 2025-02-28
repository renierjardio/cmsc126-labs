import json

class NetworkLayer:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        
    def send(self, data, dest_ip):
        packet = {'IP': self.ip_address, 'Dest_IP': dest_ip, 'Data': data}
        print(f"[NETWORK] Encapsulating packet: {packet}")
        return json.dumps(packet)
    
    def receive(self, packet):
        packet_data = json.loads(packet)
        print(f"[NETWORK] Decapsulating packet: {packet_data}")
        return packet_data['Data']