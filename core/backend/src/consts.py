import os


RESOURCES_LOCATION = os.path.join(os.path.dirname(__file__), 'resources')
PROMPTS_LOCATION = os.path.join(RESOURCES_LOCATION, "prompts")
UPLOADED_PDFS_DIRECTORY = os.path.join(RESOURCES_LOCATION, "uploaded_pdfs")
TEST_PDF_SHORT_LOCATION = os.path.join(RESOURCES_LOCATION, "WW2_short.pdf")
TEST_PDF_LOCATION = os.path.join(RESOURCES_LOCATION, "WW2.pdf")
GENERATE_QUESTION_PROMPT = os.path.join(PROMPTS_LOCATION, "generate_questions.txt")
QUIZ_EXAMPLE_LOCATION = os.path.join(PROMPTS_LOCATION, "quiz_json_example.txt")
GENERATED_QUIZ_LOCATION = os.path.join(RESOURCES_LOCATION, "quiz.json")

SPLIT_INTO_PARAGRAPHS_PROMPT = "Your role is to split the input text every two sentences in a JSON list (do not specify any keys). " \
                                "A sentence is defined as a sequence of words that convey a concept, interrupted by a point. make sure to" \
"The two sentences will be concatenated into a single one. pay particular attention in returning a syntactically correct JSON list." \
"example: if the input is 'hello everyone, i love radiohead. they are the best. what is your favorite band? Don't say Oasis please.' "\
    "the output should be ['hello everyone, i love radiohead. they are the best.', 'what is your favorite band? Don't say Oasis please.']"

PARAGRAPHS_PER_PAGE = 8
