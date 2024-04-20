import os


RESOURCES_LOCATION = os.path.join(os.path.dirname(__file__), 'resources')
TEST_PDF_LOCATION = os.path.join(RESOURCES_LOCATION, "WW2_short.pdf")
SPLIT_INTO_PARAGRAPHS_PROMPT = "Your role is to split the input text every two sentences in a JSON list (do not specify any keys)." \
"The two sentences will be concatenated into a single one. pay particular attention in returning a syntactically correct JSON list." \
"example: if the input is 'hello everyone, i love radiohead. they are the best. what is your favorite band? Don't say Oasis please.' "\
    "the output should be ['hello everyone, i love radiohead. they are the best.', 'what is your favorite band? Don't say Oasis please.']"