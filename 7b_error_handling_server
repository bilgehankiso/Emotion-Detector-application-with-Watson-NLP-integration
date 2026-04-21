"""
Flask web application server for Emotion Detector
Provides REST API endpoints to detect emotions from text input
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emotion_detection_route():
    """
    API endpoint for emotion detection
    Accepts text via 'textToAnalyze' query parameter.
    """

    # Get text from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detector
    response = emotion_detector(text_to_analyze)

    # Check for invalid input (dominant emotion is None)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return successful result in expected string format
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route('/')
def render_index_page():
    """Render main application page."""
    return "Emotion Detector is running! Send requests to /emotionDetector?textToAnalyze=..."


if __name__ == '__main__':
    # Run the Flask server
    app.run(host='0.0.0.0', port=5000, debug=True)
