from flask import Flask, request, jsonify
from ai_engine import analyze_message

app = Flask(__name__)

# Slack challenge verification
@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    # Slack URL verification during initial setup
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # Process Slack events
    event = data.get("event", {})

    # We only want human messages (ignore bot messages)
    if event.get("type") == "message" and "bot_id" not in event:
        user = event.get("user")
        text = event.get("text")
        channel = event.get("channel")

        print("\n🔔 Received Slack Message:")
        print("User:", user)
        print("Message:", text)
        print("Channel:", channel)

        # ---- AI ANALYSIS ----
        try:
            analysis = analyze_message(text)

            print("\n🤖 AI Analysis:")
            print(analysis)

            return jsonify({
                "status": "AI analysis complete",
                "analysis": analysis
            }), 200

        except Exception as e:
            print("\n❌ AI Error:", str(e))
            return jsonify({"error": "AI processing failed"}), 500

    return jsonify({"status": "ignored"}), 200


if __name__ == "__main__":
    app.run(port=5000)