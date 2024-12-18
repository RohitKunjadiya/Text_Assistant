from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    IntegerField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Optional,
    Length,
    NumberRange
)


class UserFeedbackForm(FlaskForm):
    # Name Field
    name = StringField(
        "Your Name",
        validators=[Optional(), Length(max=50)],
        description="Enter your name (optional)"
    )

    # QA Feedback
    qa_feedback = TextAreaField(
        "QA Feature Feedback",
        validators=[Optional(), Length(max=1000)],
        description="Provide your feedback on the QA feature (optional)"
    )
    qa_rating = IntegerField(
        "QA Feature Rating (1-5)",
        validators=[Optional(), NumberRange(min=1, max=5)],
        description="Rate the QA feature from 1 (Poor) to 5 (Excellent)"
    )

    # Text Summarization Feedback
    summarization_feedback = TextAreaField(
        "Text Summarization Feature Feedback",
        validators=[Optional(), Length(max=1000)],
        description="Provide your feedback on the Text Summarization feature (optional)"
    )
    summarization_rating = IntegerField(
        "Text Summarization Rating (1-5)",
        validators=[Optional(), NumberRange(min=1, max=5)],
        description="Rate the Text Summarization feature from 1 (Poor) to 5 (Excellent)"
    )

    # Translation Feedback
    translation_feedback = TextAreaField(
        "Translation Feature Feedback",
        validators=[Optional(), Length(max=1000)],
        description="Provide your feedback on the Translation feature (optional)"
    )
    translation_rating = IntegerField(
        "Translation Rating (1-5)",
        validators=[Optional(), NumberRange(min=1, max=5)],
        description="Rate the Translation feature from 1 (Poor) to 5 (Excellent)"
    )

    # Additional Comments Section
    additional_comments = TextAreaField(
        "Additional Comments",
        validators=[Optional(), Length(max=1000)],
        description="Any other feedback or suggestions for improvement?"
    )

    # Submit Button
    submit = SubmitField("Submit Feedback")
