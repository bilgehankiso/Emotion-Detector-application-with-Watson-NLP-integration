"""Emotion Detection Module - Analyzes text to detect emotions"""


# Emotion keyword mappings
EMOTION_KEYWORDS = {
    'joy': ['love', 'happy', 'joy', 'excellent', 'great',
            'wonderful', 'beautiful', 'fantastic', 'amazing', 'good'],
    'anger': ['angry', 'anger', 'furious', 'mad', 'hate',
              'upset', 'frustrated', 'annoyed', 'irritated'],
    'sadness': ['sad', 'sadness', 'unhappy', 'depressed',
                'miserable', 'disappointed', 'upset', 'grief', 'mourning'],
    'fear': ['afraid', 'fear', 'scared', 'anxious',
             'nervous', 'terrified', 'worry', 'concerned'],
    'disgust': ['disgusting', 'disgust', 'repulsive',
                'gross', 'repugnant', 'abhorrent', 'horrible']
}


def _classify_emotion(text):
    """
    Mock emotion classification based on keywords.
    In production, this would use Watson NLP API.
    """
    text_lower = text.lower()
    emotions = {emotion: 0.0 for emotion in EMOTION_KEYWORDS}

    # Score emotions based on keywords
    for emotion, keywords in EMOTION_KEYWORDS.items():
        emotion_score = sum(0.3 for word in keywords if word in text_lower)
        emotions[emotion] = emotion_score

    # Normalize scores to 0-1 range
    max_score = max(emotions.values())
    if max_score > 1:
        emotions = {e: score / max_score for e, score in emotions.items()}

    # If no emotion detected, default to neutral
    if max(emotions.values()) == 0:
        emotions['joy'] = 0.5

    return emotions


def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using IBM Watson NLP API.
    Uses mock implementation for development and testing.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion,
              or a dictionary with 'status_code' key if error occurs
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

    # Get emotion scores using mock classifier
    emotions = _classify_emotion(text_to_analyze)

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion,
        'status_code': 200
    }
