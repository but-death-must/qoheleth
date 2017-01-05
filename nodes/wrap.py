# Still sure you've found it all? There's another with this keyword. That one
# has the keyword to the last.
import hashlib
import markdown
import os
import re
import sys


TITLE = re.compile(r'\{\{hash\}\}')
CONTENT = re.compile(r'\{\{content\}\}')
LIST = re.compile(r'\{\{nodelist\}\}')

if len(sys.argv) < 2:
    print("Usage: {} nodes...".format(sys.argv[0]))
    sys.exit()

template_file = "template.html"
out_dir = "html/node"
template_index = "template_index.html"
out_index = "html/index.html"

with open(template_file, 'r') as f:
    template = f.read()

print("Building specified files into {}".format(out_dir))
for infile in sys.argv[1:]:
    node_id = hashlib.sha1(infile).hexdigest()
    print('- Parsing {} into {}'.format(infile, node_id))
    build_dir = os.path.join(out_dir, node_id)
    if not os.path.exists(build_dir):
        print("- - didn't find {}, creating".format(build_dir))
        os.makedirs(build_dir)
    else:
        print("- - found {}, using".format(build_dir))
    with open(infile, 'r') as f:
        contents = f.read()
    md = markdown.markdown(contents, extensions=['markdown.extensions.extra'])
    output = template
    output = re.sub(TITLE, node_id, output)
    output = re.sub(CONTENT, md, output)
    with open('{}/index.html'.format(build_dir), 'w') as f:
        f.write(output)
    print("- {}/index.html written".format(build_dir))

public_nodes = []
for d in os.listdir(out_dir):
    if d == 'index.html':
        continue
    with open('{}/{}/index.html'.format(out_dir, d), 'r') as f:
        text = f.read()
    if not re.search('Private node', text):
        public_nodes.append(d)

print("Building nodelist: {}".format(public_nodes))
list_html = '\n'.join(['<li><a href="/node/{node}">[{node}]</a></li>'.format(node=x) for x in public_nodes])
with open(template_index, 'r') as f:
    template = f.read()
output = re.sub(LIST, list_html, template)
with open(out_index, 'w') as f:
    f.write(output)
print("- Nodelist written; done.")
