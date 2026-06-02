import sys
import os
import markdown
import json
from datetime import datetime

# Helper function to get the date with ordinal suffixes (1st, 2nd, 3rd, etc.)
def get_ordinal_date():
    today = datetime.now()
    day = today.day
    if 11 <= (day % 100) <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    
    return f"{day}{suffix} {today.strftime('%B %Y')}"

# 1. Gather inputs interactively
print("--- Blog Post Generator ---")
md_filename = input("Name of markdown file (e.g., filename.md): ").strip()
category = input("Blog category (games, books, shows, movies, thoughts): ").strip().lower()
entry_title = input("Blog title: ").strip()
cover_image = input("Blog cover image (path or URL): ").strip()
summary = input("One line summary: ").strip()

# Ensure the markdown file has the correct extension
if not md_filename.endswith(".md"):
    md_filename += ".md"

# 2. Set up paths
md_file_path = os.path.join("markdown", md_filename)
base_filename = os.path.splitext(md_filename)[0]
output_filename = os.path.join(category, "reviews", f"{base_filename}.html")
json_path = os.path.join(category, "metadata.json")

# 3. Check if the provided markdown file actually exists
if not os.path.isfile(md_file_path):
    print(f"\nError: The file '{md_file_path}' does not exist.")
    print("Make sure it is inside the 'markdown' folder in this directory.")
    sys.exit(1)

# 4. Read the markdown content from the file
with open(md_file_path, "r", encoding="utf-8") as file:
    md_text = file.read()

# 5. Convert the markdown string to HTML
html_content = markdown.markdown(md_text)

# 6. Define the HTML template
html_output = f"""<!DOCTYPE html>
<html>
  <head>
    <title>{entry_title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../index.css">
  </head>
  <body>
      <ul class="navbar">
        <div class="home">
          <li class="navbar-item"><a href="../../index.html">Home</a></li>
        </div>
        <div class="links">
          <li class="navbar-item"><a href="javascript:history.back()">Back to Hub</a></li>
        </div>
      </ul>
    <div class="content-block">
      {html_content}
    </div>
  </body>
</html>"""

# 7. Ensure output directory exists before writing HTML
output_dir = os.path.dirname(output_filename)
os.makedirs(output_dir, exist_ok=True)

# Write the HTML file
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(html_output)

print(f"\n[+] Successfully saved HTML to: {output_filename}")

# 8. Handle the JSON metadata
current_date_str = get_ordinal_date()

# Define the new entry
new_metadata = {
    "Title": entry_title,
    "Last update": current_date_str,
    "Summary": summary,
    "cover_url": cover_image,
    "url": f"reviews/{base_filename}.html" # Added so you can easily link to the generated page
}

# Load existing JSON data if the file exists
metadata_list = []
if os.path.exists(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            metadata_list = json.load(json_file)
    except json.JSONDecodeError:
        print(f"[-] Warning: {json_path} was empty or corrupted. Starting fresh.")

# Append the new entry
metadata_list.append(new_metadata)

# Write the updated list back to the JSON file
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(metadata_list, json_file, indent=4)

print(f"[+] Successfully appended metadata to: {json_path}")
print("Done!")