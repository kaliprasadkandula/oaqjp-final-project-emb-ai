from flask import Flask,request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector",methods=["GET"])
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")
    print(f"text_to_analyze {text_to_analyze}")
    return emotion_detector(text_to_analyze)


if __name__=="__main__":
    app.run("0.0.0.0",5000,debug=True)

