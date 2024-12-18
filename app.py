from QA.qa_app import app_qa
from Translation.translation_app import app_translation
from Summarization.summary_app import app_summary
from flask import Flask, render_template, request, redirect, url_for, flash
from Database.user import MyDB
from forms import UserFeedbackForm

# Connect the database
db = MyDB()

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

app.register_blueprint(app_summary, url_prefix="/summarize")
app.register_blueprint(app_qa, url_prefix="/question_answering")
app.register_blueprint(app_translation, url_prefix="/translate")


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/services", methods=["GET", "POST"])
def services():

    if request.method == "POST":
        selected_option = request.form.get("option")
        if selected_option == "qa_system":
            return redirect(url_for("app_qa.index"))  # Redirect to QA System
        elif selected_option == "summarization":
            return redirect(url_for("app_summary.index"))  # Redirect to Summarization
        elif selected_option == "image_captioning":
            return redirect(url_for("app_caption.index"))
        elif selected_option == "translation":
            return redirect(url_for("app_translation.index"))

    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    form = UserFeedbackForm()

    if form.validate_on_submit():
        try:
            name = form.name.data
            qa_feedback = form.qa_feedback.data
            qa_rating = form.qa_rating.data
            summarization_feedback = form.summarization_feedback.data
            summarization_rating = form.summarization_rating.data
            translation_feedback = form.translation_feedback.data
            translation_rating = form.translation_rating.data
            additional_comments = form.additional_comments.data

            # Debug print statements
            # print("Feedback data:")
            # print(name, qa_feedback, qa_rating, summarization_feedback, summarization_rating,
            #       translation_feedback, translation_rating, additional_comments)

            db.insert_feedback(name, qa_feedback, qa_rating, summarization_feedback, summarization_rating,
                               translation_feedback, translation_rating, additional_comments)

            flash("Thank you for your feedback!", "success")
            return redirect(url_for("home"))

        except Exception as e:
            print(f"Database error: {e}")
            flash("An error occurred while saving feedback.", "error")

    else:
        print("Form validation failed:", form.errors)

    return render_template('feedback.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)