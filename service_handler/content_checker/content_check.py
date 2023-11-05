from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions


class ContentChecker:
    def __init__(self):
        self.endpoint = "https://youtube-transcript-summariser.cognitiveservices.azure.com/"
        self.key = AzureKeyCredential("bb13cc827cbf4b35867f8dd43630aeba")
        # tobj = transcriptor()
        # self.text = tobj.format_transcript()

    def analyze_text(self, text):
        text = text[:10000]
        client = ContentSafetyClient(self.endpoint, self.key)
        request = AnalyzeTextOptions(text=text)
        try:
            response = client.analyze_text(request)
        except HttpResponseError as e:
            print("Analyze text failed.")
            # if e.error:
            #     print(f"Error code: {e.error.code}")
            #     print(f"Error message: {e.error.message}")
            #     raise
            # print(e)
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
