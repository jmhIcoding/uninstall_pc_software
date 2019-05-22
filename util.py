__author__ = 'jmh081701'
import get_reg_value
import os
import subprocess
def get_software():
    rst_list = get_reg_value.get_all_installed_software()
    rst =[]
    for each in rst_list:
        rst.append(each[0])
    return  rst
def uninstall_software(software_name):
    rst_list = get_reg_value.get_all_installed_software()
    uninstall_string=""
    for each in rst_list:
        if each[0] == software_name:
            uninstall_string=each[1]
            break
    if uninstall_string=="":
        print("Not found installed program.")
        return
    else:
        print("uninstall "+ software_name)
        uninstall_string = uninstall_string.replace('\\','\\\\')
        os.chdir("\\".join(uninstall_string.split('\\')[:-1]))
        cmd=uninstall_string.split('\\')[-1]
        print(cmd)
        subprocess.Popen("",executable=cmd)
