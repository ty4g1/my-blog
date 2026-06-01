# My Blog

This project is a static site generator for my personal blog. It uses a Python script (`compiler.py`) to convert Markdown files into styled HTML pages and organizes them into different categories like Books, Games, Movies, Shows, and Random Thoughts.

## How to Create a New Blog Entry

Follow these three simple steps to publish a new post:

### 1. Write the Blog Post
Create a new Markdown file containing your post and place it in the `markdown/` directory. 
For example: `markdown/my-new-post.md`

### 2. Run the Compiler
Use the `compiler.py` script to convert your Markdown file into an HTML file and place it in the correct category directory (e.g., `books/`, `games/`, `movies/`, `shows/`, or `thoughts/`).

Run the following command from the root of the project:
```bash
python3 compiler.py markdown/<markdown_filename.md> <category>/reviews/<output_filename.html> "Entry Title"
```

**Example:**
```bash
python3 compiler.py markdown/my-new-post.md books/reviews/my-new-post.html "My Review of The Great Gatsby"
```
*Note: Make sure the output filename includes the category directory (like `books/`) so the generated file goes to the right place.*

### 3. Update the Index
After running the script, it will successfully generate the HTML file and print an HTML snippet to your terminal. 

It will look something like this:
```html
Successfully saved to books/my-new-post.html!

Copy and paste this entry into books/index.html:
------------------------------------------------
<div class="blog-entry">
    <a href="reviews/my-new-post.html">My Review of The Great Gatsby</a>
    <p>Last update: 2nd June 2026</p>
</div>
------------------------------------------------
```

Simply **copy the provided snippet** and paste it into the `index.html` of the corresponding category (in this example, `books/index.html`) so visitors can find your new post!
