#!/usr/bin/env python3
"""
Local SEO Report Generator

This script generates professional HTML reports from JSON data files.
Simply update your data JSON and run this script to create a new report.

Usage:
    python generate_report.py data/example_report.json
    python generate_report.py data/my_client.json --output output/my_client_report.html
"""

import argparse
import json
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, Template
from datetime import datetime


def load_json_data(json_path):
    """Load and parse JSON data file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ Loaded data from: {json_path}")
        return data
    except FileNotFoundError:
        print(f"✗ Error: File not found: {json_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON in {json_path}")
        print(f"  {str(e)}")
        sys.exit(1)


def setup_jinja_environment():
    """Set up Jinja2 template environment."""
    template_dir = Path(__file__).parent / 'templates'
    
    if not template_dir.exists():
        print(f"✗ Error: Templates directory not found: {template_dir}")
        sys.exit(1)
    
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    return env


def generate_report(data, template_env):
    """Generate HTML report from data using Jinja2 template."""
    try:
        template = template_env.get_template('report_template.html')
        html_output = template.render(**data)
        print("✓ Report generated successfully")
        return html_output
    except Exception as e:
        print(f"✗ Error generating report: {str(e)}")
        sys.exit(1)


def save_report(html_content, output_path):
    """Save the generated HTML report to file."""
    try:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Report saved to: {output_file}")
        print(f"\n📄 Open the file in your browser to view the report.")
        print(f"   You can then print to PDF (Ctrl+P or Cmd+P)")
        
        return output_file
    except Exception as e:
        print(f"✗ Error saving report: {str(e)}")
        sys.exit(1)


def get_default_output_name(input_path):
    """Generate default output filename based on input filename."""
    input_file = Path(input_path)
    company_name = input_file.stem
    timestamp = datetime.now().strftime("%Y%m%d")
    return f"output/{company_name}_report_{timestamp}.html"


def main():
    """Main function to orchestrate report generation."""
    parser = argparse.ArgumentParser(
        description='Generate professional Local SEO reports from JSON data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_report.py data/example_report.json
  python generate_report.py data/my_client.json -o output/custom_name.html
  python generate_report.py data/my_client.json --output output/report.html

After generating the report:
  1. Open the HTML file in your web browser
  2. Print to PDF (Ctrl+P or Cmd+P)
  3. Import the PDF to Canva for final design touches
        """
    )
    
    parser.add_argument(
        'input',
        help='Path to the JSON data file (e.g., data/example_report.json)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output path for the HTML report (default: output/[input_name]_report_[date].html)',
        default=None
    )
    
    args = parser.parse_args()
    
    # Determine output path
    output_path = args.output if args.output else get_default_output_name(args.input)
    
    print("\n" + "="*60)
    print("  LOCAL SEO REPORT GENERATOR")
    print("="*60 + "\n")
    
    # Load data
    data = load_json_data(args.input)
    
    # Setup Jinja2
    template_env = setup_jinja_environment()
    
    # Generate report
    html_content = generate_report(data, template_env)
    
    # Save to file
    output_file = save_report(html_content, output_path)
    
    print("\n" + "="*60)
    print("  ✓ REPORT GENERATION COMPLETE")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()

