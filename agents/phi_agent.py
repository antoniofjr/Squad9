import onnxruntime_genai as og

from datetime import datetime
import os

MODEL_PATH = "models/phi3.5-mini-instruct-onnx"

model = og.Model(MODEL_PATH)

tokenizer = og.Tokenizer(model)


def ask_phi(prompt):

    # =========================
    # prompt -> tokens
    # =========================
    tokens = tokenizer.encode(prompt)

    # =========================
    # parâmetros
    # =========================
    params = og.GeneratorParams(model)

    params.set_search_options(
        max_length=512,
        temperature=0.7
    )

    # obrigatório na sua versão
    params.input_ids = tokens

    # =========================
    # generator
    # =========================
    generator = og.Generator(model, params)

    # =========================
    # resposta
    # =========================
    output = ""

    while not generator.is_done():

        generator.compute_logits()

        generator.generate_next_token()

        token = generator.get_next_tokens()[0]

        output += tokenizer.decode([token])

    # =========================
    # criar pasta reports
    # =========================
    os.makedirs("reports", exist_ok=True)

    # =========================
    # nome do relatório
    # =========================
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"reports/chat_{timestamp}.txt"

    # =========================
    # salvar relatório
    # =========================
    with open(file_name, "w", encoding="utf-8") as f:

        f.write("===== PROMPT =====\n\n")

        f.write(prompt)

        f.write("\n\n===== RESPOSTA =====\n\n")

        f.write(output)

    print(f"\nRelatório salvo em: {file_name}")

    return output