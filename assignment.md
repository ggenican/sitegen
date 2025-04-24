Create an extract_title(markdown) function.

    It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    If there is no h1 header, raise an exception.
    extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)

Write some unit tests for it.
Create an HTML file called template.html in the root of your project. Use the content found at the bottom of this page.
Create a content/index.md file. This is the main page of the site. Copy the contents from the bottom of this page.
Create a generate_page(from_path, template_path, dest_path) function. It should:

    Print a message like "Generating page from from_path to dest_path using template_path".
    Read the markdown file at from_path and store the contents in a variable.
    Read the template file at template_path and store the contents in a variable.
    Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    Use the extract_title function to grab the title of the page.
    Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.

Update main.py to:

    Delete anything in the public directory.
    Copy all the static files from static to public.
    Generate a page from content/index.md using template.html and write it to public/index.html.

Update your main.sh script to start a simple web server after generating the site. Use the same built-in Python server as before:
