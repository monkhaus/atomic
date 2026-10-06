#!/usr/bin/env python3

import json
from pathlib import Path
import random

# Use personal habits.json if it exists, otherwise fall back to habits.example.json
source_file = Path("habits.json") if Path("habits.json").exists() else Path("habits.example.json")

with open(source_file, "r", encoding="utf-8") as f:
    habits = json.load(f)

print()
print("╔══════════════════════════════════════╗")
print("║          ATOMIC HABIT                ║")
print("╚══════════════════════════════════════╝")
print()
print(f"  → {random.choice(habits)}")
print()