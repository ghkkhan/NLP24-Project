
def is_title_in_review(review_text, title):
    review_text_downcase = review_text.lower()
    title_downcase = title.lower()
    return (title_downcase in review_text_downcase) 