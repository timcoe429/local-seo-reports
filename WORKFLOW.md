# 📋 Workflow Guide

This guide shows you the complete workflow from data collection to client delivery.

## 🔄 Complete Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Gather Client Data                                 │
│  ├─ Run SEO audit tools (SEMrush, Moz, BrightLocal, etc.)  │
│  ├─ Collect Google Business Profile data                    │
│  ├─ Analyze competitor information                          │
│  ├─ Take screenshots of key reports                         │
│  └─ Compile all metrics and findings                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Create Data File                                   │
│  ├─ Copy: data/_template.json → data/clientname.json       │
│  ├─ Fill in client information                              │
│  ├─ Add all metrics and KPIs                                │
│  ├─ Write analysis sections                                 │
│  └─ Add screenshot URLs (or leave empty)                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Generate Report                                    │
│  └─ Run: python generate_report.py data/clientname.json    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Review HTML Report                                 │
│  ├─ Open HTML file in browser                               │
│  ├─ Check all data is correct                               │
│  ├─ Verify formatting looks good                            │
│  └─ Make adjustments to JSON if needed                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Export to PDF                                      │
│  ├─ Press Ctrl+P (or Cmd+P)                                 │
│  ├─ Choose "Save as PDF"                                    │
│  ├─ Enable "Background graphics"                            │
│  └─ Save PDF file                                           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Design in Canva (Optional)                         │
│  ├─ Upload PDF to Canva                                     │
│  ├─ Add brand colors and logos                              │
│  ├─ Add design elements                                     │
│  ├─ Insert missing screenshots if needed                    │
│  └─ Export final branded PDF                                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 7: Deliver to Client                                  │
│  └─ Send final PDF via email or client portal               │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Data Collection Checklist

Use this checklist when gathering data for a new report:

### Basic Information
- [ ] Company name
- [ ] Report date (e.g., "October 2025")
- [ ] Industry/business type
- [ ] Primary service area/location

### Cover Page Metrics
- [ ] Current ranking position (#X)
- [ ] Total Google reviews
- [ ] Average star rating

### Domain & Technical SEO
- [ ] Domain Authority (DA)
- [ ] Trust Flow (TF)
- [ ] Citation Flow (CF)
- [ ] Total backlinks
- [ ] Number of linking domains
- [ ] Authority Score (if available)

### Citations & NAP
- [ ] Total citations possible
- [ ] Citations completed
- [ ] NAP consistency errors
- [ ] Address inconsistencies count
- [ ] Phone inconsistencies count

### Reviews & Reputation
- [ ] Google review count and rating
- [ ] Yelp review count and rating
- [ ] Facebook review count and rating (optional)
- [ ] Reviews in last 30 days
- [ ] Review velocity (reviews/month)

### Local Search Performance
- [ ] Average map ranking position
- [ ] Primary keyword(s) tracked
- [ ] Local search grid data
- [ ] Map pack appearances

### Organic Traffic
- [ ] Monthly organic visits
- [ ] Total ranking keywords
- [ ] Keywords in top 10
- [ ] Traffic trend (% change)
- [ ] Estimated monthly leads from organic

### Competitive Analysis
For each top 5 competitor:
- [ ] Business name
- [ ] Average ranking position
- [ ] Review count
- [ ] Star rating
- [ ] Backlink count

### Website CRO
- [ ] Current CTAs on homepage
- [ ] Conversion rate (if known)
- [ ] Key UX issues identified
- [ ] Mobile responsiveness notes

### Screenshots (Optional)
- [ ] Domain authority dashboard
- [ ] Citations report
- [ ] Review management dashboard
- [ ] Local search grid
- [ ] Competitor comparison
- [ ] Website homepage
- [ ] Traffic analytics

---

## 💡 Time-Saving Tips

### 1. Create Client Templates
Save pre-filled templates for different industries:
```
data/templates/
  ├── _template_dumpster_rental.json
  ├── _template_plumber.json
  ├── _template_dentist.json
  └── _template_lawyer.json
```

### 2. Batch Screenshot Collection
- Use a screenshot tool with annotation features
- Name screenshots consistently: `clientname_section.png`
- Upload all screenshots to one Dropbox folder
- Generate share links for all at once

### 3. Standard Analysis Frameworks
Create reusable analysis text for common situations:
- Low citation completion
- High reviews but low ranking
- Strong DA but low traffic
- Competitive market analysis

### 4. JSON Snippets Library
Keep commonly used text blocks in a separate file:
```json
{
  "citation_warning_85percent": "The 85% citation gap represents...",
  "cro_contact_vs_book": "Contact Us implies additional steps...",
  "review_velocity_importance": "Consistent review generation signals..."
}
```

### 5. Automated Screenshot Naming
When taking screenshots, use this naming pattern:
```
clientname_01_domain_authority.png
clientname_02_citations.png
clientname_03_reputation.png
clientname_04_search_grid.png
clientname_05_competitors.png
```

---

## 🎯 Quality Control Checklist

Before delivering the report, verify:

### Content
- [ ] All client-specific data is accurate
- [ ] No placeholder text remains
- [ ] Company name spelled correctly throughout
- [ ] All metrics are current and verified
- [ ] Recommendations are specific to client

### Visual
- [ ] All screenshots load properly
- [ ] No broken image links
- [ ] Tables display correctly
- [ ] Page breaks are appropriate
- [ ] Print preview looks good

### Technical
- [ ] Links work (if any)
- [ ] Colors display correctly
- [ ] PDF exports cleanly
- [ ] Background graphics show in PDF
- [ ] Font rendering is correct

### Professional
- [ ] Tone is professional and consultative
- [ ] Grammar and spelling checked
- [ ] Data presentation is clear
- [ ] Action items are specific and actionable
- [ ] Report tells a cohesive story

---

## 🔄 Revision Workflow

If client requests changes:

1. **Update JSON file**
   - Make changes to `data/clientname.json`
   - Keep original as `data/clientname_v1.json` (backup)

2. **Regenerate report**
   - Run generator script again
   - Saves new version with current date

3. **Compare versions**
   - Open both HTML files
   - Verify changes are correct

4. **Update PDF**
   - Export new PDF
   - Name clearly: `ClientName_Report_v2.pdf`

---

## 📈 Scaling Your Report Production

### For 1-5 Reports/Month
- Manual process is fine
- Use example report as reference
- Customize each report fully

### For 5-20 Reports/Month
- Create industry-specific templates
- Build a screenshot library
- Standardize data collection process
- Use batch generation for multiple clients

### For 20+ Reports/Month
- Consider automation tools for data collection
- Build a database of reusable content blocks
- Create a web interface for data entry
- Automate screenshot capture where possible

---

## 🆘 Common Issues & Solutions

### Issue: JSON Syntax Errors
**Solution**: Use [jsonlint.com](https://jsonlint.com) to validate before generating

### Issue: Screenshots Not Showing
**Solution**: Verify URL is accessible, ends in `.jpg` or `.png`, and has `raw=1` if using Dropbox

### Issue: PDF Colors Washed Out
**Solution**: Enable "Background graphics" in print settings

### Issue: Page Breaks in Wrong Places
**Solution**: Content sections have `page-break-inside: avoid` - adjust content length

### Issue: Table Formatting Issues
**Solution**: Keep competitor tables to 5-8 rows max for best print results

---

**Ready to streamline your report production?** 

Follow this workflow and you'll create professional reports in a fraction of the time!

