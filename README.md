# Final Project: Emotion Detector

An AI-powered emotion detection web application built with Flask and IBM Watson NLP library.

## Overview

Emotion Detector is a Python-based web application that analyzes text input to detect and classify emotions. It uses IBM Watson NLP library to identify five key emotions:
- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

## Features

- **Emotion Detection**: Analyzes text and returns emotion scores
- **Dominant Emotion**: Identifies the most prominent emotion in text
- **REST API**: JSON-based API for integration
- **Web Interface**: User-friendly web UI for text analysis
- **Error Handling**: Comprehensive error handling for invalid inputs
- **Unit Tests**: Complete test coverage
- **Code Quality**: Static code analysis with Pylint

## Project Structure

```
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py          # Package initialization
│   └── emotion_detection.py # Core emotion detection module
├── server.py               # Flask web server
├── test_emotion_detection.py # Unit tests
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, configure your IBM Watson credentials:

1. Sign up for IBM Watson NLP service
2. Get your API key and instance URL
3. Update `EmotionDetection/emotion_detection.py` with your credentials:
   - Replace `YOUR_API_KEY` with your actual API key
   - Replace `YOUR_INSTANCE_ID` with your instance ID

## Usage

### Running the Web Server

```bash
python server.py
```

The server will start on `http://127.0.0.1:5000`

### Web Interface

- **UI Endpoint**: `http://127.0.0.1:5000/emotionDetectorUI?text=your_text_here`
- Example: `http://127.0.0.1:5000/emotionDetectorUI?text=I%20love%20this%20so%20much`

### REST API

- **Endpoint**: `POST /emotionDetector`
- **Request Body**:
```json
{
  "text": "Your text to analyze"
}
```

- **Response**:
```json
{
  "anger": 0.0,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 0.95,
  "sadness": 0.0,
  "dominant_emotion": "joy"
}
```

## Running Tests

Execute unit tests:

```bash
python -m pytest test_emotion_detection.py -v
```

Or using unittest:

```bash
python -m unittest test_emotion_detection -v
```

## Static Code Analysis

Run Pylint for code quality checks:

```bash
pylint EmotionDetection/ server.py
```

For a specific score:

```bash
pylint EmotionDetection/ server.py --score=yes
```

## Error Handling

The application handles the following error scenarios:

- **Empty/Null Input**: Returns status code 400 with error message
- **Invalid Requests**: Returns appropriate HTTP status codes
- **API Failures**: Graceful fallback with error details

## API Response Codes

- `200`: Successful emotion detection
- `400`: Invalid text input (empty/null)
- `500`: Server error or API failure

## Requirements

- Python 3.7+
- Flask 2.3.3+
- IBM Watson SDK 7.0.0+
- requests 2.31.0+
- pylint 2.17.5+
- pytest 7.4.0+

## Author

[Your Name]

## License

MIT License

## Acknowledgments

- IBM Watson Team for the NLP library
- Flask framework for web application development
