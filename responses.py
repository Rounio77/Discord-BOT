import random


def get_response(user_input):
    lower_case = user_input.lower()

    if lower_case == '':
        return 'This is an empty string'
    if "Hello" in lower_case:
        return random.choice(["Hi", "Hello there", "How may i help you?"])
    elif 'how are you' in lower_case:
        return 'Good, thanks!'
    elif 'bye' in lower_case:
        return random.choice(["See you later", "Good bye", "see ya"])
    elif 'roll dice' in lower_case:
        return f'You rolled: {random.randint(1, 6)}'
    else:
        return random.choice(
            [
                "I do not understand your input....",
                "You can try asking Google for that...",
                "What are yu talking about?",
                "Do you mind rephrasing that..."
            ]
        )



