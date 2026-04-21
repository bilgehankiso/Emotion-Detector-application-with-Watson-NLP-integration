"""
Flask web application server for Emotion Detector
Provides REST API endpoints to detect emotions from text input
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def emotion_detection_route():
    """
    API endpoint for emotion detection

    Expected JSON payload:
    {
        "text": "Your text to analyze"
    }

    Returns:
    {
        "anger": <float>,
        "disgust": <float>,
        "fear": <float>,
        "joy": <float>,
        "sadness": <float>,
        "dominant_emotion": <str>
    }
    """

    # Get JSON data from request
    data = request.get_json()

    # Validate request has text field
    if not data or 'text' not in data:
        return jsonify({
            'error': 'No text provided',
            'message': 'Please provide text in the request body'
        }), 400

    text_to_analyze = data.get('text', '').strip()

    # Call emotion detector
    result = emotion_detector(text_to_analyze)

    # Check for error status codes
    if result.get('status_code') == 400:
        return jsonify({
            'error': 'Invalid text input',
            'message': 'Text input cannot be empty'
        }), 400

    status_code = result.get('status_code')
    if status_code != 200 and status_code is not None:
        return jsonify({
            'error': 'Analysis failed',
            'message': f'Emotion detection failed with status code {status_code}'
        }), status_code

    # Return successful result
    return jsonify({
        'anger': result.get('anger'),
        'disgust': result.get('disgust'),
        'fear': result.get('fear'),
        'joy': result.get('joy'),
        'sadness': result.get('sadness'),
        'dominant_emotion': result.get('dominant_emotion')
    }), 200


@app.route('/emotionDetectorUI', methods=['GET'])
def emotion_detection_ui():
    """
    Web UI endpoint for emotion detection
    Accepts text as query parameter
    """

    text_to_analyze = request.args.get('text', '').strip()

    # Validate input
    if not text_to_analyze:
        return '''
        <html>
            <body style="font-family: Arial, sans-serif; margin: 50px;">
                <h1>Emotion Detector</h1>
                <form method="get">
                    <label for="text">Enter text to analyze:</label><br><br>
                    <textarea id="text" name="text" rows="4" cols="50"></textarea><br><br>
                    <button type="submit">Detect Emotions</button>
                </form>
                <p style="color: red;">Error: Invalid text input.
                   Text cannot be empty.</p>
            </body>
        </html>
        ''', 400

    # Analyze emotion
    result = emotion_detector(text_to_analyze)

    # Check for errors
    if result.get('status_code') == 400:
        return '''
        <html>
            <body style="font-family: Arial, sans-serif; margin: 50px;">
                <h1>Emotion Detector</h1>
                <form method="get">
                    <label for="text">Enter text to analyze:</label><br><br>
                    <textarea id="text" name="text" rows="4"
                              cols="50"></textarea><br><br>
                    <button type="submit">Detect Emotions</button>
                </form>
                <p style="color: red;">Error: Invalid text input.
                   Text cannot be empty.</p>
            </body>
        </html>
        ''', 400

    status_code = result.get('status_code')
    if status_code != 200 and status_code is not None:
        return f'''
        <html>
            <body style="font-family: Arial, sans-serif; margin: 50px;">
                <h1>Emotion Detector</h1>
                <form method="get">
                    <label for="text">Enter text to analyze:</label><br><br>
                    <textarea id="text" name="text" rows="4"
                              cols="50"></textarea><br><br>
                    <button type="submit">Detect Emotions</button>
                </form>
                <p style="color: red;">Error: Analysis failed with status
                   code {status_code}</p>
            </body>
        </html>
        ''', status_code

    # Build results HTML
    html_response = f'''
    <html>
        <body style="font-family: Arial, sans-serif; margin: 50px;">
            <h1>Emotion Detector</h1>
            <form method="get">
                <label for="text">Enter text to analyze:</label><br><br>
                <textarea id="text" name="text" rows="4" cols="50">
                "{text_to_analyze}"</textarea><br><br>
                <button type="submit">Detect Emotions</button>
            </form>
            <h2>Results:</h2>
            <p><b>Text analyzed:</b> "{text_to_analyze}"</p>
            <p><b>Emotions detected:</b></p>
            <ul style="font-size: 16px;">
                <li><b>Anger:</b> {result.get('anger', 0):.4f}</li>
                <li><b>Disgust:</b> {result.get('disgust', 0):.4f}</li>
                <li><b>Fear:</b> {result.get('fear', 0):.4f}</li>
                <li><b>Joy:</b> {result.get('joy', 0):.4f}</li>
                <li><b>Sadness:</b> {result.get('sadness', 0):.4f}</li>
            </ul>
            <h3 style="color: green;">Dominant Emotion:
                <b>{result.get('dominant_emotion', 'Unknown').upper()}</b></h3>
        </body>
    </html>
    '''

    return html_response, 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify server is running"""
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    # Run the Flask server
    app.run(host='127.0.0.1', port=5000, debug=True)
