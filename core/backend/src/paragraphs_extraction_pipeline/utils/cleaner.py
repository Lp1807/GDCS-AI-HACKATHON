from tqdm import tqdm

from core.backend.src.gptconnector import GPTConnector


class Cleaner:
    @staticmethod
    def clean(text: list[str]) -> str:
        gpt = GPTConnector()
        for i in tqdm(range(len(text))):
            text[i] = gpt.clean(text[i]).content
            
        return ''.join(text)
