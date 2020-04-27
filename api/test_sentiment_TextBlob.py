import sentiment_TextBlob as s

######################################################################################################################
# Tests for Text_Sentiment
######################################################################################################################	

def test_get_sentiment_polarity_case_1():
    text = "I am very happy and I love everything!"

    actual_sentiment = s.Text_Sentiment().get_sentiment_polarity(text)

    assert (actual_sentiment > 0)

def test_get_sentiment_polarity_case_2():
    text = "I am very sad and depressed with everything going on."

    actual_sentiment = s.Text_Sentiment().get_sentiment_polarity(text)

    assert (actual_sentiment < 0)

def test_get_sentiment_polarity_case_3():
    text = "Good job, but I expect more in the future"

    actual_sentiment = s.Text_Sentiment().get_sentiment_polarity(text)

    assert (actual_sentiment <= 0.4) and (actual_sentiment >= -0.4)