"""Emotion Detection Module - Analyzes text to detect emotions using Watson NLP API"""
import json
import requests


def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using IBM Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """

    # Check for empty or None input
    if text_to_analyze is None or len(text_to_analyze.strip()) == 0:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Return None for all emotions if status code is 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }

    # Parse successful response
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

    return {
        'anger': emotion_predictions['anger'],
        'disgust': emotion_predictions['disgust'],
        'fear': emotion_predictions['fear'],
        'joy': emotion_predictions['joy'],
        'sadness': emotion_predictions['sadness'],
        'dominant_emotion': dominant_emotion,
        'status_code': response.status_code
    }
