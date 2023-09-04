from flask import Flask, render_template, request
import requests
import os

def create_app():
    app = Flask(__name__)
    @app.route('/', methods=['GET', 'POST'])
    def index():
        question = None
        answer = None
        if request.method == 'POST':
            
            topic = request.form.get('topic')
            
            # Check if the topic exists in the form
            if topic:
                question, answer = get_trivia_question(topic)
            
            return render_template('index.html', question=question, answer=answer)
        
        
        return render_template('index.html', question=question, answer=answer)
    return app

def get_trivia_question(topic):
    api_key = os.getenv('TRIVIA_API_KEY')
    headers = {'X-Api-Key': api_key}
    response = requests.get(f'https://api.api-ninjas.com/v1/trivia?category={topic}', headers=headers)
    data = response.json()
    print("api_key: ", api_key)
    print("data type: ", data)
    return data[0]['question'], data[0]['answer']
    

if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
