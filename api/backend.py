import json
from dotenv import load_dotenv
from flask import request
from api._utils.wsgi import app
from api._utils.database import database_get, database_post
from datetime import datetime

message_path = "messages"

@app.route("/message", methods=["POST"])
def messages():
    data = {
        "message": request.form.to_dict().get("chatbox"),
        "date": str(datetime.now().strftime("%H:%M"))
    }
    print(database_post(message_path, data))
    return "OK"

@app.route("/board")
def serve():
    data = json.loads(database_get("messages?page-size=20").replace("'", '"'))
    html_messages = []

    for key, value in data['data'].items():
        date = value['date']
        message = value['message']
        formatted_message = f"{date} - {message}"
        html_message = f"<p>{formatted_message}</p>"
        html_messages.insert(0, html_message)

    html_output = ''.join(html_messages)

    return html_output

if __name__ == "__main__":
    load_dotenv(".env")
    app.run(debug=True)