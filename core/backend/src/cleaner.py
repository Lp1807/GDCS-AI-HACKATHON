import gptconnector
from tqdm import tqdm

class Cleaner:
    @staticmethod
    def clean(text: list[str]) -> str:
        gpt = gptconnector.GPTConnector()
        for i in tqdm(range(len(text))):
            text[i] = gpt.clean(text[i]).content
            
        return ''.join(text)