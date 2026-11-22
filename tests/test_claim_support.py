"""Unit test for the synthetic claim support evaluator."""

import unittest
from pathlib import Path

from experiments.exp_001_claim_support.evaluate import (
    calculate_support_ratio,
    load_dataset,
    evaluate_fixture
)


class TestClaimSupport(unittest.TestCase):
    """Verify the claim support metric's expected behavior."""
    
    def test_two_of_three_claims_supported(self):
        """Return the correct ratio when two of three claims are supported."""
        labels = [True, False, True]

        result = calculate_support_ratio(labels)

        self.assertAlmostEqual(result, 2 / 3)

    def test_empty_labels(self):
        """Reject an empty list because the ratio is undefined."""
        labels = []

        with self.assertRaises(ValueError):
            calculate_support_ratio(labels)

    def test_invalid_label(self):
        """Reject non-Boolean claim support labels."""
        labels = [True, 1, False]

        with self.assertRaises(ValueError):
            calculate_support_ratio(labels)

    def test_all_claims_supported(self):
        """Return 1.0 when every claim is supported."""
        labels = [True, True, True]

        result = calculate_support_ratio(labels)

        self.assertEqual(result, 1.0)

    def test_no_claims_supported(self):
        """Return 0.0 when every claim is unsupported."""
        labels = [False, False, False]

        result = calculate_support_ratio(labels)

        self.assertEqual(result, 0.0)

    def test_fixture_labels(self):
        """Load the synthetic fixture and verify its claim labels."""
        project_root = Path(__file__).resolve().parent.parent

        fixture_path = (
            project_root
            / "experiments"
            / "exp_001_claim_support"
            / "fixture.json"
        )

        dataset = load_dataset(fixture_path)

        claims = dataset["claims"]
        labels = []

        for claim in claims:
            labels.append(claim["supported"])

        self.assertEqual(labels, [True, False, True])

    def test_evaluate_corrected_fixture(self):
        """Evaluate the corrected synthetic answer using the reusable workflow."""
        project_root = Path(__file__).resolve().parent.parent

        fixture_path = (
            project_root
            / "experiments"
            / "exp_001_claim_support"
            / "fixture_corrected.json"
        )

        result = evaluate_fixture(fixture_path)

        self.assertEqual(result, 1.0)

    def test_evaluate_baseline_fixture(self):
        """Evaluate the original synthetic answer using the reusable workflow."""
        project_root = Path(__file__).resolve().parent.parent

        fixture_path = (
                project_root
                / "experiments"
                / "exp_001_claim_support"
                / "fixture.json"
            )
        
        result = evaluate_fixture(fixture_path)

        self.assertAlmostEqual(result, 2 / 3)
