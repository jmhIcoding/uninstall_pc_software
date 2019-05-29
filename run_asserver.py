__author__ = 'jmh081701'
import  flask
from flask import  Flask
from flask import jsonify
from flask import request
from util import  *
import  pyautogui as pag
def __cache__server__():
    app=Flask(__name__)
    
    @app.route("/uninstall",methods=["POST"])
    def getdata():
        rst={}
        uninstall_string = None
        if not request.json:
            return jsonify({"msg":"Needed Json Request"})
        #try:
            '''
            {'app':'chrome'}
            '''
        else:
            inputJson = request.json
            ap = inputJson['app']
            softwares = get_software()
            for each in softwares:
                #print(each)
                if ap in each:
                    print("uninstall %s"%ap)
                    uninstall_string = each
                    break
                    #return jsonify({'msg':'success'})
            
        #except:
        if uninstall_string != None:
            uninstall_software(uninstall_string)
            return jsonify({'msg':'success'})
        return jsonify({'msg':'error'})
    
    @app.route("/typewrite",methods=["POST"])
    def typewrite():
        rst={}
        uninstall_string = None
        if not request.json or "typemsg" not in request.json:
            return jsonify({"msg":"Needed Json Request"})
        #try:
            '''
            {'typemsg':'www.baidu.com'}
            '''
        else:
            inputJson = request.json
            string = inputJson['typemsg']
            pag.typewrite(string)

        #except:
        if uninstall_string != None:
            uninstall_software(uninstall_string)
            return jsonify({'msg':'success'})
        return jsonify({'msg':'error'})
    app.run(host="0.0.0.0",port=int(9999))
if __name__ == '__main__':
    __cache__server__()