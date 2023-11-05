import oneai
import keys
# from dotenv import load_dotenv
# load_dotenv()
# set a One AI API key, following API calls will use this key
oneai.api_key = keys.oneai_api_key
# insert your input text here
class SummaryGenerator:
    def __init__(self):
        pass
    def summary_generator(self, your_input):
        size = len(your_input)
        # define a pipeline for processing str inputs
        pipeline = oneai.Pipeline(steps=[oneai.skills.Summarize(min_length=size/4, max_length=size/3),])
        # process the input and store the output
        output = pipeline.run(your_input)
        # print the summary
        return output.summary.text
