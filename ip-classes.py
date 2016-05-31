ip = raw_input('Enter IP: ')

def ip_class(ip):

    print "You entered: %s" % ip
    stripped_ip = ip.split(".")
    oct1 = stripped_ip[0]
    oct2 = stripped_ip[1]
    oct3 = stripped_ip[2]
    oct4 = stripped_ip[3]
    if int(oct1) >=256 or int(oct2) >=256 or int(oct3) >=256 or int(oct4) >= 256:
        print "Invalid IP, try again"
    print type(oct1)
    print "Individual Octets are ", oct1, oct2, oct3, oct4
    print "Octet Lengths are", int(len(oct1)), int(len(oct2)), int(len(oct3)), \
    int(len(oct4))
    print type(stripped_ip)

    # A class, before the private 10.x.x.x range
    if int(oct1) in range(1,10):
        print "%s is an A class IP" % ip
    # Private A class
    elif int(oct1) == 10:
        print "%s is a Private A class IP" %ip
    # remainder of A class after private 10.x.x.x range
    elif int(oct1) in range(11, 127):
        print "%s is an A class IP" % ip
    # loopback
    elif int(oct1) == 127:
        print "%s is a Localhost (Loopback) IP" % ip
    # APIPA
    elif int(oct1) == 169 and  int(oct2) == 254:
        print "%s is an APIPA IP" %ip
    # B Class, beginning of B class 128.x.x.x thru 171.x.x.x
    elif int(oct1) in range(128,172):
        print "%s is a B class IP" % ip
    # B class 172.0.x.x thru 172.15.x.x
    elif int(oct1) == 172 and int(oct2) in range(0,16):
        print "%s is a B class IP" %ip
    # Private B class 172.16.x.x thru 172.31.x.x
    elif int(oct1) == 172 and int(oct2) in range(16,32):
        print "%s is a Private B class IP" % ip
    # Resuming B class after the private 172.16.x.x thru 172.31.x.x range
    elif int(oct1) == 172 and int(oct2) in range(32,256):
        print "%s is a B class IP" %ip

    # C class, before the private ip range, so 192.0-167
    elif int(oct1) == 192 and int(oct2) in range(0, 168):
        print "%s is a C class IP" % ip
    # The entire Private C class, 192.168.all.all
    elif int(oct1) == 192 and int(oct2) == 168 :
        print "%s is a private C class IP" % ip
    # C class, finishing off 192.169.x.x thru 192.255.x.x
    elif int(oct1) == 192 and int(oct2) in range(169, 256):
        print "%s is a C Class IP" % ip
    # C class, remainder of 193.x.x.x thru 223.255.255.255
    elif int(oct1) in range(193, 224):
        print "%s is a C class IP (193.xxx - 223)" % ip
    # D class
    elif int(oct1) in range(224,240):
        print "%s is a D class IP (Multicast)" %ip
    # E class
    elif int(oct1) in range(240, 255):
        print "%s is an E class IP (Experimental)" % ip
    else:
        print "%s is not a valid IP" % ip


ip_class(ip)