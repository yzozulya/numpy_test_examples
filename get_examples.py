import os
import urllib.request
from bs4 import BeautifulSoup


def find_header(node):
    sibling = node.previous_sibling
    if sibling:
        return sibling if sibling.name == 'h3' else find_header(sibling)
    else:
        print(node)


def get_examples(parsed_html):
    for item in parsed_html.body.find_all('div', attrs={'class': 'codearea'}):
        name = find_header(item).text
        f = open("general/{0}.py".format(name), "w")
        for line in item.text.split("\n"):
            if line.startswith(">>> ") or line.startswith("... "):
                f.write(line[4:])
                f.write("\n")
        f.close()


def create_files_from_examples(examples, pf_path):
    f = open(pf_path, "w")
    f.write("import numpy as np\n")
    for example in examples:
        for line in example.text.split("\n"):
            if line.startswith(">>> ") or line.startswith("... "):
                f.write(line[4:])
                f.write("\n")
    f.close()
    print("created {0}".format(pf_path))


def get_examples_from_scipydoc():
    parent_dir = "scipy_doc"
    html = urllib.request.urlopen("http://docs.scipy.org/doc/numpy/reference/routines.html")
    parsed_html = BeautifulSoup(html)

    tree = parsed_html.find('div', attrs={'class': 'toctree-wrapper'})
    subtrees = tree.find_all('li', attrs={'class': 'toctree-l1'})

    for tree in subtrees:
        pf_dir = os.path.join(parent_dir, tree.a.attrs['href'])
        if not os.path.exists(pf_dir):
            os.makedirs(pf_dir)

        link = "http://docs.scipy.org/doc/numpy/reference/{0}".format(tree.a.attrs['href'])
        parsed_child = BeautifulSoup(urllib.request.urlopen(link))

        examples = parsed_child.find_all('div', attrs={'class': 'highlight-python'})
        if examples:
            pf_name = "{0}.py".format(parsed_child.find('h1').text[:-1])
            create_files_from_examples(examples, os.path.join(pf_dir, pf_name))
        else:
            sections = parsed_child.find_all('div', attrs={'class': 'section'})
            for section in sections:
                link_table_rows = section.find_all('tr')
                for row in link_table_rows:
                    try:
                        href = row.td.a.attrs['href']
                    except AttributeError:
                        print("Unexpected table raw format: {0}".format(row.text))
                    else:
                        link = "http://docs.scipy.org/doc/numpy/reference/{0}".format(href)
                        parsed_example_page = BeautifulSoup(urllib.request.urlopen(link))
                        examples = parsed_example_page.find_all('div', attrs={'class': 'highlight-python'})

                        pf_name = "{0}.py".format(parsed_example_page.find('h1').text[:-1])
                        create_files_from_examples(examples, os.path.join(pf_dir, pf_name))


get_examples_from_scipydoc()