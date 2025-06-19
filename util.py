import google.generativeai as genai
from PIL import Image

def init_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-2.5-flash")  # ✅ Use updated model name


def generate_caption(model, image_file, prompt="Describe this image for social media"):
    try:
        image = Image.open(image_file)
        response = model.generate_content([image, prompt])
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

