import json
from pathlib import Path

def calculate_support_ratio(labels: list[bool]) -> float:
    """Calculate the proportion of supported claims.

    Args:
        labels: Non-empty list of Boolean claim-support labels.
            True indicates supported; False indicates unsupported.

    Returns:
        A float between 0.0 and 1.0 representing the support ratio.

    Raises:
        ValueError: If the list is empty or contains non-Boolean labels.
    """

    if len(labels) == 0:
        raise ValueError("Cannot calculate support ratio: no claims provided.")

    for label in labels:
        if type(label) is not bool:
            raise ValueError("Claim support labels must be Boolean values.")
        
    return sum(labels) / len(labels)


def load_dataset(fixture_path: Path) -> dict:
    """Load a synthetic evaluation dataset from a JSON file.

    Args:
        fixture_path: Path to the JSON dataset file.

    Returns:
        The parsed dataset as a Python dictionary.

    Raises:
        OSError: If the file cannot be opened or read.
        json.JSONDecodeError: If the file contains invalid JSON.
    """

    with fixture_path.open("r", encoding="utf-8") as file:
            dataset = json.load(file)
            
    return dataset


def evaluate_fixture(fixture_path: Path) -> float:
    """Evaluate claim support using a synthetic JSON fixture.
    
    Args:
        fixture_path: Path to the versioned evaluation fixture.
        
    Returns:
        The supported claim ratio as a float between 0.0 and 1.0.
        
    Raises:
        OSError: If the fixture cannot be read.
        json.JSONDecodeError: If the JSON is malformed.
        KeyError: If a required dataset field is missing.
        ValueError: If claim labels are empty or invalid.
    """

    claims = load_dataset(fixture_path)["claims"]
    labels = []

    for claim in claims:
        labels.append(claim["supported"])

    return calculate_support_ratio(labels)


if __name__ == "__main__":
    baseline_path = Path(__file__).with_name("fixture.json")
    corrected_path = Path(__file__).with_name("fixture_corrected.json")

    baseline_ratio = evaluate_fixture(baseline_path)
    corrected_ratio = evaluate_fixture(corrected_path)

    print(f"Baseline support ratio: {baseline_ratio:.2%}")
    print(f"Corrected support ratio: {corrected_ratio:.2%}")
