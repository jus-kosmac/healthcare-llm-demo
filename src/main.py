import json

from src.llm_processor import LlmProcessor

INPUT_FILE = "../examples/medical_transcript.txt"
OUTPUT_FILE = "../examples/example_output.txt"


def run_example() -> None:
    with open(file=INPUT_FILE, mode="r") as file:
        transcript = file.read()

    llm_processor = LlmProcessor()
    patient_case, report = llm_processor.process_transcript(transcript)

    output_txt = f"""
REPORT:
{report.strip()}

#########################################

STRUCTURED OUTPUT:
{json.dumps(patient_case.model_dump(), indent=2)}
""".strip()

    with open(file=OUTPUT_FILE, mode="w") as file:
        file.write(output_txt)

    print(f"Success! Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_example()
