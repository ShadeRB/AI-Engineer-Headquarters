from transformers import pipeline
import yaml

class Generator:
    def __init__(self, config):
        model_name = config['generation']['model']
        self.llm = pipeline(
            'text-generation',
            model=model_name,
            device=-1,  # -1 = CPU; change to 0 if using GPU
        )

    def generate_answer(self, query, contexts):
        prompt = f"Question: {query}\nContext: {' '.join(contexts)}\nAnswer:"

        response = self.llm(
            prompt,
            do_sample=True,
            top_p=0.9,
            temperature=0.7,
            max_length=300,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3
        )[0]['generated_text']

        # Clean up answer
        if "Answer:" in response:
            return response.split("Answer:")[1].strip()
        return response.strip()

if __name__ == "__main__":
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    generator = Generator(config)
    answer = generator.generate_answer(
        "How to reset my account password?",
        ["To reset your password, go to the login page and click 'Forgot Password'. You will receive a reset link via email."]
    )
    print(answer)
