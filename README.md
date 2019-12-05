# OTP-API
A flask app with One-Time-Password related APIs. These APIs use [2factor.in](https://2factor.in) OTP provider.

### To setup your environment 
```bash
sudo pip install virtualenv
python3 -m venv flaskenv
source flaskenv/bin/activate
pip install -r requirements.txt
```

### OTP Generation API

To access this API via your browser, provide phone number with the URL. 

```bash
http://127.0.0.1:5000/api/v1/otpgen?phone=9988776655
```

### OTP Verification API

To access this API via your browser, provide phone number and OTP with the URL. 

```bash
http://127.0.0.1:5000/api/v1/otpverify?phone=9988776655&otp=123456
```

### Understanding the response of the APIs

Both the APIs provide output in JSON format with the value for the **Status** field indicating **Success** or **Error**.

Further details about the Error can be obtained using the **Details** field in the response.
