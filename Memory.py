<<<<<<< HEAD
import psutil
import sys
import platform

def bytes_norm(n):
    symbols = ('K', 'M', 'G', 'T')
    prefix = {}

    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10

    for i in reversed(symbols):
        if (n >= prefix[i]):
            value = float(n) / prefix[i]
            return '%.2f%s' % (value, i)
    return '%sB' % n


def main():

    x=[]
    mem_usage=[]


    for part in psutil.disk_partitions(all=False):
        if part.fstype == '':
            continue

        x+=part.device                                      #stores device names

        mem_usage+=psutil.disk_usage(part.mountpoint)        #stores memory as (total,used,free,percent)
        a=psutil.disk_usage(part.mountpoint).total
        b=bytes_norm(a)


    it=iter(mem_usage)
    mem_usage=(list(zip(it,it,it,it)))
    print(x)
    print(mem_usage)
    print(platform.uname())



if __name__=="__main__": main()
=======
import platform
import psutil
import sys

def bytes_norm(n):
    symbols = ('K', 'M', 'G', 'T')
    prefix = {}

    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10

    for i in reversed(symbols):
        if (n >= prefix[i]):
            value = float(n) / prefix[i]
            return '%.2f%s' % (value, i)
    return '%sB' % n


def main():

    mem_usage=[]
    sys_info_arr = []
    os_arr = []

    for part in psutil.disk_partitions(all=False):
        if part.fstype == '':
            continue

        y = ""
        mem_usage += psutil.disk_usage(part.mountpoint)  # stores memory as (total,used,free,percent)
        y = ''.join(part.device)

        sys_info = {'Total': bytes_norm(psutil.disk_usage(part.mountpoint).total),
                    'Used': bytes_norm(psutil.disk_usage(part.mountpoint).used),
                    'Free': bytes_norm(psutil.disk_usage(part.mountpoint).free),
                    'Percent': psutil.disk_usage(part.mountpoint).percent,
                    'Device': y}

        sys_info_arr.append(sys_info)  # sys_info_arr stores memory details of each physical drive

        os_arr.append({'OS ': ' '.join([platform.uname().system, platform.uname().release])})
        os_arr.append(sys_info_arr)  # os_arr contains os details in first element, second element is sys_info_arr

    print(os_arr)

if __name__=="__main__": main()

