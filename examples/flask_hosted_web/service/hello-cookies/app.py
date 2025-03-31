from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def return_index():
    cookie = request.cookies.get('auth')
    if cookie == 'test':
        return "LNC25{co0KIe_mANIpulAT10N}"
    else:
        if "auth" not in request.cookies:
            resp = make_response("Current cookie value: 'freshie'\nThe flag is only available for people with cookie values of 'test' sorry.")
            resp.set_cookie('auth', 'freshie')
            return resp
        else:
            return(f"Current cookie value: '{cookie}'\nThe flag is only available for people with cookie values of 'test' sorry.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
