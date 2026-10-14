from typing import cast

from geniex import AutoModelForCausalLM
from geniex.generation.streamer import TextIteratorStreamer


def main():
    model = AutoModelForCausalLM.from_pretrained(
        #"Qwen/Qwen3-0.6B-GGUF",
        # device_map="auto",
        # "ai-hub-models/Qwen3-8B",
        "ai-hub-models/Gemma-4-E4B-it",
        device_map="qairt",
    )

    messages = []
    while True:
        question = input("Ask a question (or /q): ")
        if question.lower() == "/q":
            break
        messages.append({'role': 'user', 'content': question})
        prompt = model.tokenizer.apply_chat_template(
            messages=messages, add_generation_prompt=True,
        )

        streamer = cast(
            TextIteratorStreamer,
            model.generate(prompt, max_new_tokens=9046, stream=True),
        )
        for chunk in streamer:
            print(chunk, end="", flush=True)
        print()

        messages.append({'role': 'assistant', 'content': streamer.output.text})

    model.close()


if __name__ == "__main__":
    main()
