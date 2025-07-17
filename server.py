"""
Flask web application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the main page with the input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    """
    Analyze the text input and return formatted emotion detection result.
    Handles blank inputs with appropriate error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text_to_analyze)

        if result.get("dominant_emotion") is None:
            return "Invalid text! Please try again!"

        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return response
    except Exception as e:  # pylint: disable=broad-exception-caught
        return f"Error processing the request: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
