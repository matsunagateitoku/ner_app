# app.py
from flask import Flask, render_template, request
from text_utils import extract_named_entities
import logging

# Set up logging for the Flask app
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    named_entities = None
    displacy_html = None
    
    if request.method == "POST":
        input_text = request.form.get("user_input")
        
        if input_text:
            logging.debug(f"Received input: {input_text}")
            named_entities, displacy_html = extract_named_entities(input_text)
            if named_entities is None:
                named_entities = [("Error", "Unable to process the text.")]
    
    return render_template("index.html", named_entities=named_entities, displacy_html=displacy_html)

if __name__ == "__main__":
    logging.debug("Starting Flask app...")
    app.run(debug=True)
