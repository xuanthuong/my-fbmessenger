#  -*- coding: utf-8 -*-
"""
Practice on creating facebook messenger bot
reference: 

Date: Aug 05, 2017
@author: Thuong Tran
Description: Create some message for Amaris
"""


msg_welcome = "attachment" : {
  "type": "template",
  "payload": {
    "template_type": "generic",
    "elements": [
      {
        "title": "Welcome to Amaris",
        "image_url": "https://amaris.com/Sitefinity/WebsiteTemplates/AmarisWebsiteTemplate/App_Themes/AmarisWebsite/imgs/logo_amaris.png",
        "subtitle": '''Amaris is an independent Technology and Management Consulting Group 
                      with high added-value consulting services on an international level''',
        "default_action": {
          "type": "web_url",
          "url": "https://amaris.com",
          "messenger_extensions": True,
          "webview_height_ratio": "tall",
          "fallback_url": "https://amaris.com"
        },
        "buttons":[
          {
            "type": "web_url",
            "url": "https://amaris.com",
            "title": "View Website"
          },{
            "type": "postback",
            "title": "Start Chatting",
            "payload": "DEVELOPER_DEFINED_PAYLOAD"
          }              
        ]      
      }
    ]
  }}

msg_quick_topics = {
  "text": "Please choose quick topics:",
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
  ]}

msg_insight = "attachment" : {
  "type":"template",
  "payload":{
    "template_type":"generic",
    "elements":[
      {
        "title":"Discover the interview of Olivier Brourhant in Le Temps",
        "image_url":"",
        "subtitle":"Olivier Brourhant, Amaris CEO and co-founder, talks about Amaris’ success, his vision and reaching 3000 employees in only 10 years",
        "default_action": {
          "type": "web_url",
          "url": "https://amaris.com/en/amaris-website/news/news-detail/index/discover-the-interview-of-olivier-brourhant-in-le-temps",
          "messenger_extensions": True,
          "webview_height_ratio": "tall",
          "fallback_url": "https://amaris.com/en/amaris-website/news/news-detail/index/discover-the-interview-of-olivier-brourhant-in-le-temps"
        },
        "buttons":[
          {
            "type":"web_url",
            "url":"https://amaris.com/en/amaris-website/news/news-detail/index/discover-the-interview-of-olivier-brourhant-in-le-temps",
            "title":"Read more"
          }
        ]      
      },
      {
        "title":"3000 employees in Amaris, 3000 inspiring reasons to apply",
        "image_url":"",
        "subtitle":"Today we are celebrating the fact that we have reached the milestone of 3000 employees",
        "default_action": {
          "type": "web_url",
          "url": "https://amaris.com/en/amaris-website/news/news-detail/index/we-are-now-3000-inspiring-people-in-amaris-!",
          "messenger_extensions": True,
          "webview_height_ratio": "tall",
          "fallback_url": "https://amaris.com/en/amaris-website/news/news-detail/index/we-are-now-3000-inspiring-people-in-amaris-!"
        },
        "buttons":[
          {
            "type":"web_url",
            "url":"https://amaris.com/en/amaris-website/news/news-detail/index/we-are-now-3000-inspiring-people-in-amaris-!",
            "title":"Read more"
          }
        ]      
      },
      {
        "title":"Our offices have been ISO27001 Certified",
        "image_url":"",
        "subtitle":"Another proof that we are a reliable asset for our clients, especially on Information Security.",
        "default_action": {
          "type": "web_url",
          "url": "https://amaris.com/en/amaris-website/news/news-detail/index/our-offices-have-been-iso27001-certified-!",
          "messenger_extensions": True,
          "webview_height_ratio": "tall",
          "fallback_url": "https://amaris.com/en/amaris-website/news/news-detail/index/our-offices-have-been-iso27001-certified-!"
        },
        "buttons":[
          {
            "type":"web_url",
            "url":"https://amaris.com/en/amaris-website/news/news-detail/index/our-offices-have-been-iso27001-certified-!",
            "title":"Read more"
          }
        ]      
      }
    ]
  }}

msg_media = "attachment" : {
  "type": "template",
  "payload": {
    "template_type": "generic",
    "elements": [
      {
        "title": "Interview of Olivier Brourhant in Lyon Décideurs",
        "default_action": {
          "type": "web_url",
          "url": "https://youtube.com/watch?v=niOEF3H_lVc",
          "messenger_extensions": True
        },
        "buttons":[
          {
            "type": "web_url",
            "url": "https://youtube.com/watch?v=niOEF3H_lVc",
            "title": "View On Youtube"
          },
          {
            "type":"web_url",
            "url":"https://amaris.com",
            "title":"Read more"
          } 
        ]      
      },
      {
        "title": "Amaris Foundation: I-Clown project",
        "default_action": {
          "type": "web_url",
          "url": "https://youtube.com/watch?v=hM2ZuhWyOGU",
          "messenger_extensions": True
        },
        "buttons":[
          {
            "type": "web_url",
            "url": "https://youtube.com/watch?v=hM2ZuhWyOGU",
            "title": "View On Youtube"
          },
          {
            "type":"web_url",
            "url":"https://amaris.com",
            "title":"Read more"
          }              
        ]      
      }
    ]
  }}

msg_expertise = "attachment" : {
  "type": "template",
  "payload": {
    "template_type": "generic",
    "elements": [
      {
        "title": "Overview",
        "default_action": {
          "type": "web_url",
          "url": "https://amaris.com/amaris-website/our-expertises/overview",
          "messenger_extensions": True
        },
        "buttons":[
          {
            "type": "web_url",
            "url": "https://amaris.com/amaris-website/our-expertises/overview",
            "title": "Read more"
          }
        ]      
      },
      {
        "title": "Business Management and Consulting",
        "default_action": {
          "type": "web_url",
          "url": "https://amaris.com/amaris-website/our-expertises/business-and-management-consulting",
          "messenger_extensions": True
        },
        "buttons":[
          {
            "type": "web_url",
            "url": "https://amaris.com/amaris-website/our-expertises/business-and-management-consulting",
            "title": "Read more"
          }            
        ]      
      }
    ]
  }}

def get_msg_amaris_welcome():
  return msg_welcome

def get_msg_quick_topic():
  return msg_quick_topics

def get_msg_amaris_insight():
  return msg_insight

def get_msg_amaris_media():
  return msg_media

def get_msg_amaris_expertise():
  return msg_abc

def get_msg_amaris_solution():
  return msg_abc