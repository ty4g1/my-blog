# My Blog

This project is a static site generator for my personal blog. It uses Python scripts to convert Markdown files into styled HTML pages and organizes them into different categories like Books, Games, Movies, Shows, and Random Thoughts.

The live site is hosted at: [atharvatyagi.site](https://atharvatyagi.site)

## How to Create a New Blog Entry

Follow these three simple steps to publish a new post:

### 1. Write the Blog Post
Create a new Markdown file containing your post and place it in the `markdown/` directory. 
For example: `markdown/my-new-post.md`

### 2. Publish the Post
Run the interactive publish script to compile your Markdown file into an HTML review page and automatically update the site index pages.

Run the following command from the root of the project:
```bash
./scripts/publish.sh
```
*(Alternatively, you can run `bash scripts/publish.sh`)*

It will prompt you for:
- Name of markdown file (e.g., `my-new-post.md`)
- Blog category (e.g., `books`, `games`, `shows`, `movies`, `thoughts`)
- Blog title
- Blog cover image (path or URL)
- One line summary

The script will handle compiling the post, adding the necessary metadata, and rebuilding the static category pages so your new post is instantly visible on the site!
