import scapy.all as scapy
import optparse


def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip_address", dest="ip_address", help="Enter IP address")

    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP address")

    return user_input


def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    all_packet = broadcast / arp_request
    (answered_list, unanswered_list) = scapy.srp(all_packet, timeout=1)
    answered_list.summmary()


ip_address = get_input()
scan_network(ip_address.ip_address)
