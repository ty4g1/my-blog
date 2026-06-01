import sys
import os
import markdown
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

# 1. Ensure all three arguments are provided
if len(sys.argv) < 4:
    print('Usage: python script.py <path_to_markdown.md> <output_filename.html> "Entry Title"')
    sys.exit(1)

md_file_path = sys.argv[1]
output_filename = sys.argv[2]
entry_title = sys.argv[3]

# Ensure the output filename ends with .html
if not output_filename.endswith(".html"):
    output_filename += ".html"

# 2. Check if the provided markdown file actually exists
if not os.path.isfile(md_file_path):
    print(f"Error: The file '{md_file_path}' does not exist.")
    sys.exit(1)

# 3. Read the markdown content from the file
with open(md_file_path, "r", encoding="utf-8") as file:
    md_text = file.read()

# 4. Convert the markdown string to HTML
html_content = markdown.markdown(md_text)

# 5. Define the HTML template
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
          <li class="navbar-item"><a href="../index.html">Home</a></li>
        </div>
        <div class="links">
          <li class="navbar-item"><a href="../../games/index.html">Game Reviews</a></li>
          <li class="navbar-item"><a href="../../books/index.html">Book Reviews</a></li>
          <li class="navbar-item"><a href="../../shows/index.html">Show Reviews</a></li>
          <li class="navbar-item"><a href="../../movies/index.html">Movie Reviews</a></li>
          <li class="navbar-item"><a href="../../thoughts/index.html">Random Thoughts</a></li>
        </div>
      </ul>
    <div class="content-block">
      {html_content}
    </div>
  </body>
</html>"""

# Ensure the output directory actually exists before writing
output_dir = os.path.dirname(output_filename)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 6. Write the final formatted string to the dynamically named output file
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(html_output)

# 7. Parse the path to generate the correct href and index instructions
# Normalize path separators to forward slashes for consistency
normalized_path = output_filename.replace('\\', '/')
path_parts = normalized_path.split('/')

if len(path_parts) > 1:
    first_dir = path_parts[0]
    href_path = '/'.join(path_parts[1:])
    target_index = f"{first_dir}/index.html"
else:
    href_path = normalized_path
    target_index = "index.html"

# 8. Generate and print the HTML index snippet
current_date_str = get_ordinal_date()

snippet = f"""
<div class="blog-entry">
    <a href="{href_path}">{entry_title}</a>
    <p>Last update: {current_date_str}</p>
</div>
"""

print(f"Successfully saved to {output_filename}!\n")
print(f"Copy and paste this entry into {target_index}:")
print("------------------------------------------------")
print(snippet.strip())
print("------------------------------------------------")