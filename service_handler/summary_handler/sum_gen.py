import oneai
import keys
import logging
from config.log_config.log_config import LogStatements
logger = logging.getLogger('summary_generator')


class SummaryGenerator:
    def __init__(self):
        # set a One AI API key, following API calls will use this key
        oneai.api_key = keys.oneai_api_key

    def summary_generator(self, your_input):
        size = len(your_input)
        # define a pipeline for processing str inputs
        try:
            pipeline = oneai.Pipeline(steps=[oneai.skills.Summarize(min_length=size/4, max_length=size/3),])
            # process the input and store the output
            output = pipeline.run(your_input)
            # print the summary
            return output.summary.text
        except Exception:
            print("Summary Generation Failed. Try Again!")
            return None
