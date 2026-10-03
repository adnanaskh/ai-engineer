import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from groq import Groq

load_dotenv()



prompt = "Create a list of 7 wonders."

saved_data = {
    "prompt": prompt,
    "timestamp": datetime.now().isoformat(),
    "responses": {
        "gemini": None,
        "groq": None
    }
}





print("---Requesting Gemeini---")

gemini_client = genai.Client()


for attempt in range(3):
    try:
        gemini_response = gemini_client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt,
        )

        print("Gemini Response: ")
        print(gemini_response.text)

        saved_data["responses"]["gemini"] = gemini_response.text
        break
    except Exception as e:
        if "503" in str(e) and attempt < 2:
            print(f"Gemini servers busy (503). Retrying in 3 seconds... (Attempt {attempt+1}/3)")
            time.sleep(3)
            continue
        print(f"Gemini Error: Servers are under heavy load. Skipping to Groq...")
        print(f"Details: {e}")
        break


print("\n" + "="*40+ "\n")


groq_client = Groq()

try:
    groq_response = groq_client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content" : str(prompt)
            }
            
        ],
    )

    print("GROQ RESPONSE: ")
    print(groq_response.choices[0].message.content)
    saved_data["responses"]["groq"] = groq_response.choices[0].message.content


except Exception as e:
    print(f"Froq error: {e}" )
