# ASS-Sniffer
**Alternate Stream Scanner & Sniffing Tool**

---

## Overview

**ASS-Sniffer** is a Windows-based interactive tool for **detecting, viewing, and extracting Alternate Data Streams (ADS)** from NTFS file systems.  
It leverages PowerShell under the hood to enumerate hidden streams, display their contents, and optionally export them.

> **Version:** `0.2.0-alpha`  
> **Status:** Alpha — expect bugs, missing features, and possibly explosions

## Features

- **Scan files for ADS** — Quickly list all alternate data streams for a given file.
- **View ADS contents** — Open and display the data inside hidden streams.
- **Save ADS to a file** — Extract and save stream contents for further analysis.
- **Interactive mode** — Easy-to-follow menus with overwrite protection.
- **PowerShell integration** — Uses native Windows APIs for reliability.

---

## Installation

### **Prerequisites**
- **Windows 10 or later** (NTFS filesystem required)
- **PowerShell** (included in Windows)
- **Python 3.9+**
- `git` (optional, for cloning)

### **Clone the Repository**
```bash
git clone https://github.com/ABeimbornCyber/ASS-Sniffer.git
cd ASS-Sniffer
```

---

## Usage

Run the tool directly using Python:
```bash
python ass_sniffer.py
```
You'll be greeted with an interactive menu!

```bash
Welcome to Alternate Stream Scanner (ASS) and Sniffing Tool!
The Interactive ADS Tool!

Please make a selection:
[1] Scan a specific file for ADS
[2] View a file's ADS (Interactive)
[3] Save a file's ADS (Interactive)
[4] Quit Tool
```

### Example: Scanning a file for ADS

```bash
> python ass_sniffer.py
[1] Scan a specific file for ADS
Selection: 1
Enter the name of the file: secret.txt

==== RESULTS ====
Data Stream: hidden_payload.txt
Length: 2048
PSChildName: secret.txt
----------------------------
```

### Example: Saving ADS Content

```bash
Selection: 3
Enter the name of the file to extract an ADS from: secret.txt
[0]: hidden_payload.txt
[1]: metadata.json

Enter the ADS number: 0
Name for save file: extracted_payload.txt
File SAVED
```
---

## Disclaimer

This tool is provided as-is for educational and forensic purposes only.
Do not use it for malicious activity.
The author assumes no liability for misuse.


Feel free to fork the repo, open issues, or submit PRs!
For major changes, please open a discussion first.



MIT License © 2025 — Aaron Beimborn

Soli Deo Gloria



