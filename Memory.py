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
    sys_mem_arr=[]

    for part in psutil.disk_partitions(all=False):
        if part.fstype == '':
            continue

        y=""
        mem_usage+=psutil.disk_usage(part.mountpoint)        #stores memory as (total,used,free,percent)
        y=''.join(part.device)

        sys_mem = {'Total': bytes_norm(psutil.disk_usage(part.mountpoint).total), 'Used':bytes_norm(psutil.disk_usage(part.mountpoint).used),
                   'Free':bytes_norm(psutil.disk_usage(part.mountpoint).free), 'Percent':psutil.disk_usage(part.mountpoint).percent,
                   'Device': y}

        sys_mem_arr.append(sys_mem)



    print(sys_mem_arr)

    it=iter(mem_usage)
    mem_usage=(list(zip(it,it,it,it)))





if __name__=="__main__": main()



#create platform.uname() to dict