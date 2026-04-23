# uv Package Manager Installation Guide

This guide covers **uv** installation for **Windows**, **macOS**, and **Linux** users using a single bash command.

---

## What is uv?

**uv** is an extremely fast Python package manager written in Rust, created by [Astral](https://astral.sh/). It's designed as a drop-in replacement for `pip` and `pip-tools`, but significantly faster.

---

## Install uv (same command for all platforms)

Use a **bash-style terminal**:

| Platform | Terminal |
|----------|----------|
| macOS | Terminal |
| Linux | Terminal |
| Windows | **Git Bash** |

Run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This is the official install method from Astral.

---

## Why this works cross-platform

- **uv** is written in Rust
- The installer script automatically:
  - Detects your OS (macOS / Linux / Windows)
  - Detects your CPU architecture
  - Downloads the correct binary
- Git Bash on Windows provides the POSIX layer (`curl`, `sh`, paths, etc.)

From the script's perspective, Windows Git Bash behaves like Linux/macOS.

---

## Verify Installation (same for everyone)

```bash
uv --version
which uv
```

**Expected output:**
- A version number (e.g., `uv 0.x.x`)
- A valid path (often `~/.cargo/bin/uv` or `~/.local/bin/uv`)

---

## Important Notes

### Windows Users

After installation, **restart Git Bash** (close and reopen) so the PATH updates are picked up.

Alternatively, reload your shell config:

```bash
source ~/.bashrc
```

### Alternative Installation for Windows (CMD/PowerShell)

If you're **not** using Git Bash, use Windows package manager instead:

```powershell
winget install Astral.uv
```

> **Note:** This is only needed if you cannot use Git Bash. For this course, we recommend using Git Bash for consistency.

---

## Quick Start with uv

Once installed, here are some common commands:

### Create a new project with virtual environment

```bash
uv venv
```

### Activate the virtual environment

```bash
# macOS / Linux / Git Bash
source .venv/bin/activate
```

### Install packages

```bash
uv pip install requests numpy pandas
```

### Install from requirements.txt

```bash
uv pip install -r requirements.txt
```

### Check installed packages

```bash
uv pip list
```

---

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `uv: command not found` | PATH not updated | Restart Git Bash or run `source ~/.bashrc` |
| `curl: command not found` | Not using Git Bash on Windows | Open Git Bash instead of CMD/PowerShell |
| Installation fails | Network/firewall issue | Try `winget install Astral.uv` on Windows |

---

## Summary

| Platform | Terminal | Install Command |
|----------|----------|-----------------|
| macOS | Terminal | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Linux | Terminal | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Windows | Git Bash | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

**One command, all platforms.**
