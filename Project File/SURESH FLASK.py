from flask import Flask, render_template



Olympic = Flask(__name__)


@Olympic.route('/', methods=["GET", "POST"] )
def home():
    return render_template('index.html')

@Olympic.route('/dashboard', methods=["GET", "POST"]) 
def dashboard():
    return render_template('dashboard.html')

@Olympic.route('/report', methods=["GET", "POST"])
def report():
    return render_template('report.html')

@Olympic.route('/story', methods=["GET", "POST"])
def story():
    return render_template('story.html')


# run server
if __name__ == "__main__":
    Olympic.run(debug=True)