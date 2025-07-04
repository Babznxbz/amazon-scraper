from flask import Flask, request, render_template
import requests

app = Flask(__name__)

N8N_WEBHOOK_URL = "https://addo11111.app.n8n.cloud/webhook-test/amazon-scraper"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['product_url']
        try:
            response = requests.post(N8N_WEBHOOK_URL, json={"url": url})
            if response.status_code == 200:
                result = response.json()
            else:
                result = {"error": "n8n did not return 200 OK"}
        except Exception as e:
            result = {"error": str(e)}
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
