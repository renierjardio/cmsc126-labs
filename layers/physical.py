class PhysicalLayer:
    def send(self, data):
        bits = ''.join(format(byte, '08b') for byte in data.encode())
        print(f"[PHYSICAL] Converting data to bits: {bits}")
        return bits  
            
    def receive(self, bits):
        bytes_data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8)).decode(errors='ignore')
        print(f"[PHYSICAL] Received raw bits: {bytes_data}")
        return bytes_data