import nmap



banner = """
 \      \   _____ _____  ______  
 /   |   \ /     \\__  \ \____ \ 
/    |    \  Y Y  \/ __ \|  |_> >
\____|__  /__|_|  (____  /   __/ 
        \/      \/     \/|__|    
    #SCANNER        
        """
print(banner)
scanner = nmap.PortScanner()
print("Version : ",scanner.nmap_version)


ip_address = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_address)
type(ip_address)
resp = input(""" \n Please enter the type of scan you want to run
                1)SYN ACK-Scan
                2)UDP Scan
                3)Comprehensive Scan\n""")

print("You have selected option: ",resp)

options = """\nPlease enter the type of scan you want to run
                1)SYN ACK-Scan
                2)UDP Scan
                3)Comprehensive Scan\n"""
while True:
    print("*****Please prees 'q' or write 'exit' for exit loop*****")
    
    
    
    if resp == "1":
        print("Nmap version: ", scanner.nmap_version)
        scanner.scan(ip_address, "1-1024", "-v -sS")
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_address].state)
        print(scanner[ip_address].all_protocols())
        print("Open Ports: ",scanner[ip_address]["tcp"].keys())
    
    elif resp == "2":
        print("Nmap version: ", scanner.nmap_version)
        scanner.scan(ip_address, "1-1024", "-v -sU")
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_address].state)
        print(scanner[ip_address].all_protocols())
        print("Open Ports: ",scanner[ip_address]["udp"].keys())
    
    elif resp == "3":  
        print("Nmap version: ", scanner.nmap_version)
        scanner.scan(ip_address, "1-1024", "-v -sS -sV -sC -A -O")
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_address].state)
        print(scanner[ip_address].all_protocols())
        print("Open Ports: ",scanner[ip_address]["tcp"].keys())

    elif resp == "q" or "Q":
        print("Exiting the program")
        break
    
    elif resp == "exit" or "EXIT":
        print("Exiting the program")
        break
    
    else:
        print("There is no option like this")
        print(options)