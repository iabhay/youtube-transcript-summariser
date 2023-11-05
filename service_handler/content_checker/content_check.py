from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions
import keys


class ContentChecker:
    def __init__(self):
        self.endpoint = keys.CONTENT_CHECK_ENDPOINT
        self.key = AzureKeyCredential(keys.CONTENT_CHECK_KEY)

    def analyze_text(self, text):
        text = text[:10000]
        client = ContentSafetyClient(self.endpoint, self.key)
        request = AnalyzeTextOptions(text=text)
        try:
            response = client.analyze_text(request)
        except HttpResponseError as e:
            print("Analyze text failed.")
            raise
        if response.hate_result:
            res = {
                    "Hate": response.hate_result.severity,
                    "SelfHarm": response.self_harm_result.severity,
                    "Adult": response.sexual_result.severity,
                    "Violence": response.violence_result.severity
                   }
            return res
        return False
