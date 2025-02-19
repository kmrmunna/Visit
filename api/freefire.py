from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

# Your Free Fire token linked to your ID
MY_TOKEN = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxMTA5Mzk1MjAzNSwibmlja25hbWUiOiJURVNUX19fXzki..."

def send_request():
    url = "https://client.ind.freefiremobile.com/GetPlayerPersonalShow"
    edata = bytes.fromhex("01383008d4508a02e91abed9902b3fd9")
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Authorization': f"Bearer {MY_TOKEN}",
        'Content-Type': "application/x-www-form-urlencoded",
        'Expect': "100-continue",
        'X-Unity-Version': "2018.4.11f1",
        'X-GA': "v1 1",
        'ReleaseVersion': "OB47"
    }
    response = requests.post(url, edata, headers=headers)
    return response.json(), response.status_code


@app.route('/api/freefire', methods=['GET'])
def freefire_api():
    results = []
    for i in range(5):  # Loop runs 5 times
        data, status = send_request()
        results.append({"attempt": i + 1, "response": data})
        time.sleep(2)  # Delay of 2 seconds between requests
    return jsonify({"loop_results": results}), 200


if __name__ == "__main__":
    app.run()
