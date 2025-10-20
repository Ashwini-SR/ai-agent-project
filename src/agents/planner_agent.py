from openai import OpenAI

def plan_content(topic, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert content strategist."},
            {"role": "user", "content": f"Create a 3-point content plan about {topic} for social media."}
        ]
    )
    return response.choices[0].message.content
