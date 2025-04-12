from flask import Flask,request,jsonify,render_template
from EmotionDetection import emotion_detector

app=Flask(__name__  )
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')  # use the correct key name!
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    result=emotion_detector(text_to_analyze)
    if not result :
        return "error",500
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted_result     
if __name__ == "__main__":
    print("Starting Flask app...")  # Debug print
    app.run(debug=True)