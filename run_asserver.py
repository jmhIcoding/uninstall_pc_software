__author__ = 'jmh081701'
import  flask
from flask import  Flask
from flask import jsonify
from flask import request
from util import  *
def __cache__server__():
    app=Flask(__name__)

    @app.route("/uninstall",methods=["POST"])
    def getdata():
        rst={}
        if not request.json:
            return jsonify({"msg":"Needed Json Request"})
        try:
            '''
            {'app':'chrome'}
            '''
            inputJson = request.json
            app = inputJson['app']
            softwares = get_software()
            for each in softwares:
                print(each)
                if app in each:
                    print("uninstall %s"%app)
                    #uninstall_software(each)
                    return jsonify({'msg':'success'})
            return jsonify({'msg':'error'})
        except:
            return jsonify({"msg":"Needed correct Json Request"})

    app.run(host="0.0.0.0",port=int(9999))
if __name__ == '__main__':
    __cache__server__()