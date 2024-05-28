---
title: Marimo Islands
toc: false
theme: [air, alt, wide]
---

<script type="module" src="https://cdn.jsdelivr.net/npm/@marimo-team/islands@0.6.2/dist/main.js"></script>
<link
    href="https://cdn.jsdelivr.net/npm/@marimo-team/islands@0.6.2/dist/style.css"
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

```js
import { showCode } from "./components/showCode.js";
```

```js
const marimo_html = FileAttachment("data/dislocation-fields.html").html();
```

```js
let marimo_code_div = showCode(
  FileAttachment("data-files/dislocation-fields.py"),
  { open: false },
);
```

<div class="grid grid-cols-2" style="grid-auto-rows: auto;">
  <div class="card">

# Reactive Python Notebook

Marimo is a reactive Python notebook, with suppport for Pyodide kernels running natively in the browser.
Using the new [Marimo islands feature](https://docs.marimo.io/guides/wasm.html#islands), and [Framework's data loaders](https://observablehq.com/framework/loaders) we can generate custom html tags at build time, which embed reactive python functionality using the Marimo frontend.

DOM Elements look like so:

```
<marimo-island data-app-id="main">
  <marimo-cell-output>
    <div> Hello, world! </div>
  </marimo-cell-output>
  <marimo-cell-code>
    encoded(print("Hello, world!"))
  </marimo-cell-code>
</marimo-island>
```

and the marimo notebook for the example on the right is:

${marimo_code_div}

  </div>
  <div class="card">
    <div id="marimo-island"> ${marimo_html.body} </div>
  </div>
</div>

<style type="text/css">

  #marimo-island img {
    max-width: 100%;
}

</style>
