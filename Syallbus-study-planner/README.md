# Syllabus Study Planner

A study planner that reads your syllabus PDF, combines it with your exam date, and uses the Gemini API to generate a structured, day-by-day study plan.

## Features

- [1] Extracts syllabus text from a PDF using `pymupdf`
- [2] Takes the exam date as input and calculates days remaining
- [3] Builds a custom prompt combining the syllabus content and days left
- [4] Sends the prompt to Gemini and prints a structured, day-by-day study plan
- [5] Validates PDFs and gracefully handles empty/image-only files
- [6] Handles bad file paths and API failures without crashing

## Setup

1. Clone the repo
2. Install dependencies: `pip install pymupdf google-genai`
3. Get your own API key from Google AI Studio
4. Set it as an environment variable:
   - Mac/Linux: `export GEMINI_API_KEY="your_key_here"`
   - Windows PowerShell: `$env:GEMINI_API_KEY="your_key_here"`

## How to Run

Requires Python 3.10 or newer.

1. First get your API key and set it as an environment variable.
2. Run the following in terminal:

```
python <file-name>.py
```

## How It Works

1. The script reads the PDF into raw text using `read_pdf()`.
2. It calculates how many days are left until the exam using `days_until()`.
3. It builds those two pieces into a single prompt using `build_prompt()`.
4. It sends the prompt to Gemini and prints the response using `get_study_plan()`.

## Example Usage

```
Enter the pdf file path: example3.pdf
Enter the exam date("YYYY-MM-DD"): 2026-09-17
Your study plan:

Unit II: Data Engineering Life Cycle & Ecosystem

A 56-Day Hyper-Customized Mastery & Retention Study Plan

Program Architecture & Methodology

To guarantee a top-tier grade on your exam in 56 days, this plan abandons passive reading in favor of Cognitive Science-Backed Retrieval Practice and Spaced Repetition.

Phase 1: Deep-Dive Masterclass & First-Pass Retrieval (Days 1–21)
Day 1: Data Life Cycle (7 Stages)
Milestone: Memorize and explain the comprehensive, organization-wide lifespan of data.
Granular Study Focus: Study the 7 stages of the Data Life Cycle: Creation/Collection, Storage, Processing, Analysis, Distribution/Sharing, Archiving, Deletion.
Active Recall Prompts:
What is the fundamental difference between Processing and Analysis in the Data Life Cycle?
Why is "Archiving" considered a distinct step from "Deletion"?
Day 2: Data Engineering Life Cycle (8 Stages)
Milestone: Map out the technical, engineering-focused stages of pipeline development.
Granular Study Focus: Study the 8 stages: Requirement Gathering, Ingestion, Storage, Transformation, Orchestration, Quality/Validation, Deployment, Monitoring.

... (plan continues through Day 56, organized into 4 phases: Deep Acquisition, Consolidation, Simulation, and Peak Performance/Exam Day)

```
## Error Handling

- If a bad/wrong file path or API call error occurs, it's handled gracefully.
- If a PDF has no extractable text (or is image-only), it exits with a clear message.
- If the API fails or the user enters an invalid date, it's handled without crashing.

## What I Learned

- When dealing with the empty PDF logic, I encountered a real bug and learned to use a threshold check instead of a strict empty-string check.
- How to properly handle errors that occur on the API side, including live failures like a 503 server error.
- How to combine text extraction and an LLM API together to build a genuinely useful, working tool.