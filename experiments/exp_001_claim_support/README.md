# Experiment 001: Synthetic Claim Support Evaluation

## Overview

Mizan's first Python-based GenAI evaluation experiment. The objective is to learn Python functions, JSON handling, input validation, automated testing, and basic evaluation metrics.

**System:** Simulated Direct LLM  
**Dataset:** SYN-001, Version 1  
**Execution mode:** Simulated (no live AI model)

## Scenario

A fictional expense policy states:

> Expense claims above $500 require manager approval.

The simulated AI answer contains three claims: two supported and one unsupported by the policy.

The corrected answer removes the unsupported claim.

## Evaluation Metric

**Supported Claim Ratio = Supported Claims / Total Claims**

| Result | Baseline | Corrected |
|---|---:|---:|
| Supported claims | 2/3 | 2/2 |
| Support ratio | 66.67% | 100.00% |

These results use predefined human labels, not automated factual verification.

## Project Files

- `fixture.json`: Original synthetic claims.
- `fixture_corrected.json`: Corrected claims.
- `evaluate.py`: Dataset loading, validation, and evaluation.
- `../../tests/test_claim_support.py`: Automated tests.

## Run the Experiment

From the Mizan project root:

```powershell
python .\experiments\exp_001_claim_support\evaluate.py
```

Run automated tests:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

**Last verified result:** 9 tests passed.

## Key Learnings

- Writing reusable Python functions with type hints and docstrings.
- Reading JSON files and extracting structured data.
- Validating inputs and handling exceptions.
- Writing unit and integration tests.
- Comparing baseline and corrected outputs.
- Understanding evaluation metric limitations.

## Limitations

This experiment uses a small synthetic dataset with predefined labels. The support ratio measures grounding against the supplied source, not universal factual correctness, answer completeness, or real-world LLM performance.