__author__ = 'jmh081701'
import get_reg_value
import os
def get_software():
    rst_list = get_reg_value.get_all_installed_software()
    rst =[]
    for each in rst_list:
        rst.append(each[0])
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
        os.system(uninstall_string)
if __name__ == '__main__':
    uninstall_software("USBPcap 1.2.0.4")