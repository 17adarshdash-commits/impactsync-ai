import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

video_file = client.files.upload(file="data/staged/phone2.mp4")

# Wait for the file to become ACTIVE before using it
while video_file.state.name == "PROCESSING":
    print("Processing video...")
    time.sleep(3)
    video_file = client.files.get(name=video_file.name)

if video_file.state.name == "FAILED":
    raise ValueError("Video processing failed")

print(f"File is {video_file.state.name}")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        video_file,
        "Identify the exact timestamp (in seconds) of the main event in this video. Return only JSON: {\"timestamp_seconds\": X, \"event\": \"description\"}"
    ]
)
print(response.text)