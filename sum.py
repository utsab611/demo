from flask import Flask,jsonify,request 
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def toThePower():
    number = request.args['number']
    print(type(number))
    square = (int(number)**2)
    cube = (int(number)**3)
    

    #print(number)
    return jsonify({"data":[{"square":square,"cube":cube}]})

@app.route('/sum',methods = ['POST','GET'])
def getSum():
    number = request.get_json()
    first_number=number['first_number']
    second_number=number['second_number']
    print(type(first_number))
    sum = first_number + second_number
    print(number)
    return jsonify({"data":[{"sum":sum}]})
    



if __name__ =="__main__":
    app.run(debug=True) 
