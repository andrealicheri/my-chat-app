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
        "date": str(datetime.now().strftime("%d %m - %H:%M"))
    }
    print(database_post(message_path, data))
    return "OK"

@app.route("/board")
def serve():
    data = json.loads(database_get("messages?page-size=20").replace("'", '"'))
    html_messages = []
    messages = [(value['date'], value['message']) for key, value in data['data'].items()]
    messages.sort(key=lambda x: x[0])

    for date, message in messages:
        formatted_message = f"{date} - {message}"
        html_message = f"<article><p>{formatted_message}</p></article>"
        html_messages.append(html_message)

    html_output = ''.join(html_messages)

    return html_output

if __name__ == "__main__":
    load_dotenv(".env")
    app.run(debug=True)