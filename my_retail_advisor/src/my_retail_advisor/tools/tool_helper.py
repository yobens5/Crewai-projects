import requests
import base64
from my_retail_advisor.auth import Auth

class Helper:    
    @staticmethod
    def image2text(image_path_or_url: str) -> str:
        """This tool is useful when we want to generate textual descriptions from images."""
        
        with open(image_path_or_url, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        print(f"Processing image from file: {image_path_or_url}")

        try:
            access_token = Auth.get_ibm_token()
        except Exception as e:
            print("Error:", e)
        
        url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29"

        prompt = (
            "Caption the picture with details including names and descriptions of products." 
        )
        
        body = {
        "messages": [{"role":"user","content":[{"type":"text","text":prompt},{"type":"image_url","image_url":{"url": f"data:image/jpeg;base64,{encoded_image}"}}]}],
        "project_id": "b20349a9-3dd5-47fd-b4ef-1b10e1f3b591",
        "model_id": "meta-llama/llama-3-2-90b-vision-instruct",
        "decoding_method": "greedy",
        "max_tokens": 1000
        }
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        }

        response = requests.post(
            url,
            headers=headers,
            json=body
        )
        
        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))
        data = response.json()
        output = data['choices'][0]['message']['content']
        print(output)
        return "".join(output)