import requests, sys
headers = {
    'x-wormgpt-provider': 'worm_gpt',
    'Content-Type': 'application/json',
}
json_data = {
    'messages': [
        {
            'role': 'user',
            'content': sys.argv,
        },
    ],
    'max_tokens': 8200990,
}
response = requests.post('https://wrmgpt.com/v1/chat/completions', headers=headers, json=json_data)
print(response.json()['choices'][0]['message']['content'])
