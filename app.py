from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)
# app.run(host='127.0.0.1',port=5001)
@app.route("/")

def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def get_Chat_response(user_input):
    print("User input:", user_input.lower())  # Debugging print statement
    # Process user input related to medical queries
    # Here, we will assume that any user input containing the word "medicine" is considered a medical query
    if "hi" in user_input.lower() or "hello" in user_input.lower():
        return "Hello, welcome to our Med Express web page. How can I help you? <br>1. About this page.\n 2. Contact details.\n 3. Our features.\n 4. Our future scope.\n 5. Medicine.\n 6. Help."
    elif "about this page" in user_input.lower():
        return "Welcome to Medical Health center, where health meets technology for a brighter, healthier future.\n Here are some points about us:\n 1. Our vision.\n 2. Who we are.\n 3. Our mission.\n 4. How we do it.\n 5. Our priority"
    elif "medicine" in user_input.lower():
        # Call the medicine recommendation function to get recommended medicines based on user input
        recommendation = get_Medicine_recommendation(user_input)
        return recommendation
    else:
        # For non-medical queries, return a generic response
        return "I'm sorry, I can only provide recommendations for medical queries at the moment."



def get_Medicine_recommendation(user_input):
    # Dummy medicine recommendation logic for demonstration purposes
    recommendations = []
    
    # Process user input (e.g., symptoms or medical condition)
    # and generate medicine recommendations based on predefined rules or algorithms
    if "headache" in user_input.lower():
        recommendations.append("Aspirin")
        recommendations.append("Ibuprofen")
    if "fever" in user_input.lower():
        recommendations.append("Acetaminophen")
        recommendations.append("Paracetamol")
    if "cough" in user_input.lower():
        recommendations.append("Dextromethorphan")
        recommendations.append("Guaifenesin")
    if "Fungal" in user_input.lower():
        recommendations.append("Fluconazole")
        recommendations.append("Terbinafin")
        recommendations.append("Ketoconazole")

    # If no recommendations found, provide a generic response
    if not recommendations:
        return "I'm sorry, I couldn't find any specific medicine recommendations for your query. Please consult a healthcare professional for personalized advice."
    
    # Format and return the recommendations as a string
    return "Based on your input, here are some medicine recommendations: " + ", ".join(recommendations)

if __name__ == '__main__':
 app.run(port=5001) 
