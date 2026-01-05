# GitHub Copilot instructions for this repository

## Purpose
- Short, focused instructions to help AI agents contribute confidently to this small Python project.

## Quick context
- Repo is tiny: primary files are `README.md` and `test1.py` (current `test1.py` contains a single `print("Hello world")`).
- No dependency or CI config found in the repository.

## What to do first (high-impact, low-risk)
1. Run the project locally to confirm behavior:
   - Windows: `py -3 -m venv .venv && .\.venv\Scripts\Activate.ps1` (PowerShell) or `.\.venv\Scripts\activate` (cmd).
   - Run: `python test1.py` (expected output: `Hello world`).
2. If adding behavior, keep changes small and testable: convert script-level code into functions before adding logic.

## Conventions and patterns to follow
- Keep modules small and single-responsibility. Example: refactor `test1.py` to:

```python
# test1.py
def main():
    print("Hello world")

if __name__ == "__main__":
    main()
```

- Add unit tests in `tests/` using `pytest`. Example test for the snippet above:

```python
# tests/test_main.py
from test1 import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello world" in captured.out
```

- If you introduce dependencies, add a `requirements.txt` at the repo root and pin versions.

## Testing & debugging
- Preferred test tool: `pytest` (no config found yet). Run tests with: `py -3 -m pytest`.
- For simple debugging, use: `python -m pdb test1.py` or VS Code Run/Debug.

## Project files to reference
- `README.md` — very small; update when adding features or usage examples.
- `test1.py` — current entry point / example code. Use as template for converting scripts into modules.

## CI / PR guidance (repo currently has no CI)
- If you add CI, use `.github/workflows/ci.yml` and include steps: set up Python, install from `requirements.txt`, run `pytest`.
- Make PRs small, one logical change per PR; include unit tests for added behavior.

## When merging updates to this instructions file
- If `.github/copilot-instructions.md` already exists, merge carefully by preserving existing actionable bullets and examples. Keep file short (20–50 lines) and focused on concrete repo-specific steps.

---

If anything here is unclear or you want extra sections (e.g., CI template, contribution checklist, or example issues), tell me which one to add and I will expand this file.