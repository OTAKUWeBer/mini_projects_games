import os
import re
import subprocess

# Function to get the list of wireless networks and their details
def get_wireless_networks():
    # Run the 'netsh' command to get the wireless networks
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=bssid']).decode()
    
    # Regex pattern to extract network details
    network_pattern = re.compile(r'SSID \d+ : (.+?)\r\n\s+Network type\s+: (.+?)\r\n\s+Authentication\s+: (.+?)\r\n\s+Encryption\s+: (.+?)\r\n\s+BSSID \d+\s+: (.+?)\r\n\s+Signal\s+: (.+?)\r\n\s+Radio type\s+: (.+?)\r\n\s+Channel\s+: (.+?)\r\n\s+Basic rates\s+: (.+?)\r\n\s+Other rates\s+: (.+?)\r\n\s+Network ID\s+: (.+?)\r\n\s+', re.DOTALL)
    
    # Find all network details in the output
    networks = network_pattern.findall(output)
    
    return networks

# Function to get the password of a specific network
def get_network_password(ssid):
    # Run the 'netsh' command to get the password of the network
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode()
    
    # Regex pattern to extract the password
    password_pattern = re.compile(r'Key Content\s+: (.+?)\r\n\s+', re.DOTALL)
    
    # Find the password in the output
    password_match = password_pattern.search(output)
    
    if password_match:
        return password_match.group(1)
    else:
        return 'Password not found'

# Main function to display wireless networks and their passwords
def main():
    networks = get_wireless_networks()
    for network in networks:
        ssid, network_type, authentication, encryption, bssid, signal, radio_type, channel, basic_rates, other_rates, network_id = network
        password = get_network_password(ssid)
        print(f'SSID: {ssid}')
        print(f'Password: {password}')
        print('---')

# Run the main function
if __name__ == '__main__':
    main()