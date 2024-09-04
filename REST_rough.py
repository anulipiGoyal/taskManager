from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<int:n>')
def armstrong(n):
    Tsum=0
    order = len(str(n))
    copyN = n
    while(n>0):
        digit = n%10
        Tsum += digit ** order
        n = n//10
    
    if (Tsum == copyN):
        print(f"{copyN} is an armstrong number")
        result = {
            "Number" : copyN,
            "Armstrong": True,
            "Server IP": "122.126.98.000",
            "Other Numbers": [123,789,5656]
        }
    else:
        print(f"{copyN} is NOT an armstrong number")
        result = {
            "Number" : copyN,
            "Armstrong": False,
            "Server IP": "122.126.98.000"
        }
    return jsonify(result)
    



if __name__ == '__main__':
    app.run()   