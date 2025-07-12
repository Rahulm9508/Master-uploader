from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from AndySX'

@app.route('/api/cp/dl')
def classplus_proxy():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Log it
    print(f"[INFO] Got download request for: {url}")

    # For now, return the same URL for yt-dlp to pick up
    return url, 200

if __name__ == "__main__":
    app.run(port=8000)