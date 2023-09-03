# Capturing a PMKID from WPA/WPA2 Access Points with a Python Script
A python script for capturing a PMKID from a WiFi router for cracking WPA/WPA2 passwords.

To crack passwords from the captured PMKID obtained by this script, see our other repo:
<a href="https://github.com/ZeroDayArcade/wpa-password-cracking-with-pmkid">WPA/WPA2 Password Cracking in Python - PMKID</a>

This script will produce hash lines in the hashcat hc22000 format that can be cracked with hashcat and will also print out the necessary data to crack passwords with the script from our other repo referenced above. It is built for simplicity and comprehension and is meant to help those looking to build their own hacking tools get started with a bare-bones example.

Unlike capturing a 4-way handshake, you do not need need to put your WiFi adapter into monitor mode. I tested the PMKID capture with <a href="https://www.amazon.com/GenBasic-Wireless-Network-Dongle-Adapter/dp/B0BNFKJPXS/">this WiFi adapter that can be bought for less than $10 on Amazon</a>. Your computer's internal WiFi adapter may work for this purpose since monitor mode is not required, but when testing with a Raspberry Pi 4 I found that I had to use the USB WiFi adapter. The capture was from a TP-Link Archer C1200 v2.0 Router (Firmware Version 2.0.0), but many other common wireless routers should work. Note that not all wireless routers are vulnerable to this exploit, only those that append a PMKID to the end of the first EAPoL frame. This exploit was originally found in 2018 by atom and the hashcat team. See the thread on the hashcat forums: <a href="https://hashcat.net/forum/thread-7717.html">Thread</a>. This script will give you a way to capture PMKID with very little code using only standard python libraries that you can modify for your own purposes. 

This script should work on the majority of Linux distributions including Kali Linux and may also work on macOS or Windows, but if you are running macOS or Windows it will might be easier to use the script with a Virtual Machine running a form of Linux with VirtualBox or VMWare. 

*Only ever hack a network you own and have legal permission to hack. This is for educational purposes only.* 

## Getting and running the script
Clone the project:
```
git clone https://github.com/ZeroDayArcade/capture-pmkid-wpa-wifi-hacking.git
```
cd into project directory:
```
cd capture-pmkid-wpa-wifi-hacking
```
***No monitor mode required***, you can just leave you wireless adapter in the default managed mode. To run the script for a given network/access point run:
```
sudo python3 capture_pmkid.py <INTERFACE> "<SSID>"
```
Then attempt to connect to that network with the same interface/wireless adapter and ***any random password***. While the random password will be rejected, the access point will send back a PMKID appended to the end of first EAPoL frame that you can use to crack the network password. This assumes of course that the access point is one that appends a PMKID. Many common WPA/WPA2 routers do this. 

I successfully tested this with a TP-Link Archer C1200 v2.0 Router (Firmware Version 2.0.0), a Raspberry Pi 4 running Raspian, and a <a href="https://www.amazon.com/GenBasic-Wireless-Network-Dongle-Adapter/dp/B0BNFKJPXS/">GenBasic Wireless Adapter (Model 2A4M1)</a>.

### Example ###

Let's say we are targeting an access point with SSID = `ZDA_TP_LINK` and our wireless adapter's WiFi interface is `wlan1`. In that case we'd run
```
sudo python3 capture_pmkid.py wlan1 "ZDA_TP_LINK"
```
You'll then see the string "`Connect to "ZDA_TP_LINK" using wlan1 and a random password to capture PMKID...` printed in Terminal. On your computer, use wlan1 to connect to `ZDA_TP_LINK` as you would connect to any other WiFi network. For a Raspberry Pi 4 running Raspian, this would be clicking the Wireless LAN dropdown on the top right of the screen, hovering over `wlan1` and then selecting `ZDA_TP_LINK` from the dropdown of available networks. On most OS's you can also do this from the command line in a seperate Terminal window. 

Once prompted for a password, enter a random password of at least 8 characters. Upon doing this, the script will capture the PMKID and print out:
```
Possible PMKID:                <PMKID>
SSID:                          <SSID>
MAC AP:                        <MAC_ADDRESS_ACCESS_POINT>
MAC Client:                    >MAC_ADDRESS_OF_INTERFACE>

Hashcat hc22000 format hash line:
<WPA01_HASHCAT_HC22000_FORMAT_HASHLINE>
```

You can then use the fields printed above with `crack_pmkid.py` from our other repo: <a href="https://github.com/ZeroDayArcade/wpa-password-cracking-with-pmkid/">here</a>, or for more speed and power, use the `WPA*01*<PMKID>*<MAC_AP>*<MAC_CL>*<ESSID>***` line with hashcat.


# More Zero Day Arcade Tutorials:
**Learn Reverse Engineering, Assembly, Code Injection and More:**  
🎓  <a href="https://zerodayarcade.com/tutorials">zerodayarcade.com/tutorials</a> 

**More WiFi Hacking with Simple Python Scripts:**  
<a href="https://github.com/ZeroDayArcade/wpa-password-cracking-with-pmkid">Cracking WPA/WPA2 Passwords with PMKID</a>  
<a href="https://github.com/ZeroDayArcade/capture-handshake-wpa-wifi-hacking">Capturing WPA/WPA2 4-Way Handshake</a>  
<a href="https://github.com/ZeroDayArcade/cracking-wpa-with-handshake">Cracking WPA/WPA2 Passwords with 4-Way Handshake</a>  


# Find Hacking Bounties in Gaming:
🎮  <a href="https://zerodayarcade.com/bounties">zerodayarcade.com/bounties</a>



