import os
import sys
import json

import requests
from flask import Flask, request
import apiai
from amaris_demo_msg import get_msg_amaris_welcome, get_msg_quick_topic, get_msg_amaris_map
from amaris_demo_msg import get_msg_amaris_insight, get_msg_amaris_media, get_msg_amaris_expertise

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
          # log(message_text)
          ### Get message from somewhere -- important
          response_msg = process_received_msg(message_text)
          ### 
          # response_msg = {
          #   "type":"image",
          #   "payload":{
          #     "url":"https://saltmarshrunning.com/wp-content/uploads/2014/09/bananasf.jpg"
          #   }}
          send_message(sender_id, response_msg)

        if messaging_event.get("delivery"):  # delivery confirmation
          pass

        if messaging_event.get("optin"):  # optin confirmation
          pass

        if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
          sender_id = messaging_event["sender"]["id"]
          recipient_id = messaging_event["recipient"]["id"]
          message_text = messaging_event["postback"]["title"]

          response_msg = process_received_msg(message_text)
          send_message(sender_id, response_msg)

  return "ok", 200

def process_received_msg(msg):
  if msg.lower() == "get started":
    return get_msg_amaris_welcome()
  elif msg.lower() == "start chatting":
    return get_msg_quick_topic()
  elif msg.lower() == "insight":
    return get_msg_amaris_insight()
  elif msg.lower() == "media":
    return get_msg_amaris_media()
  elif msg.lower() == "expertise":
    return get_msg_amaris_expertise()
  elif msg.lower() == "where is Amaris Vietnam?" or msg.lower() == "show me Amaris Vietnam address":
    return get_msg_amaris_map()
      

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
      "message": message_text
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