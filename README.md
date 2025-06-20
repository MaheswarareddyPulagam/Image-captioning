# Image-captioning
# 📸 AI Image Caption Generator using Gemini Pro Vision

Welcome to the **AI Image Caption Generator** — a web app that uses Google’s **Gemini Pro Vision** model to generate creative captions for any image you upload.

---

## 🌟 Features

- 🤖 AI-generated captions powered by Gemini Vision
- 🖼 Upload `.jpg`, `.jpeg`, or `.png` images
- ✍️ Add an optional text prompt to guide the caption's tone or style (e.g., "funny", "motivational")
- ⚡ Instant response with ready-to-use social media captions
- 🌐 Built with **Python**, **Streamlit**, and **Google Generative AI**

---

## 🧠 How It Works

1. The user uploads an image.
2. Optionally enters a text prompt (e.g., style or tone).
3. The image and prompt are passed to Gemini Vision.
4. Gemini generates a human-like caption based on both image content and the prompt.
5. The app displays the caption instantly.

---

## 📁 Project Structure

├── app.py # Main Streamlit app
├── util.py # Model initialization & caption generation logic
├── .env # Stores your Google API Key (not committed to GitHub)
├── requirements.txt # Python dependencies
##Install Dependencies
using command :pip install -r requirements.txt
##Set Up API Key
GOOGLE_API_KEY=your_google_api_key_here
##Run the App
streamlit run app.py
