import onnxruntime_genai as og

MODEL_PATH = "models/phi3.5-mini-instruct-onnx"

model = og.Model(MODEL_PATH)
tokenizer = og.Tokenizer(model)

def ask_phi(prompt):

    tokens = tokenizer.encode(prompt)

    params = og.GeneratorParams(model)
    params.set_search_options(
        max_length=512,
        temperature=0.7
    )

    params.input_ids = tokens

    generator = og.Generator(model, params)

    output = ""

    while not generator.is_done():
        generator.compute_logits()
        generator.generate_next_token()

        token = generator.get_next_tokens()[0]
        output += tokenizer.decode([token])

    return output