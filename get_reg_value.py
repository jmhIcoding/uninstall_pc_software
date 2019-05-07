__author__ = 'jmh081701'
import win32api,win32con

def get_all_installed_software():
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_paths=[r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",r"Software\Microsoft\Windows\CurrentVersion\Uninstall"]
    rst_list=[]
    for path in reg_paths:
        pkey = win32api.RegOpenKeyEx(reg_root,path)
        for item in win32api.RegEnumKeyEx(pkey):
            value_paths = path+"\\"+item[0]
            #print(value_paths)
            try:
                vkey = win32api.RegOpenKeyEx(reg_root,value_paths)
                DisplayName,key_type = win32api.RegQueryValueEx(vkey,"DisplayName")
                UninstallString,key_type = win32api.RegQueryValueEx(vkey,"UninstallString")
                #print({'name':DisplayName,'Uninstall string':UninstallString})
                rst_list.append((DisplayName,UninstallString))
                win32api.RegCloseKey(vkey)
            except:
                pass
        win32api.RegCloseKey(pkey)
    return rst_list
if __name__ == '__main__':
    software=get_all_installed_software()
    print(software)