import onnxruntime_genai as og
from pathlib import Path

MODEL_PATH = "models/phi3.5-onnx"

# carregar modelo
model = og.Model(MODEL_PATH)
tokenizer = og.Tokenizer(model)

def ask_phi(prompt: str):

    full_prompt = f"""
    Você é um especialista em Power Platform.

    {prompt}
    """

    tokens = tokenizer.encode(full_prompt)

    params = og.GeneratorParams(model)
    params.set_search_options(
        max_length=500,
        temperature=0.7
    )

    generator = og.Generator(model, params)
    generator.append_tokens(tokens)

    output = ""

    while not generator.is_done():
        generator.generate_next_token()

        new_token = generator.get_next_tokens()[0]
        output += tokenizer.decode([new_token])

    return output