from flask import Flask, request, jsonify
import requests
import json
import logging
 
# Configure logging
logging.basicConfig(
    level=logging.INFO,  # You can change to DEBUG for more details
    format="%(asctime)s [%(levelname)s] %(message)s",
)
 
app = Flask(__name__)
app.debug = True 
@app.route("/api/notifications", methods=["POST"])
def notifications():
    data = request.json
    logging.info(data)
 
    # Handle validation tokens during subscription creation
    if "validationToken" in request.args:
        token = request.args.get("validationToken")
        logging.info(f"Validation token received: {token}")
        return token
 
    # Notifications from MS Graph come as a list under "value"
    notifications = data.get("value", [])
    for notification in notifications:
        logging.info(f"Notification received: {notification}")
        print()
 
        resource = notification.get("resource", "")
        parts = resource.split('/')
 
        if len(parts) >= 4:
            chat_id = parts[1]
            message_id = parts[3]
            logging.info(f"Received notification for chat: {chat_id}, message: {message_id}")
 
            # Example placeholders for future functionality
            # message_json = get_message_details(chat_id, message_id)
            # if not message_json:
            #     continue
            # question = extract_question(message_json)
            # logging.info(f"Extracted question: {question}")
            # answer = call_llm(question)
            # logging.info(f"LLM answer: {answer}")
            # send_reply(chat_id, answer)
 
    return jsonify({"status": "received"}), 203
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # host="0.0.0.0" for Render compatibility