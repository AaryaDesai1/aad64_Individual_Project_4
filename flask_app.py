from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
import os
import openai

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def home():
    return render_template("traits.html", title="Home")


def get_top_professions(traits, model="text-davinci-003"):
    prompt = f"I am skilled at {traits}. What are the top professions for me?"

    prompt_answer = f"""
    Considering my skills: {traits}, which professions align best with my abilities?
    ```{prompt}```
    """

    print(prompt_answer)

    messages = [{"role": "user", "content": prompt_answer}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
        max_tokens=100,
        stop=None,
    )

    return response.choices[0].message["content"]


@app.route("/traits")
def traits():
    result = request.args.get("traits", "")
    print(result)
    return render_template("traits.html", result=result)


@app.route("/predict", methods=["POST"])
def predict():
    prompt = request.form.get("prompt")
    result = get_top_professions(prompt)
    return redirect(url_for("result", result=result))


@app.route("/result")
def result():
    result = request.args.get("result", "")
    return render_template("professions.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
