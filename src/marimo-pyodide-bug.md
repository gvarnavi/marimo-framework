---
title: Pyodide Back
toc: false
theme: [air, alt,wide]
---
  
<script type="module" src="https://cdn.jsdelivr.net/npm/@marimo-team/islands@0.5.2/dist/main.js"></script>
<link
    href="https://cdn.jsdelivr.net/npm/@marimo-team/islands@0.5.2/dist/style.css"
    rel="stylesheet"
    crossorigin="anonymous"
/>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link
    rel="preconnect"
    href="https://fonts.gstatic.com"
    crossorigin
/>
<link href="https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;500;700&amp;family=Lora&amp;family=PT+Sans:wght@400;700&amp;display=swap" rel="stylesheet" />
<link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css"
    integrity="sha384-wcIxkf4k558AjM3Yz3BBFQUbk/zgIYC2R0QpeeYb+TwlBVMrlgLqwRjRtGZiK7ww"
    crossorigin="anonymous"
/>

# Marimo Pyodide Bug

Currently, the MarimoIslandGenerator tries to build the app before producing the rendered HTML stubs. This has a number of consequences:
- A marimo island like the one below, which tries to import a package with micropip that is not locally-installed will pre-render with errors until pyodide gets initialized
```python
# imports
import marimo as mo
import sys

if "pyodide" in sys.modules:
  import micropip
  await micropip.install('cowsay') 

import cowsay
cowsay.get_output_string('cow', 'Hello, Marimo!')
```

```js
const marimo_html = FileAttachment("data/marimo-pyodide-islands-bug.html").html();
```
```js
marimo_html.body
```

- If the marimo app during export is successful, the HTML output will include all outputs
  - This can be nice, since you get a static view of the app until pyodide initializes
  - Is slightly inconsisent with the rest of marimo (which does not store outputs, and instead only saves the necessary .py files)

- There is no indication to the user when pyodide has initialized and is ready to use
