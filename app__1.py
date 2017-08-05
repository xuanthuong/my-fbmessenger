import os
import sys
import json

import requests
from flask import Flask, request
import apiai

ai = apiai.ApiAI("22b626babf6c432db11d6f6c69127fc2")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
  # when the endpoint is registered as a webhook, it must echo back
  # the 'hub.challenge' value it receives in the query arguments
  if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
    if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
      return "Verification token mismatch", 403
    return request.args["hub.challenge"], 200

  return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

  # endpoint for processing incoming messaging events

  data = request.get_json()
  log(data)  # you may not want to log every incoming message in production, but it's good for testing

  if data["object"] == "page":

    for entry in data["entry"]:
      for messaging_event in entry["messaging"]:

        if messaging_event.get("message"):  # someone sent us a message

          sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
          recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
          message_text = messaging_event["message"]["text"]  # the message's text
          
          # # Call api.ai or any other trained model -> get response text
          # # Prepare API.ai request
          # req = ai.text_request()
          # req.lang = 'en'
          # req.query = message_text
          # # Get response from API.ai
          # api_response = req.getresponse()
          # response_str = api_response.read().decode('utf-8')
          # response_obj = json.loads(response_str)
          # if 'result' in response_obj:
          #   response = response_obj["result"]["fulfillment"]["speech"]
          #   send_message(sender_id, response)
          # else:
          #   send_message(sender_id, "got it, let get started")

          message = {
                      "type":"template",
                      "payload":{
                        "template_type":"generic",
                        "elements":[
                          {
                            "title":"Welcome to Peter\'s Hats",
                            "image_url":"https://saltmarshrunning.com/wp-content/uploads/2014/09/bananasf.jpg",
                            "subtitle":"We\'ve got the right hat for everyone.",
                            "default_action": {
                              "type": "web_url",
                              "url": "https://saltmarshrunning.com",
                              "messenger_extensions": True,
                              "webview_height_ratio": "tall",
                              "fallback_url": "https://saltmarshrunning.com"
                            },
                            "buttons":[
                              {
                                "type":"web_url",
                                "url":"https://saltmarshrunning.com",
                                "title":"View Website"
                              },{
                                "type":"postback",
                                "title":"Start Chatting",
                                "payload":"DEVELOPER_DEFINED_PAYLOAD"
                              }              
                            ]      
                          }
                        ]
                      }
                  }
        
          send_message(sender_id, message)

        if messaging_event.get("delivery"):  # delivery confirmation
          pass

        if messaging_event.get("optin"):  # optin confirmation
          pass

        if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
          pass

  return "ok", 200


def send_message(recipient_id, message_text):
  
  log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

  params = {
      "access_token": os.environ["PAGE_ACCESS_TOKEN"]
  }
  headers = {
      "Content-Type": "application/json"
  }
  data = json.dumps({
      "recipient": {
          "id": recipient_id
      },
      "message": {
          "attachment": message_text
      }
  })
  r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
  if r.status_code != 200:
    log(r.status_code)
    log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
  print str(message)
  sys.stdout.flush()


if __name__ == '__main__':
  app.run(debug=True)