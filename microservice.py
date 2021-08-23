import os
from flask import Flask, request
import collapse.collapse as collapse

app = Flask(__name__)


#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /collapse?value=999999
#
@app.route('/collapse')
def dispatch():
    try:
        parm = {}
        for key in request.args:
            parm[key] = str(request.args.get(key, ''))
        value=parm.get('value',None)    
        result = collapse.collapse(value)
        return str(result)
    except:
        return str("internal error")


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))

