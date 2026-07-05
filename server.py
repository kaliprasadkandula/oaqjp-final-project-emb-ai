from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector",methods=["GET"])
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")
    # print(f"text_to_analyze {text_to_analyze}")
    response =  emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    anger   = response['anger']
    disgust = response['disgust']
    fear    = response['fear']
    joy     = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']



    return (
    f"For the given statement, the system response is "
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    f"'joy': {joy} and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant}."      
    )





@app.route("/",methods=["GET"])
def render_index_page():    
    return render_template("index.html")


if __name__=="__main__":
    app.run("0.0.0.0",5000,debug=True)

