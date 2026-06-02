import os
import json

def read_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def build_site():
    print("--- Building Static Site ---")
    
    # Load templates
    navbar_tmpl = read_template("templates/navbar.html")
    category_tmpl = read_template("templates/category.html")
    home_tmpl = read_template("templates/home.html")
    
    categories = {
        "games": {
            "title": "Game Reviews",
            "header": "<span>Game</span> Reviews",
            "desc": "Here are my collected thoughts on games I've played recently. Might post some initial thoughts and update the reviews as I play further through the game. Plan to cover a variety of game genres now that I can afford to buy more games."
        },
        "books": {
            "title": "Book Reviews",
            "header": "<span>Book</span> Reviews",
            "desc": "Here are my collected thoughts on books I've read recently. The reviews are one books I've finished reading. Generally will focus on books I've read, but might occasionally include some audiobooks as well."
        },
        "shows": {
            "title": "Show Reviews",
            "header": "<span>Show</span> Reviews",
            "desc": "Here are my collected thoughts on shows I've watched recently. Will probably update the reviews as I watch more episodes, or split into multiple reviews. This will likely include a mix of TV shows, web series, and Animes."
        },
        "movies": {
            "title": "Movie Reviews",
            "header": "<span>Movie</span> Reviews",
            "desc": "Here are my collected thoughts on movies I've watched recently. This is probably going to be the least updated/populated section, since I don't get to sit down and watch a whole movie often."
        },
        "thoughts": {
            "title": "Random Thoughts",
            "header": "<span>Random</span> Thoughts",
            "desc": "Here is simply a bunch of random posts into the void, maybe I felt like writing my thoughts on something that happened, or something I thought of. This could be an idea bank, or just a collection of garbage."
        }
    }

    # 1. Build category pages
    for cat, data in categories.items():
        print(f"Building category: {cat}")
        
        # Build navbar for category (1 level deep)
        nav_html = navbar_tmpl.replace("{{ base_path }}", "../")
        
        # Load entries
        json_path = os.path.join(cat, "metadata.json")
        entries_html = ""
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                try:
                    entries = json.load(f)
                    # Reverse entries (newest first)
                    for entry in reversed(entries):
                        entry_url = entry.get('url', '#')
                        cover_url = entry.get('cover_url', '')
                        entries_html += f"""
              <a class="content-entry" href="{entry_url}">
                <img src="{cover_url}" alt="{entry.get('Title', '')}" class="entry-pic"/>
                <div class="entry-body">
                  <div class="entry-header">
                  <h2 class="blog-title">{entry.get('Title', '')}</h2>
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
        cat_html = category_tmpl.replace("{{ title }}", data["title"])
        cat_html = cat_html.replace("{{ base_path }}", "../")
        cat_html = cat_html.replace("{{ navbar }}", nav_html)
        cat_html = cat_html.replace("{{ header }}", data["header"])
        cat_html = cat_html.replace("{{ desc }}", data["desc"])
        cat_html = cat_html.replace("{{ content_list }}", entries_html)

        with open(os.path.join(cat, "index.html"), "w", encoding="utf-8") as f:
            f.write(cat_html)

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
