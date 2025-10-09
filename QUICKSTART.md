# 🚀 Quick Start Guide

Get your first Local SEO report generated in **5 minutes**!

## Step 1: Install Python (if needed)

**Check if you have Python:**
```bash
python --version
```

If you don't have Python installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/) (get Python 3.8+)
- **Mac**: `brew install python3` or download from [python.org](https://www.python.org/downloads/)
- **Linux**: `sudo apt install python3 python3-pip` (Ubuntu/Debian)

## Step 2: Setup

```bash
# Navigate to the project folder
cd local-seo-reports

# Install required packages
pip install -r requirements.txt
```

That's it! You're ready to generate reports.

## Step 3: Generate Your First Report

```bash
# Test with the example data
python generate_report.py data/example_report.json
```

You should see:
```
============================================================
  LOCAL SEO REPORT GENERATOR
============================================================

✓ Loaded data from: data/example_report.json
✓ Report generated successfully
✓ Report saved to: output/example_report_20251009.html

📄 Open the file in your browser to view the report.
   You can then print to PDF (Ctrl+P or Cmd+P)

============================================================
  ✓ REPORT GENERATION COMPLETE
============================================================
```

## Step 4: View Your Report

1. Navigate to the `output/` folder
2. Double-click the HTML file (or right-click → Open with → Browser)
3. You'll see your beautiful report!

## Step 5: Create Your Own Report

```bash
# Copy the example file
cp data/example_report.json data/my_client.json

# Edit the file with your client's data
# Use Notepad, VS Code, or any text editor

# Generate the new report
python generate_report.py data/my_client.json
```

## Step 6: Export to PDF

1. Open the HTML report in your browser
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Choose "Save as PDF"
4. **Important**: Enable "Background graphics" for colors!
5. Save your PDF

## Step 7: Canva (Optional)

1. Open Canva
2. Upload your PDF
3. Add logos, branding, and design elements
4. Export and deliver to client!

---

## 📝 Quick Data Reference

Here's what you need to gather for a new report:

### Client Information
- [ ] Company name
- [ ] Report date
- [ ] Current ranking position
- [ ] Review count and rating

### SEO Metrics
- [ ] Domain Authority (DA)
- [ ] Trust Flow
- [ ] Citation Flow
- [ ] Total backlinks
- [ ] Linking domains
- [ ] Monthly organic traffic

### Local SEO Data
- [ ] Citations completed / total
- [ ] NAP errors count
- [ ] Average map ranking
- [ ] Google Business Profile data

### Screenshots (optional - can add later)
- [ ] Domain authority screenshot
- [ ] Citation report screenshot
- [ ] Reputation management screenshot
- [ ] Search grid screenshot
- [ ] Competitive analysis screenshot
- [ ] Website screenshot

### Competitor Data
- [ ] Top 5 competitors
- [ ] Their rankings, reviews, ratings
- [ ] Their backlink counts

---

## 🔥 Pro Tips

1. **Start with placeholders**: Don't wait for screenshots - generate the report with empty screenshot URLs and add them later in Canva

2. **Save a template**: Create `data/_template.json` with your standard structure and copy it for each new client

3. **Batch generation**: Put all client JSON files in `data/` and generate them all at once

4. **Version control**: Name your files like `data/clientname_2025_10.json` to track different report versions

5. **Test first**: Always test with example data before creating a client report

---

## ⚡ Common Commands

```bash
# Generate report
python generate_report.py data/your_file.json

# Generate with custom output name
python generate_report.py data/client.json -o output/ClientName_October_2025.html

# Get help
python generate_report.py --help
```

---

## 🆘 Need Help?

- **JSON errors**: Use [jsonlint.com](https://jsonlint.com) to validate your JSON
- **Python not found**: Make sure Python is installed and in your PATH
- **Template errors**: Check that `templates/report_template.html` exists
- **Styling issues**: Make sure "Background graphics" is enabled when printing to PDF

---

**You're all set! 🎉**

Create amazing Local SEO reports in minutes!

