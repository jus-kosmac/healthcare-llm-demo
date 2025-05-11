# HealthCare LLM Demo

This demo processes an example medical transcript and extracts patient information into a predefined structured JSON output.
It also produces an example of a custom formatted report.
- Input: `examples/medical_transcript.txt`
- Output: `examples/example_output.txt`

## Instructions for running locally
- Create `.env` file with `OPENAI_API_KEY=...`. You need to have an OpenAI account with non-zero balance.
- Build Docker image.
```
docker build -t healthcare-llm-demo:local-dev .
```
- Run demo example.
```
docker-compose up
```

## Resources
- [OpenAI docs - models](https://platform.openai.com/docs/models)
- [OpenAI docs - structured outputs](https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses)