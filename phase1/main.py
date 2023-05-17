from flask import Flask, render_template, request, jsonify
from mbti import get_mbti_type

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/result", methods=["POST"])
def result():
    # Get answers from form
    answer1 = int(request.form["answer1"])
    answer2 = int(request.form["answer2"])
    answer3 = int(request.form["answer3"])
    answer4 = int(request.form["answer4"])
    answer5 = int(request.form["answer5"])
    answer6 = int(request.form["answer6"])
    answer7 = int(request.form["answer7"])
    answer8 = int(request.form["answer8"])
    answer9 = int(request.form["answer9"])
    answer10 = int(request.form["answer10"])

    # Calculate MBTI type
    a,b,c,d = get_mbti_type(answer1, answer2, answer3, answer4, answer5,
                              answer6, answer7, answer8, answer9, answer10)

    # Render the result template with the MBTI type
    return render_template("result.html", a=a,b=b,c=c,d=d)

# if __name__ == "__main__":
#     app.run(debug=True)


app.run(host='0.0.0.0', port=81)
