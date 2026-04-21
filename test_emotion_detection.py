import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    Tests various text inputs to ensure correct emotion detection and output format.
    """
    
    def test_emotion_detector_joy(self):
        """Test that joyful text returns joy as dominant emotion"""
        result = emotion_detector("I love this so much!")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertGreaterEqual(result['joy'], 0)
        self.assertIsNotNone(result['status_code'])
    
    def test_emotion_detector_anger(self):
        """Test that angry text returns anger as dominant emotion"""
        result = emotion_detector("I am so angry and frustrated!")
        self.assertEqual(result['dominant_emotion'], 'anger')
        self.assertGreaterEqual(result['anger'], 0)
        self.assertEqual(result['status_code'], 200)
    
    def test_emotion_detector_sadness(self):
        """Test that sad text returns sadness as dominant emotion"""
        result = emotion_detector("I am very sad and unhappy")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertGreaterEqual(result['sadness'], 0)
        self.assertEqual(result['status_code'], 200)
    
    def test_emotion_detector_fear(self):
        """Test that fearful text returns fear as dominant emotion"""
        result = emotion_detector("I am afraid and nervous")
        self.assertEqual(result['dominant_emotion'], 'fear')
        self.assertGreaterEqual(result['fear'], 0)
        self.assertEqual(result['status_code'], 200)
    
    def test_emotion_detector_disgust(self):
        """Test that disgusting text returns disgust as dominant emotion"""
        result = emotion_detector("This is disgusting and repulsive")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        self.assertGreaterEqual(result['disgust'], 0)
        self.assertEqual(result['status_code'], 200)
    
    def test_emotion_detector_empty_string(self):
        """Test that empty string returns status code 400"""
        result = emotion_detector("")
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['dominant_emotion'])
    
    def test_emotion_detector_none_input(self):
        """Test that None input returns status code 400"""
        result = emotion_detector(None)
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['dominant_emotion'])
    
    def test_emotion_detector_whitespace(self):
        """Test that whitespace-only string returns status code 400"""
        result = emotion_detector("   \n\t   ")
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['dominant_emotion'])
    
    def test_emotion_detector_output_format(self):
        """Test that output has the correct format"""
        result = emotion_detector("This is a test")
        
        # Check all required keys exist
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion', 'status_code']
        for key in required_keys:
            self.assertIn(key, result)
    
    def test_emotion_detector_score_valid(self):
        """Test that emotion scores are valid numbers between 0 and 1"""
        result = emotion_detector("I am very happy!")
        
        if result['status_code'] == 200:
            for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
                self.assertIsInstance(result[emotion], (int, float))
                self.assertGreaterEqual(result[emotion], 0)
                self.assertLessEqual(result[emotion], 1)


if __name__ == '__main__':
    unittest.main()
