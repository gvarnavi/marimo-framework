import asyncio

from bs4 import BeautifulSoup
from marimo._server.export import run_app_then_export_as_reactive_html
from marimo._utils.marimo_path import MarimoPath

path = MarimoPath("src/data-files/dislocation-fields.py")
html, _ = asyncio.run(run_app_then_export_as_reactive_html(path, include_code=False))

soup = BeautifulSoup(html, features="html.parser")
body = soup.body.decode_contents().strip()
print(body)
