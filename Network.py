import psutil

network_arr=[]
temp=[]

temp=psutil.net_io_counters(pernic=True)

for nic in psutil.net_io_counters(pernic=True):
    x={'NIC':nic,'Bytes sent': temp[nic].bytes_sent,'Bytes received':temp[nic].bytes_recv,'Packets Sent':temp[nic].packets_sent,
       'Packet received':temp[nic].packets_recv}
    network_arr.append(x)


print(network_arr)

