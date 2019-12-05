import flask
import http.client,json,sqlite3
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>OTP API</h1>
<p>APIs to send OTP to a specific phone number and verify the OTP</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/otpgen', methods=['GET'])
def api_otp_gen():

    query_parameters = request.args
    phone = query_parameters.get('phone')

    conn = http.client.HTTPConnection("2factor.in")
    payload = ""
    headers = { 'content-type': "application/x-www-form-urlencoded" }
    conn.request("GET", "/API/V1/4ebb88cd-173e-11ea-9fa5-0200cd936049/SMS/7019098800/AUTOGEN", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data.decode('utf-8'))

    status = json_data['Status']

    if(status == 'Success'):
        session_id = json_data['Details']
        _query = "INSERT INTO SessionID VALUES({0},'{1}')"
        conn = sqlite3.connect('sqlite.db')
        cur = conn.cursor()
        print(_query.format(phone,session_id))
        cur.execute(_query.format(phone,session_id))
        conn.commit()
        del json_data['Details']
        return json_data
    else:
        return json_data 

app.run()
