# Local SEO Report Generator

A streamlined system for creating professional Local SEO performance reports for businesses. Generate beautiful, data-driven HTML reports that can be converted to PDF and imported into Canva for final design touches.

## 🎯 Purpose

This tool makes it **SUPER easy** to create new Local SEO reports for clients. Simply:
1. Copy the example data file
2. Update the data with your client's information
3. Run the generator script
4. Get a professional HTML report ready for PDF export

## 📋 Features

- **Professional Design**: Modern, clean template with excellent print/PDF output
- **Easy to Use**: Update JSON data, run one command, get your report
- **Fully Customizable**: Every section can be customized via the JSON data file
- **Print-Optimized**: Built-in print styles for clean PDF generation
- **Canva-Ready**: Export to PDF and import directly into Canva for branding

## 🚀 Quick Start

### 1. Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/local-seo-reports.git
cd local-seo-reports

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Create Your First Report

```bash
# Generate report from example data
python generate_report.py data/example_report.json

# The report will be saved to: output/example_report_YYYYMMDD.html
```

### 3. Create a Custom Report

```bash
# Copy the example data file
cp data/example_report.json data/my_client.json

# Edit data/my_client.json with your client's data
# (Use any text editor or VS Code)

# Generate the report
python generate_report.py data/my_client.json

# Custom output path (optional)
python generate_report.py data/my_client.json -o output/custom_name.html
```

### 4. Convert to PDF

1. Open the generated HTML file in your web browser
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
3. Select "Save as PDF" as the destination
4. Recommended PDF settings:
   - Paper size: Letter (8.5 x 11 inches)
   - Margins: Default or Minimum
   - Background graphics: **Enabled** (important for colors!)
5. Save the PDF

### 5. Import to Canva

1. Open Canva and create a new design
2. Upload your PDF file
3. Add your branding elements, logos, and final design touches
4. Export and share with your client!

## 📁 Project Structure

```
local-seo-reports/
├── data/                      # JSON data files
│   └── example_report.json    # Example report with all fields
├── templates/                 # HTML templates
│   └── report_template.html   # Main report template
├── output/                    # Generated HTML reports
├── generate_report.py         # Main generator script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 📝 Customizing Your Report

### JSON Data Structure

The `data/example_report.json` file contains all the data for your report. Key sections include:

- **company**: Business name and basic info
- **report_date**: Date of the report (e.g., "October 2025")
- **cover**: Cover page metrics and subtitle
- **executive_summary**: Strengths, weaknesses, opportunities, KPIs
- **domain_authority**: DA metrics and analysis
- **citations**: Citation data and NAP consistency
- **reputation**: Review data and analysis
- **search_grid**: Local search grid performance
- **competitive_analysis**: Competitor comparison data
- **market_threat**: Optional market expansion analysis
- **website_cro**: Conversion rate optimization analysis
- **organic_traffic**: Traffic metrics and projections
- **recommendations**: Strategic action items
- **final_summary**: Executive overview and timeline

### Adding Screenshots

In your JSON data file, you can add screenshot URLs to any section:

```json
"domain_authority": {
  "screenshot": "https://your-image-url.com/screenshot.jpg",
  ...
}
```

**Supported image sources:**
- Direct URLs (Dropbox, Google Drive, etc.)
- Relative paths (place images in a folder and reference them)
- Base64 encoded images (for fully self-contained reports)

**To use Dropbox:**
1. Upload your screenshot to Dropbox
2. Get the share link
3. Change `dl=0` to `raw=1` at the end of the URL
4. Use this URL in your JSON file

### Optional Sections

The `market_threat` section is optional. To exclude it from your report:

```json
{
  "company": { ... },
  ...
  // Simply omit the "market_threat" key, or set it to null
  "market_threat": null,
  ...
}
```

The report will automatically adjust section numbering.

## 🎨 Customizing the Template

### Colors

To change the brand color (default: `#0f58a8` blue):

1. Open `templates/report_template.html`
2. Search for `#0f58a8`
3. Replace with your brand color
4. Regenerate your report

### Fonts

The template uses:
- **Poppins** for headings
- **Montserrat** for body text

To change fonts, update the Google Fonts link in `templates/report_template.html`.

### Layout

The template is built with CSS Grid and Flexbox for easy customization. Key classes:
- `.three-col-section` - Three-column layout sections
- `.insight-box` - Blue insight boxes
- `.warning-box` - Orange warning boxes
- `.data-row` - Key metrics display
- `.competitor-table` - Competitor comparison tables

## 🔧 Advanced Usage

### Command Line Options

```bash
# Basic usage
python generate_report.py data/client.json

# Custom output path
python generate_report.py data/client.json -o output/custom_name.html

# Help
python generate_report.py --help
```

### Batch Processing

Generate multiple reports at once:

```bash
# Windows (PowerShell)
Get-ChildItem data\*.json | ForEach-Object { python generate_report.py $_.FullName }

# Mac/Linux (Bash)
for file in data/*.json; do python generate_report.py "$file"; done
```

### Using Without Screenshots

If you don't have screenshots yet, just leave the screenshot URLs empty:

```json
"domain_authority": {
  "screenshot": "",
  ...
}
```

The report will render without the image, leaving space for you to add it later in Canva.

## 🐛 Troubleshooting

### "File not found" error
- Make sure you're running the command from the project root directory
- Check that your JSON file path is correct

### "Invalid JSON" error
- Use a JSON validator (like jsonlint.com) to check your JSON syntax
- Common issues: missing commas, unescaped quotes, trailing commas

### Colors not showing in PDF
- Make sure "Background graphics" is enabled in your print dialog
- Try using Chrome or Firefox for better PDF export support

### Template not found
- Make sure the `templates/` directory exists
- Check that `report_template.html` is in the templates folder

## 📚 Tips & Best Practices

1. **Keep a template**: Create a "template" JSON file with placeholder text to speed up new reports
2. **Version control**: Use Git branches for different clients or report versions
3. **Image optimization**: Compress screenshots before adding them to reduce file size
4. **Backup data**: Keep your JSON data files in a secure location
5. **Test first**: Generate a test report with example data before customizing

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Suggest new features
- Improve documentation
- Add new template sections

## 📄 License

This project is licensed under the MIT License - feel free to use it for commercial projects!

## 🙋 Support

Need help? Check out:
- Example data file: `data/example_report.json`
- Template comments: `templates/report_template.html`
- Script help: `python generate_report.py --help`

---

**Made with ❤️ for digital marketing professionals**

Ready to create amazing Local SEO reports in minutes instead of hours!
