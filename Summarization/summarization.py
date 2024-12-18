from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "facebook/bart-large-cnn"  # Replace with your model name
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def summarize_text(text):
    """Summarize the text using the loaded model."""
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=270, min_length=160, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary