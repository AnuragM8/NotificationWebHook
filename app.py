from flask import Flask, request, jsonify, abort
import requests
import json

app = Flask(__name__)

@app.route("/api/notifications", methods=["POST"])
def notifications():
    data = request.json
    # Handle validation tokens during subscription creation
    if "validationToken" in request.args:
        # Respond with the validation token (required for subscription validation)
        return request.args.get("validationToken")

    # Notifications from MS Graph come as a list under "value"
    notifications = data.get("value", [])
    for notification in notifications:
        print("notification:",notification)
        resource = notification.get("resource", "")
        # Expect resource format: chats/{chat-id}/messages/{message-id}
        parts = resource.split('/')
        if len(parts) >= 4:
            chat_id = parts[1]
            message_id = parts[3]

            print(f"Received notification for chat: {chat_id}, message: {message_id}")

            # Get full message details
            # message_json = get_message_details(chat_id, message_id)
            # if not message_json:
            #     continue

            # # Check if app mentioned
            # # if is_mentioned(message_json):
            # question = extract_question(message_json)
            # print(f"Extracted question: {question}")

            # # Call your LLM
            # answer = call_llm(question)
            # print(f"LLM answer: {answer}")

            # # Send reply back to chat
            # send_reply(chat_id, answer)

    return jsonify({"status": "received"}), 202


if __name__ == "__main__":
    app.run(port=5000)