import json

class TransportLayer:
    def send(self, data):
        segment = {'Seq': 1, 'Ack': 1, 'Data': data}
        print(f"[TRANSPORT] Encapsulating segment: {segment}")
        return json.dumps(segment)
    
    def receive(self, segment):
        segment_data = json.loads(segment)
        print(f"[TRANSPORT] Decapsulating segment: {segment_data}")
        return segment_data['Data']