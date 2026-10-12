#!/usr/bin/env python3

import json
import random
import sys
from pathlib import Path

def get_source_file() -> Path:
    """Resolve the path to the habits file relative to the script's location."""
    # __file__ gives the path to this script. .parent gets its directory.
    script_dir = Path(__file__).parent.resolve()
    
    personal_file = script_dir / "habits.json"
    example_file = script_dir / "habits.example.json"

    if personal_file.exists():
        return personal_file
    
    if example_file.exists():
        return example_file
        
    print(f"Error: Neither '{personal_file.name}' nor '{example_file.name}' found in {script_dir}", file=sys.stderr)
    sys.exit(1)

def load_habits(file_path: Path) -> list[str]:
    """Load and parse the habits JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON in {file_path.name}: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    source_file = get_source_file()
    habits = load_habits(source_file)
    
    if not habits:
        print("Error: The habits list is empty.", file=sys.stderr)
        sys.exit(1)

    print("\n╔══════════════════════════════════════╗")
    print("║          ATOMIC HABIT                ║")
    print("╚══════════════════════════════════════╝\n")
    print(f"  → {random.choice(habits)}\n")

if __name__ == "__main__":
    main()