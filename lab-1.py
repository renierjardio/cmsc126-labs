import json
import pickle
import base64

class PhysicalLayer:
    def send(self, data):
        bits = ''.join(format(byte, '08b') for byte in data.encode())
        print(f"[PHYSICAL] Converting data to bits: {bits}")
        return bits  
            
    def receive(self, bits):
        bytes_data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8)).decode(errors='ignore')
        print(f"[PHYSICAL] Received raw bits: {bytes_data}")
        return bytes_data
            

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
            

class TransportLayer:
    def send(self, data):
        segment = {'Seq': 1, 'Ack': 1, 'Data': data}
        print(f"[TRANSPORT] Encapsulating segment: {segment}")
        return json.dumps(segment)
    
    def receive(self, segment):
        segment_data = json.loads(segment)
        print(f"[TRANSPORT] Decapsulating segment: {segment_data}")
        return segment_data['Data'] 


class SessionLayer:
    def send(self, data):
        if isinstance(data, bytes):
            data = base64.b64encode(data).decode('utf-8')
        session = {'Session_ID': 12345, 'Data': data}
        print(f"[SESSION] Managing session: {session}")
        return json.dumps(session)
        
    def receive(self, session):
        session_data = json.loads(session)
        print(f"[SESSION] Handling session: {session_data}")
        data = session_data['Data']
        try:
            data = base64.b64decode(data.encode('utf-8'))
        except (base64.binascii.Error, UnicodeDecodeError):
            pass
        return data


class PresentationLayer:
    def send(self, data):
        encoded_data = pickle.dumps(data)
        print(f"[PRESENTATION] Encoding data: {encoded_data}")
        return encoded_data
    
    def receive(self, encoded_data):
        decoded_data = pickle.loads(encoded_data)
        print(f"[PRESENTATION] Decoding data: {decoded_data}")
        return decoded_data
            

class ApplicationLayer:
    def send(self, data):
        request = {'Request': 'GET', 'Payload': data}
        print(f"[APPLICATION] Sending request: {request}")
        return json.dumps(request)
    
    def receive(self, request):
        request_data = json.loads(request)
        print(f"[APPLICATION] Received request: {request_data}")
        return request_data['Payload']
 
   
def simulate_communication(data, dest_ip, mac_address):
    app = ApplicationLayer()
    pres = PresentationLayer()
    sesh = SessionLayer()
    transp = TransportLayer()
    net = NetworkLayer(ip_address='192.168.1.1')
    dtl = DataLinkLayer(mac_address)
    phys = PhysicalLayer()
    
    # Sending side
    app_data = app.send(data)
    pres_data = pres.send(app_data)
    sesh_data = sesh.send(pres_data)
    transp_data = transp.send(sesh_data)
    net_data = net.send(transp_data, dest_ip)
    dtl_data = dtl.send(net_data)
    phys_data = phys.send(dtl_data)
    
    # Receiving side
    received_dtl_data = phys.receive(phys_data)
    received_net_data = dtl.receive(received_dtl_data)
    received_transp_data = net.receive(received_net_data)
    received_sesh_data = transp.receive(received_transp_data)
    received_pres_data = sesh.receive(received_sesh_data)
    received_app_data = pres.receive(received_pres_data)
    final_data = app.receive(received_app_data)
    
    return final_data
        

def main():
    print(f"Hello! Welcome to the OSI Model Python Simulation.")
    sent_message = input("Please enter a data to be sent: ")
    dest_ip = input("Now, please enter the destination IP: ")
    mac_address = input("Lastly, input the MAC Address: ")
    received_message = simulate_communication(sent_message, dest_ip, mac_address)
    
    print(f"\nSuccessful! Received message is: {received_message}")
    
    
if __name__ == "__main__":
    main()
                
        