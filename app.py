import requests
import json
import gradio as gr


url="http://localhost:11434/api/generate"

headers={
    "Content-type": "application/json"
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt='\n'.join(history)
    data={
        "model":"codehelper",
        "prompt":final_prompt,
        "stream": False
    }

    response=requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error : ",response.text)

interface=gr.Interface(
    title='Multi Programming Code Assistant App Using CodeLlama',
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder='Enter yot Prompt'),
    outputs='text'
)

interface.launch()