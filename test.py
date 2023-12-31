from flask import Flask, render_template, request

# from transformers import pipeline, set_seed

app = Flask(__name__)

# # Set up the text generation pipeline with GPT-2 model
# text_generator = pipeline("text-generation")
# set_seed(42)  # Optional: Set a seed for reproducibility


@app.route("/")
def index():
    return render_template("traits.html")


@app.route("/generate", methods=["POST"])
def generate():
    # if request.method == "POST":
    #     prompt = request.form["prompt"]
    #     # Generate text using GPT-2 based on the provided prompt
    #     # generated_text = text_generator(prompt, max_length=50, num_return_sequences=1)
    #     generated_text = generated_text[0]["generated_text"]
    return render_template("professions.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
