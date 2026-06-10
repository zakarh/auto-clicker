# Auto Clicker

A lightweight Windows auto-clicker written in Python using `ctypes` — no third-party dependencies required.

## Requirements

- Windows
- Python 3.x

## Usage

```
python auto_clicker.py
```

## Controls

| Key | Action |
|-----|--------|
| F8 | Start / stop clicking |
| ESC | Exit the program |

## Configuration

The click interval defaults to **10ms** (100 clicks/sec). To change it, edit the `delay` variable near the top of [auto_clicker.py](auto_clicker.py):

```python
delay = 0.01  # seconds between clicks
```
