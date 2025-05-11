from typing import Optional

from pydantic import BaseModel
from openai import OpenAI


class PatientCase(BaseModel):
    patient_name: Optional[str] = None
    age: Optional[int] = None
    diagnoses: Optional[list[str]] = None
    past_treatments: Optional[list[str]] = None
    current_discussion: Optional[str] = None
    recommendations: Optional[list[str]] = None
    prescriptions: Optional[list[str]] = None


_MODEL = "gpt-4.1"


class LlmProcessor:
    def __init__(self) -> None:
        self.client = OpenAI()

    @staticmethod
    def _create_prompt(transcript: str) -> str:
        return f"""
You are given a transcript of a medical consultation.
Extract the relevant patient information into a structured output.

Here is the transcript:
{transcript.strip()}
""".strip()

    @staticmethod
    def _create_report(patient_case: PatientCase) -> str:
        def format_items(items: Optional[list[str]]) -> Optional[str]:
            if items is None:
                return None
            return "\n".join(f"- {item.strip()}" for item in items)

        return f"""
Patient name: {patient_case.patient_name}
Age: {patient_case.age}
-------------------------------------
Diagnoses:
{format_items(patient_case.diagnoses)}
-------------------------------------
Past treatments:
{format_items(patient_case.past_treatments)}
-------------------------------------
Current discussion:
{patient_case.current_discussion}
-------------------------------------
Recommendations:
{format_items(patient_case.recommendations)}
-------------------------------------
Prescriptions:
{format_items(patient_case.prescriptions)}
""".strip()

    def process_transcript(self, transcript: str) -> tuple[PatientCase, str]:
        prompt = self._create_prompt(transcript)
        
        try:
            response = self.client.responses.parse(
                model=_MODEL,
                input=[{"role": "user", "content": prompt}],
                text_format=PatientCase
            )
            patient_case = response.output_parsed
        except Exception as e:
            raise Exception(f"LLM error: {e}")

        report = self._create_report(patient_case)
        return patient_case, report
