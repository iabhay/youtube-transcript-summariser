import os
import azure.ai.textanalytics
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError


class Summariser:
    def __init__(self):
    # This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
        self.key = "d0b5987028ba43089d906708e099da84"
        self.endpoint = "https://youtube-summariser.cognitiveservices.azure.com/"
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential

    # Authenticate the client using your key and endpoint
    def authenticate_client(self):
        ta_credential = AzureKeyCredential(self.key)
        text_analytics_client = azure.ai.textanalytics.TextAnalyticsClient(
            endpoint=self.endpoint,
            credential=ta_credential)
        return text_analytics_client

    # Example method for summarizing text
    def sample_extractive_summarization(self, document):
        client = self.authenticate_client()
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.textanalytics import (
            TextAnalyticsClient,
            ExtractiveSummaryAction
        )
        poller = client.begin_analyze_actions(
            document,
            actions=[
                ExtractiveSummaryAction(max_sentence_count=20)
            ],
        )
        document_results = poller.result()
        for result in document_results:
            extract_summary_result = result[0]  # first document, first result
            if extract_summary_result.is_error:
                print("...Is an error with code '{}' and message '{}'".format(
                    extract_summary_result.code, extract_summary_result.message
                ))
            else:
                txt = "Summary extracted: \n{}".format(" ".join([sentence.text for sentence in extract_summary_result.sentences]))
                return txt
