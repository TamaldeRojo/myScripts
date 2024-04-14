import nmap
import socket
from scapy.all import ARP,Ether, srp
from time import time




def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]        
        s.close()
        
        return ip_address
    except Exception as e:
        print("Error:", e)
        return None
    
def nmapScanner(ip):
    ep = nmap.PortScanner()
    ipMask = ip + "/24"
    ep.scan(ipMask)
    print(f"[+] {ep.all_hosts()}")
    
def scapyScanner(ip):
    # scapy.arping(ip)
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet,timeout=3,verbose=False)[0]
    
    connectedDevice = []
    
    for sent, received in result:
        connectedDevice.append({'ip': received.psrc,'mac':received.hwsrc})
    return connectedDevice


def main():
    ip = "192.168.0.1/24" #get_ip_address() + "/24"
    print(ip)
    devices = scapyScanner(ip)
    
    print("Connected devices:")
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t{device['mac']}")
    print("-----------------------------------------")
    
if __name__ == "__main__":
    main()