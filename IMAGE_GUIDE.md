# 📸 Image Guide for Reports

## 🎯 Recommended Image Dimensions

### Optimal Specs
```
Width:  1100px
Height: 400-600px (550px recommended)
Ratio:  16:9 landscape
Format: JPG or PNG
Size:   < 500KB per image (compressed)
```

### Specific Recommendations by Section

| Section | Image Type | Ideal Size |
|---------|-----------|------------|
| **Domain Authority** | Dashboard screenshot | 1100 × 550px |
| **Citations** | Citation report | 1100 × 500px |
| **Reputation** | Review dashboard | 1100 × 550px |
| **Search Grid** | Local grid heatmap | 1100 × 600px |
| **Competitors** | Comparison table | 1100 × 500px |
| **Website CRO** | Homepage screenshot | 1100 × 700px* |
| **Organic Traffic** | Traffic graph | 1100 × 450px |

*Website screenshots can be slightly taller since they're more visual

## 📏 Why These Dimensions?

### Width: 1100px
- Matches the report container max-width
- Ensures crisp, full-width display
- Scales perfectly for print

### Height: 400-600px
- **400-450px** = More content fits below (good for data-heavy sections)
- **500-550px** = Balanced (recommended for most screenshots)
- **600-700px** = More visual focus (good for website/design screenshots)

### Aspect Ratios
```
16:9  = 1100 × 619px  (standard, recommended)
16:10 = 1100 × 688px  (slightly taller)
2:1   = 1100 × 550px  (wide, good for dashboards)
```

## 🔧 Preparing Your Screenshots

### Step 1: Capture Screenshots
Use any tool:
- **Windows:** Snipping Tool, Snip & Sketch, ShareX
- **Mac:** Cmd+Shift+4, CleanShot X
- **Browser:** Full page screenshot extensions

### Step 2: Crop & Resize
- Crop to show only relevant content
- Remove unnecessary UI elements
- Resize to 1100px width
- Maintain aspect ratio

### Step 3: Optimize File Size
- Use image compression (TinyPNG, Squoosh, etc.)
- Target under 500KB per image
- JPG quality: 80-85%
- PNG: Use compression

### Step 4: Upload & Get URLs

**Option A: Dropbox**
```
1. Upload image to Dropbox
2. Get share link
3. Change dl=0 to raw=1 in URL
4. Use in JSON: "screenshot": "https://...&raw=1"
```

**Option B: Google Drive (requires public access)**
```
1. Upload to Google Drive
2. Set to "Anyone with link can view"
3. Get direct download link
4. Use in JSON
```

**Option C: Image Hosting (Imgur, etc.)**
```
1. Upload to image host
2. Get direct image URL
3. Must end in .jpg or .png
4. Use in JSON
```

**Option D: Local Files (if not sharing)**
```
1. Create images/ folder in project
2. Save images there
3. Use relative path: "screenshot": "../images/da_screenshot.jpg"
```

## 📱 Screenshot Sizes from Different Tools

### SEMrush Dashboard
- Export: 1920px wide (resize to 1100px)
- Focus on key metrics area
- Crop header/footer

### Moz Link Explorer
- Export: 1440px wide (resize to 1100px)
- Capture DA/link metrics section
- Remove unnecessary navigation

### BrightLocal Grid
- Export grid view: 1200-1400px wide
- Resize to 1100px
- Ensure heatmap colors are visible

### Google Business Profile
- Screenshot review section: 1920px
- Resize and crop to 1100 × 550px
- Focus on star rating and review count

## 🎨 Image Quality Tips

### Do's ✅
- Use high resolution source (then resize)
- Capture in daylight mode (better print)
- Include legends and labels
- Ensure text is readable at final size
- Compress after resizing

### Don'ts ❌
- Don't use tiny screenshots (< 800px)
- Don't include sensitive client data in shared examples
- Don't use dark mode (harder to print)
- Don't leave excessive whitespace
- Don't use huge file sizes (> 1MB)

## 🖼️ Example Workflow

### For a Domain Authority Screenshot:

```
1. Open Moz/SEMrush dashboard
2. Navigate to domain overview
3. Take screenshot (full screen)
   → Result: 1920 × 1080px PNG

4. Open in image editor
5. Crop to just the metrics area
   → Result: 1920 × 800px

6. Resize width to 1100px (maintain ratio)
   → Result: 1100 × 458px

7. Compress (TinyPNG or similar)
   → Result: 1100 × 458px, 250KB

8. Upload to Dropbox
9. Get share link with raw=1
10. Add to JSON:
    "screenshot": "https://dropbox.com/.../da.jpg?raw=1"
```

## 📊 File Naming Convention

Keep screenshots organized:

```
clientname_01_domain_authority.jpg
clientname_02_citations.jpg
clientname_03_reputation.jpg
clientname_04_search_grid.jpg
clientname_05_competitors.jpg
clientname_06_website.jpg
clientname_07_traffic.jpg
```

Or by date:
```
2025-10-09_american_dumpster_da.jpg
2025-10-09_american_dumpster_citations.jpg
```

## 🔍 Testing Your Images

Before adding to report:
1. ✅ Open image in browser - does it load quickly?
2. ✅ Is text readable at 1100px width?
3. ✅ File size under 500KB?
4. ✅ URL ends in .jpg or .png?
5. ✅ URL is publicly accessible?

## 💡 Pro Tips

### 1. Batch Processing
Use Photoshop/GIMP actions to:
- Resize multiple images to 1100px width
- Apply compression
- Add subtle drop shadow (optional)

### 2. Consistency
Use the same tool for all screenshots of same type:
- All dashboard shots from same tool
- Same zoom level
- Same UI theme

### 3. Annotations (Optional)
Add arrows or highlights to draw attention:
- Use tools like Skitch, Snagit, or Markup
- Keep annotations minimal
- Use brand colors

### 4. Placeholder Images
While waiting for real screenshots:
- Use placeholder services (placeholder.com)
- Size: 1100 × 550
- Label: "Screenshot: [Section Name]"

## 🆘 Troubleshooting

### Image Too Large in PDF
- Reduce height to 400-450px
- Compress file size more
- Check if browser zoom is affecting it

### Image Blurry
- Source was too small
- Use 2x resolution then scale (2200 × 1100, resize to 1100)
- Save as PNG instead of JPG

### Image Not Loading
- Check URL is public
- Verify URL ends in image extension
- Test URL in incognito browser tab
- Check Dropbox has raw=1 parameter

### Colors Look Different in PDF
- Save in RGB color space (not CMYK)
- Use JPG quality 85% minimum
- Enable "Background graphics" when printing

---

## 📏 Quick Reference Card

```
┌─────────────────────────────────────────┐
│  IDEAL IMAGE SPECS FOR REPORTS         │
├─────────────────────────────────────────┤
│  Width:    1100px                       │
│  Height:   400-600px                    │
│  Format:   JPG (80-85%) or PNG          │
│  Size:     < 500KB                      │
│  Ratio:    16:9 landscape               │
│  Mode:     RGB (not CMYK)               │
└─────────────────────────────────────────┘
```

---

## ✅ Checklist Before Adding Image to JSON

- [ ] Image is 1100px wide (or proportional)
- [ ] Height is 400-600px
- [ ] File size under 500KB
- [ ] Uploaded to public location
- [ ] URL tested in browser
- [ ] URL ends in .jpg or .png
- [ ] Text is readable
- [ ] Colors look good
- [ ] No sensitive data visible

---

**Ready to add images?** Just update the `screenshot` fields in your JSON files with the URLs!

```json
{
  "domain_authority": {
    "screenshot": "https://www.dropbox.com/scl/fi/xxx/image.jpg?raw=1",
    ...
  }
}
```

