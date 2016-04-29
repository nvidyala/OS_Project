import platform

os_info=[]

x=platform.system()

if(x=='Windows'):
    sys_info = {'Release': platform.win32_ver()[0],
                'Version': platform.win32_ver()[1],
                'OS Type': platform.win32_ver()[3]}

    print(sys_info)

elif(x=='Linux'):
    sys_info = {'Release': platform.win32_ver()[0],
                'Version': platform.win32_ver()[1],
                'Codename': platform.win32_ver()[2]}

