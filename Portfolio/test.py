import google.generativeai as genai

# Use your actual API key here
genai.configure(api_key="AIzaSyAr7V8xbKjceqP0tf0X_OdEL8bg1ON6qVk")

models = genai.list_models()

for model in models:
    print(model.name)