from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# ✅ Use production webhook URL (no "-test")
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/amazon-scraper"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('product_url')
        try:
            print(f"📡 Sending URL to: {N8N_WEBHOOK_URL}")
            # 🔑 Wait here until n8n finishes and returns response
            response = requests.post(N8N_WEBHOOK_URL, json={"url": url}, timeout=180)

            if response.status_code == 200:
                try:
                    result = response.json()  # show final JSON result
                except Exception:
                    result = {"message": "✔️ Workflow finished successfully."}
            else:
                result = {"error": f"❌ n8n returned status {response.status_code}"}
        except Exception as e:
            result = {"error": str(e)}

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
