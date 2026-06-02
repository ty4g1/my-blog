import os
import json

def read_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def build_site():
    print("--- Building Static Site ---")
    
    # Load templates
    navbar_tmpl = read_template("templates/navbar.html")
    blog_tmpl = read_template("templates/blog.html")
    home_tmpl = read_template("templates/home.html")
    
    # 1. Build blog page
    print("Building blog feed")
    
    nav_html = navbar_tmpl.replace("{{ base_path }}", "../")
    
    # Load entries
    json_path = os.path.join("blog", "metadata.json")
    entries_html = ""
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                entries = json.load(f)
                # Reverse entries (newest first)
                for entry in reversed(entries):
                    entry_url = entry.get('url', '#')
                    cover_url = entry.get('cover_url', '')
                    category_badge = f'<span class="blog-category" style="font-size: 0.8em; opacity: 0.7; padding-left: 10px;">[{entry.get("category", "post")}]</span>' if entry.get("category") else ""
                    entries_html += f"""
          <a class="content-entry" href="{entry_url}">
            <img src="{cover_url}" alt="{entry.get('Title', '')}" class="entry-pic"/>
            <div class="entry-body">
              <div class="entry-header">
              <h2 class="blog-title">{entry.get('Title', '')}{category_badge}</h2>
              <p class="blog-date">{entry.get('Last update', '')}</p>
              </div>
              <p class="blog-summary">{entry.get('Summary', '')}</p>
            </div>
          </a>"""
            except json.JSONDecodeError:
                print(f"  Warning: {json_path} was corrupted.")
                entries_html = "<p>No entries found yet.</p>"
    else:
        entries_html = "<p>No entries found yet.</p>"

    # Replace placeholders in template
    blog_html = blog_tmpl.replace("{{ title }}", "My Blog")
    blog_html = blog_html.replace("{{ base_path }}", "../")
    blog_html = blog_html.replace("{{ navbar }}", nav_html)
    blog_html = blog_html.replace("{{ content_list }}", entries_html)

    os.makedirs("blog", exist_ok=True)
    with open(os.path.join("blog", "index.html"), "w", encoding="utf-8") as f:
        f.write(blog_html)

    # 2. Build static pages (Home)
    print("Building static pages (Home)")
    
    # Home is in root
    home_nav = navbar_tmpl.replace("{{ base_path }}", "")
    home_out = home_tmpl.replace("{{ navbar }}", home_nav)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(home_out)

    print("--- Build Complete ---")

if __name__ == "__main__":
    build_site()
