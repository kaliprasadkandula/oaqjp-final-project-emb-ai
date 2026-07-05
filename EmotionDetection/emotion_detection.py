import requests
import json

def emotion_detector(text_to_analyze:str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotion_scores = {}
    
    for emotion in ['anger','disgust','fear','joy','sadness']:
        emotion_scores[f"{emotion}"] = emotions[f"{emotion}"]
    dominant_emotion = max(emotion_scores,key=emotion_scores.get)
    # print(f"dominant_emotion",dominant_emotion)
    emotion_scores["dominant_emotion"] = dominant_emotion
    return emotion_scores


