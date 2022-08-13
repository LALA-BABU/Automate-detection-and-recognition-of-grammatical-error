
from happytransformer import HappyTextToText
from happytransformer import TTSettings
happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
text = "gec: " + "helo"
settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
result = happy_tt.generate_text(text, args=settings)
print(result.text)

from textblob import TextBlob
misspelled_word=result.text
corrected_word= TextBlob(misspelled_word).correct()
print("Incorrect Word: ",misspelled_word)
print("Corrected Word :",corrected_word)

