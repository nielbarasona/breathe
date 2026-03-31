# Breathe

A Python-based Terminal User Interface (TUI) for tracking service and
maintenance intervals.

Originally designed for monitoring CPAP machine maintenance schedules (filters,
masks, hoses, etc.), `breathe` is general-purpose enough to track recurring
service intervals for any equipment.

## Features

- **Interval Tracking**: Track when a part was last serviced and calculate the
next required service date.
- **TUI Interface**: (WIP) A clean, terminal-based interface for managing
service schedules.
- **Flexible**: Agnostic to the type of equipment; define any part and its
required maintenance interval in days.

## Development Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency
management and packaging.

### Prerequisites

- Python 3.13 or higher
- `uv` installed on your system

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd breathe
   ```

2. Sync the project dependencies:

   ```bash
   uv sync
   ```

### Running the App

To run the main CLI/TUI entry point:

```bash
uv run breathe
```

### Running Tests

This project uses `pytest` for testing.

```bash
uv run pytest
```

### Linting & Formatting

This project uses `ruff` for linting and formatting, and `pyright` for type checking.

```bash
# Run the ruff linter
uv run ruff check .

# Run the pyright type checker
uv run pyright
```

