#!/usr/bin/env python3
"""
openLCA Database Explorer
Simple utility to export all flows and processes from an openLCA database to a text file via IPC.

Usage:
    python olca_explorer.py

Output:
    Creates olca_database_contents.txt with all flows and processes

Requirements:
    - openLCA running with IPC server enabled (Tools > Developer tools > IPC Server)
    - pip install olca-ipc
"""

import sys
from olca_ipc import Client
import olca_schema as o


def main():
    """Connect to openLCA and export all flows and processes to a text file."""
    try:
        # Connect to openLCA IPC server
        print("Connecting to openLCA IPC server...")
        client = Client(8080)
        print("✓ Connected successfully!")
        
        # Get all flows and processes
        print("Retrieving flows and processes...")
        flows = client.get_descriptors(o.Flow)
        processes = client.get_descriptors(o.Process)
        
        # Create output filename
        output_file = "olca_database_contents.txt"
        
        # Write to file
        print(f"Writing to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            # Header
            f.write("openLCA Database Contents\n")
            f.write("=" * 60 + "\n\n")
            
            # Flows section
            f.write("FLOWS\n")
            f.write("=" * 60 + "\n")
            f.write(f"Found {len(flows)} flows in the database:\n\n")
            
            for flow in sorted(flows, key=lambda f: f.name.lower()):
                f.write(f"Name: {flow.name}\n")
                f.write(f"UUID: {flow.id}\n")
                if hasattr(flow, 'category') and flow.category:
                    f.write(f"Category: {flow.category}\n")
                f.write("-" * 40 + "\n")
            
            # Processes section
            f.write("\n" + "=" * 60 + "\n")
            f.write("PROCESSES\n")
            f.write("=" * 60 + "\n")
            f.write(f"Found {len(processes)} processes in the database:\n\n")
            
            for process in sorted(processes, key=lambda p: p.name.lower()):
                f.write(f"Name: {process.name}\n")
                f.write(f"UUID: {process.id}\n")
                if hasattr(process, 'category') and process.category:
                    f.write(f"Category: {process.category}\n")
                f.write("-" * 40 + "\n")
            
            # Summary
            f.write("\n" + "=" * 60 + "\n")
            f.write("SUMMARY\n")
            f.write("=" * 60 + "\n")
            f.write(f"Total Flows: {len(flows)}\n")
            f.write(f"Total Processes: {len(processes)}\n")
            f.write(f"Total Entities: {len(flows) + len(processes)}\n")
        
        print(f"✓ Database contents exported to {output_file}")
        print(f"  - {len(flows)} flows")
        print(f"  - {len(processes)} processes")
        print(f"  - {len(flows) + len(processes)} total entities")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("Make sure openLCA is running with IPC server enabled:")
        print("Tools > Developer tools > IPC Server > Start")
        sys.exit(1)


if __name__ == "__main__":
    main()
