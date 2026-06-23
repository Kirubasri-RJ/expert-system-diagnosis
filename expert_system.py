RULES = [
    {
        "symptoms": {"wont_start", "clicking_sound", "lights_dim"},
        "diagnosis": "Weak or dead battery",
        "explanation": "The engine won't start, you hear clicking, and the lights are dim. This points to insufficient power reaching the starter, the classic sign of a weak or dead battery.",
    },
    {
        "symptoms": {"engine_overheating", "coolant_low"},
        "diagnosis": "Coolant leak or failing radiator",
        "explanation": "The engine is overheating and coolant levels are low. This usually means coolant is leaking somewhere in the system, reducing the engine's ability to cool itself.",
    },
    {
        "symptoms": {"strange_noise", "squealing_sound"},
        "diagnosis": "Worn brake pads or loose belt",
        "explanation": "A squealing noise usually comes from worn brake pads or a loose/worn serpentine belt.",
    },
    {
        "symptoms": {"check_engine_light", "poor_fuel_economy"},
        "diagnosis": "Faulty oxygen sensor or dirty fuel injectors",
        "explanation": "A lit check engine light along with poor fuel economy commonly traces back to a faulty oxygen sensor or dirty fuel injectors.",
    },
]

DEFAULT_DIAGNOSIS = {
    "diagnosis": "Unable to determine a specific issue",
    "explanation": "The reported symptoms don't match any rule in the knowledge base. Consider consulting a certified mechanic.",
}

SYMPTOM_QUESTIONS = {
    "wont_start": "Does the car fail to start? (y/n): ",
    "clicking_sound": "Do you hear a clicking sound when trying to start? (y/n): ",
    "lights_dim": "Are the dashboard/headlights dimmer than usual? (y/n): ",
    "engine_overheating": "Is the engine overheating? (y/n): ",
    "coolant_low": "Is the coolant level low? (y/n): ",
    "strange_noise": "Is the car making a strange noise? (y/n): ",
}


def ask_yes_no(question):
    while True:
        try:
            answer = input(question).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Assuming 'no' for this symptom.")
            return False

        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please answer with 'y' or 'n'.")


def gather_symptoms():
    reported_symptoms = set()
    print("\nPlease answer the following questions about your car's symptoms.\n")

    for symptom_key, question_text in SYMPTOM_QUESTIONS.items():
        if ask_yes_no(question_text):
            reported_symptoms.add(symptom_key)

    return reported_symptoms


def diagnose(reported_symptoms):
    if not reported_symptoms:
        return {
            "diagnosis": "No symptoms reported",
            "explanation": "You didn't report any symptoms, so no diagnosis can be made.",
        }

    best_match = None
    best_match_count = 0

    for rule in RULES:
        if rule["symptoms"].issubset(reported_symptoms):
            match_count = len(rule["symptoms"])
            if match_count > best_match_count:
                best_match = rule
                best_match_count = match_count

    if best_match:
        return best_match
    return DEFAULT_DIAGNOSIS


def main():
    print("=" * 60)
    print(" CAR TROUBLESHOOTING EXPERT SYSTEM")
    print("=" * 60)

    while True:
        symptoms = gather_symptoms()
        result = diagnose(symptoms)

        print("\n" + "-" * 60)
        print("DIAGNOSIS:", result["diagnosis"])
        print("-" * 60)
        print("REASONING:", result["explanation"])
        print("-" * 60)

        again = ask_yes_no("\nWould you like to run another diagnosis? (y/n): ")
        if not again:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()