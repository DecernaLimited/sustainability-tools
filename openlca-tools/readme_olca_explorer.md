# openLCA Database Explorer

Simple Python script to export all flows and processes from an openLCA database to a text file via IPC.

## Requirements

- openLCA running with IPC server enabled
- Python 3.6 or higher
- `pip install olca-ipc`

## Setup

1. **Install the package:**
   ```bash
   pip install olca-ipc
   ```

2. **Start openLCA IPC server:**
   - Open openLCA
   - Open your database
   - Go to **Tools → Developer tools → IPC Server**
   - Click **Start** (default port: 8080)

## Usage

Simply run the script:

```bash
python olca_explorer.py
```

The script will create a file called `olca_database_contents.txt` with all your database contents.

## Output

The script creates a text file containing:

1. **All flows** with names, UUIDs, and categories
2. **All processes** with names, UUIDs, and categories  
3. **Summary statistics** showing total counts

Console output:
```
Connecting to openLCA IPC server...
✓ Connected successfully!
Retrieving flows and processes...
Writing to olca_database_contents.txt...
✓ Database contents exported to olca_database_contents.txt
  - 1,234 flows
  - 567 processes
  - 1,801 total entities
```

The generated text file will look like:
```
openLCA Database Contents
============================================================

FLOWS
============================================================
Found 1,234 flows in the database:

Name: Electricity, medium voltage
UUID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
Category: Energy/Electricity
----------------------------------------
```

## Troubleshooting

**Connection failed?**
- Make sure openLCA is running
- Check IPC server is started (Tools → Developer tools → IPC Server)
- Default port is 8080

**Missing package?**
- Run: `pip install olca-ipc`

Perfect for documenting your openLCA database contents!