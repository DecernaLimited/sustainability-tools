#!/usr/bin/env python3
"""
Example usage of the openLCA Database Explorer
==============================================

This script demonstrates how to use the OpenLCAExplorer class
in your own Python projects for programmatic database exploration.
"""

from olca_explorer import OpenLCAExplorer


def example_basic_usage():
    """Basic usage example - connect and get summary."""
    print("=== Basic Usage Example ===")
    
    # Create explorer instance
    explorer = OpenLCAExplorer()
    
    # Connect to openLCA
    if not explorer.connect():
        print("Failed to connect to openLCA")
        return
    
    # Get database summary
    summary = explorer.get_database_summary()
    print(f"Database contains:")
    print(f"  - {summary['flows']} flows")
    print(f"  - {summary['processes']} processes")
    print(f"  - {summary['total_entities']} total entities")


def example_flow_analysis():
    """Example of analyzing flows in the database."""
    print("\n=== Flow Analysis Example ===")
    
    explorer = OpenLCAExplorer()
    
    if not explorer.connect():
        return
    
    flows = explorer.get_flows()
    
    # Analyse flow types
    flow_types = {}
    categories = {}
    
    for flow in flows:
        # Count flow types
        flow_type = getattr(flow, 'flow_type', 'Unknown')
        flow_types[flow_type] = flow_types.get(flow_type, 0) + 1
        
        # Count categories
        category = getattr(flow, 'category', 'No category')
        categories[category] = categories.get(category, 0) + 1
    
    print("Flow Types:")
    for flow_type, count in sorted(flow_types.items()):
        print(f"  {flow_type}: {count}")
    
    print(f"\nTop 5 Flow Categories:")
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    for category, count in sorted_categories[:5]:
        print(f"  {category}: {count}")


def example_process_search():
    """Example of searching for specific processes."""
    print("\n=== Process Search Example ===")
    
    explorer = OpenLCAExplorer()
    
    if not explorer.connect():
        return
    
    processes = explorer.get_processes()
    
    # Search for processes containing specific keywords
    search_terms = ['electricity', 'transport', 'steel']
    
    for term in search_terms:
        matching_processes = [
            p for p in processes 
            if term.lower() in p.name.lower()
        ]
        
        print(f"\nProcesses containing '{term}': {len(matching_processes)}")
        
        # Show first 3 matches
        for process in matching_processes[:3]:
            print(f"  - {process.name}")
        
        if len(matching_processes) > 3:
            print(f"  ... and {len(matching_processes) - 3} more")


def example_remote_connection():
    """Example of connecting to a different port."""
    print("\n=== Different Port Example ===")
    
    # This would connect to a different port
    # Uncomment and modify for your setup
    # explorer = OpenLCAExplorer(port=8081)
    
    # For demonstration, we'll just show the default connection
    explorer = OpenLCAExplorer(port=8080)
    
    if explorer.connect():
        print(f"Successfully connected to localhost:{explorer.port}")
        summary = explorer.get_database_summary()
        print(f"Database has {summary['total_entities']} entities")
    else:
        print("Failed to connect to server")


def example_export_to_csv():
    """Example of exporting database contents to CSV."""
    print("\n=== CSV Export Example ===")
    
    import csv
    
    explorer = OpenLCAExplorer()
    
    if not explorer.connect():
        return
    
    # Export flows to CSV
    flows = explorer.get_flows()
    
    with open('flows_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'UUID', 'Type', 'Category'])
        
        for flow in flows:
            writer.writerow([
                flow.name,
                flow.id,
                getattr(flow, 'flow_type', 'Unknown'),
                getattr(flow, 'category', 'No category')
            ])
    
    print(f"Exported {len(flows)} flows to 'flows_export.csv'")
    
    # Export processes to CSV
    processes = explorer.get_processes()
    
    with open('processes_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'UUID', 'Type', 'Category'])
        
        for process in processes:
            writer.writerow([
                process.name,
                process.id,
                getattr(process, 'process_type', 'Unknown'),
                getattr(process, 'category', 'No category')
            ])
    
    print(f"Exported {len(processes)} processes to 'processes_export.csv'")


if __name__ == "__main__":
    """Run all examples."""
    print("openLCA Database Explorer - Usage Examples")
    print("=" * 50)
    
    try:
        example_basic_usage()
        example_flow_analysis()
        example_process_search()
        example_remote_connection()
        example_export_to_csv()
        
        print("\n✓ All examples completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⚠ Examples interrupted by user")
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        print("Make sure openLCA is running with IPC server enabled")