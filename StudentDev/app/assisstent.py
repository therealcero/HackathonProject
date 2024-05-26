from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def chatbot(user_input):
    # Tokenize the input
    inputs = tokenizer.encode(user_input + "</s>", return_tensors="pt")
    # Generate a response
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage
def ask(user_input):
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        return
    else:
        response = chatbot(user_input)
        return response
if __name__ == '__main__':
    ask(input())
