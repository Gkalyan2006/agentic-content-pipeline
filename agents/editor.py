from groq import Groq

client = Groq(api_key="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")

def editor_agent(article):

    prompt = f"""
    You are professional content editor.
    Apply brand voice:

     - Friendly
     - Educational
     - Motivational.

    Rewrite to professional publication quality.
    Keep meaning same.Remove unrealistic claims.
    Fix grammar and clarity.

    Article:
    {article}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
