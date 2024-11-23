from crewai.tools import BaseTool
from my_retail_advisor.tools.tool_helper import Helper

class VisionTool(BaseTool):
    name: str = "Vision Tool"
    description: str = "Analyzes a default picture to collect visual data and caption."

    def _run(self) -> str:
        # Absolute path to the shelve.png image
        image_path = '/Users/yohanbensoussan/Projects/crewai/my_retail_advisor/shelve.jpg'

        # Simulating image-to-text conversion
        products_in_image = Helper.image2text(image_path)
        return products_in_image
