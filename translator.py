from transformers import MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text: str) -> str:
        if not text.strip():
            return ""

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        translated = self.model.generate(**inputs)
        output = self.tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )

        return output