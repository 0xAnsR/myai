from flask import Flask, request, jsonify
import openai  # Make sure to install the OpenAI library

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/process_task', methods=['POST'])
def process_task():
    task = request.json.get('task')
    # Use OpenAI's API to process the task (e.g., filtering, reminders)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": task}]
    )
    return jsonify(response.choices[0].message['content'])

if __name__ == '__main__':
    app.run(debug=True)