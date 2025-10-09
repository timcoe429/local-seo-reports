# 🎯 Get Started in 3 Steps

Welcome to your Local SEO Report Generator! Here's the fastest way to get up and running.

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate Example Report
```bash
python generate_report.py data/example_report.json
```

### Step 3: View Your Report
- Go to the `output/` folder
- Open the HTML file in your browser
- That's it! 🎉

---

## 📖 What's What

Your repository contains:

| File | What It Does |
|------|--------------|
| **generate_report.py** | Main script - generates HTML from JSON |
| **requirements.txt** | Dependencies to install |
| **data/example_report.json** | Full working example (American Dumpster Co.) |
| **data/_template.json** | Blank template to copy for new reports |
| **templates/report_template.html** | HTML template with your design |

## 📚 Documentation Files

| File | When to Read It |
|------|-----------------|
| **GET_STARTED.md** | ← You are here! |
| **QUICKSTART.md** | First time using the system |
| **README.md** | Complete documentation |
| **WORKFLOW.md** | How to create reports from scratch |
| **SETUP_CHECKLIST.md** | Step-by-step setup guide |
| **PROJECT_SUMMARY.md** | Technical overview |

---

## 🚀 Your First Custom Report

### 1. Copy the Template
```bash
# Windows
copy data\_template.json data\my_client.json

# Mac/Linux
cp data/_template.json data/my_client.json
```

### 2. Edit the JSON File
Open `data/my_client.json` in any text editor and fill in:
- Company name
- All metrics (DA, reviews, traffic, etc.)
- Analysis text
- Competitor data
- Recommendations

### 3. Generate Report
```bash
python generate_report.py data/my_client.json
```

### 4. Export to PDF
1. Open HTML in browser
2. Ctrl+P (or Cmd+P)
3. Save as PDF
4. **Enable "Background graphics"**

### 5. Optional: Add to Canva
- Upload PDF to Canva
- Add logos and branding
- Export final version

---

## 🎨 Adding Screenshots

In your JSON file, add image URLs:

```json
"domain_authority": {
  "screenshot": "https://example.com/screenshot.jpg",
  ...
}
```

**Using Dropbox:**
1. Upload screenshot to Dropbox
2. Get share link
3. Change `dl=0` to `raw=1` in URL
4. Use in JSON

**No screenshots yet?** Leave empty (`""`) and add them in Canva later!

---

## 💡 Key Tips

✅ **Validate JSON**: Use [jsonlint.com](https://jsonlint.com) before generating  
✅ **Start Simple**: Use example_report.json as reference  
✅ **Test Often**: Regenerate frequently while building  
✅ **Save Templates**: Create industry-specific templates  
✅ **Enable Background Graphics**: Required for PDF colors  

---

## 🆘 Something Not Working?

### "Python not found"
Install Python from [python.org](https://www.python.org/downloads/)

### "Invalid JSON"
Check your JSON syntax at [jsonlint.com](https://jsonlint.com)

### "Template not found"
Make sure you're in the project root directory

### "Screenshots not showing"
Verify URLs are direct image links

### "PDF colors missing"
Enable "Background graphics" in print settings

---

## 📖 Next Steps

1. ✅ Generate example report (test)
2. ✅ Review the HTML output
3. ✅ Test PDF export
4. ✅ Read **WORKFLOW.md** for full process
5. ✅ Create your first real client report!

---

## 🎯 Command Cheat Sheet

```bash
# Generate report (auto-named output)
python generate_report.py data/client.json

# Generate with custom output name
python generate_report.py data/client.json -o output/custom_name.html

# Get help
python generate_report.py --help
```

---

## 📊 What Data You Need

For each report, gather:
- [ ] Company name
- [ ] Domain Authority metrics
- [ ] Review counts and ratings
- [ ] Citation data
- [ ] Traffic numbers
- [ ] Competitor information
- [ ] Screenshots (optional)

See **WORKFLOW.md** for complete checklist!

---

## 🎉 You're Ready!

Everything is set up and ready to go. Your system can now generate professional Local SEO reports in minutes instead of hours.

**Ready to create your first report?**  
Follow the steps above or jump to **QUICKSTART.md**!

---

## 📞 Documentation Quick Links

- **Just getting started?** → Read this file (GET_STARTED.md)
- **First time setup?** → Read QUICKSTART.md
- **Creating a report?** → Read WORKFLOW.md
- **Need full details?** → Read README.md
- **Want a checklist?** → Read SETUP_CHECKLIST.md
- **Technical overview?** → Read PROJECT_SUMMARY.md

---

**Happy reporting! 🚀**

Questions? Check the README.md or modify the system to fit your needs!

