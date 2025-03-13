from layers import physical, datalink, network, transport, session, presentation, application

def simulate_communication(data, dest_ip):
    app = application.ApplicationLayer()
    pres = presentation.PresentationLayer()
    sesh = session.SessionLayer()
    transp = transport.TransportLayer()
    net = network.NetworkLayer()
    dtl = datalink.DataLinkLayer()
    phys = physical.PhysicalLayer()
    
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
    received_message = simulate_communication(sent_message, "192.168.1.2")
    
    print(f"\nSuccessful! Received message is: {received_message}")
    
    
if __name__ == "__main__":
    main()
                
        