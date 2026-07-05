# Emotion Detection with Watson NLP

A Flask web application that analyzes a piece of text and detects the emotions
expressed in it — **anger, disgust, fear, joy, and sadness** — using IBM
Watson NLP's `EmotionPredict` service. It also reports the **dominant emotion**
in the text.

This is the final project for the *Developing AI Applications with Python and
Flask* course.

## Features

- Detects five emotions and their confidence scores for any input text.
- Identifies the dominant emotion.
- Simple web interface to enter text and view results.
- Error handling for blank/invalid input (returns *"Invalid text! Please try again!"*).
- Unit-tested emotion detection package.
- Passes PyLint static code analysis with a 10/10 score.

## Project Structure

- `EmotionDetection/` — the emotion detection package
  - `__init__.py` — exposes the `emotion_detector` function
  - `emotion_detection.py` — calls the Watson NLP API and formats the result
- `server.py` — Flask web server that deploys the application
- `templates/index.html` — the web page (input form + results area)
- `static/mywebscript.js` — frontend script that calls the server
- `tests/test_emotion_detection.py` — unit tests for the package

## How to Run

From the project root, start the Flask server:

```bash
python3 server.py
```

Then open the application in your browser at:

```
http://localhost:5000
```

Enter a statement in the text box and click **Run Sentiment Analysis** to see
the detected emotions and the dominant emotion.

## Running the Tests

```bash
python3 -m unittest tests/test_emotion_detection.py
```

## Static Code Analysis

```bash
pylint server.py
```

## License

The content of this project is licensed under Apache 2.0.
