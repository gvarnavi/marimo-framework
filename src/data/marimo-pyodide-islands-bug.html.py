import asyncio

from marimo import MarimoIslandGenerator

generator = MarimoIslandGenerator.from_file("src/data-files/marimo-pyodide-islands-bug.py")
#app = asyncio.run(generator.build())
body = generator.render_body()
print(body)
