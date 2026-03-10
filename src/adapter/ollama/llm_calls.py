from ollama import chat
from src.config import settings

import logging

def call_ollama(user_message_title: str = '', user_message_content: str = '', temperature: float = 0.7):
    response = ''
    print(user_message_content)
    stream = chat(
        model=settings.OLLAMA_SETTINGS.OLLAMA_MODEL,
        messages=[
#          {
#            'role': 'user',
#            'content': '/set nothink'
#          },
          {
            'role': 'user',
            'content': f'/set parameter temperature {temperature}'
          },
          {
            'role': 'user',
            'content': user_message_content
          }
        ],
        stream=True,
    )
    i = 0
    for chunk in stream:
        response += chunk['message']['content']
        i += 1
        print(f"generating response {i}: {chunk['message']['content']}")
    return response
