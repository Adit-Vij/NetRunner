from scapy.all import sniff, IP
import logging

logging.basicConfig(filename="external_ips_contacted.log", level = logging.INFO, format = '%(asctime)s-%(message)s')

contacted_ips =  [] #Global List

def log_contacted_ip(packet):

    if IP in packet:

        dest_ip = packet[IP].dst
        if not dest_ip.startswith(('10.', '172.', '192.168.')) and dest_ip not in contacted_ips:

            contacted_ips.append(dest_ip)
            logging.info(f"Contacted external ip: {dest_ip}")
            print(f"Contacted external ip: {dest_ip}")
            
def start_sniffing():
    sniff(filter="ip", prn = log_contacted_ip, store = 0)