import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()


    clean_text = re.sub(r"<.*?>", "", html)


    lines = clean_text.splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    result = "\n".join(lines)


    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(result)
        delete_html_tags("draft.html")
