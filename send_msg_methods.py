#  -*- coding: utf-8 -*-
"""
Practice on creating facebook messenger bot
reference: 

Date: Aug 05, 2017
@author: Thuong Tran
Description: create general function for sending different of messages that fb support
"""


def get_image_msg(url, file_upload):
  msg = "No image"
  if (url):
    msg = {
      "type":"image",
      "payload": {
        "url":"https://petersapparel.com/img/shirt.png"
      }}
  elif (file_upload):
    msg = {
      "type": "image", "payload":{},
      'filedata = @/tmp/shirt.png; type=image/png'
    }
  return msg


def get_video_msg():
  pass # same with image, "type": "video"
def get_audio_msg():
  pass # same with image, "type": "audio"
def get_file_msg():
  pass # same with image, "type": "file"


def get_generic_template_msg():
  msg = {
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
  return msg
  
def get_quick_reply_msg():
  msg = {
    "text": "Quick topics:",
    "quick_replies":[
      {
        "content_type": "text",
        "title": "Insight",
        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_INSIGHT"
      },
      {
        "content_type": "text",
        "title": "Media",
        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_MEDIA"
      },
      {
        "content_type": "text",
        "title": "Others",
        "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_OTHER_CHATTING"
      }
    ]
  }
  return msg