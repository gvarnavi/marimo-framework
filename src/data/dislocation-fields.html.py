import asyncio

from marimo import MarimoIslandGenerator

generator = MarimoIslandGenerator.from_file("src/data-files/dislocation-fields.py")
app = asyncio.run(generator.build())
body = generator.render_body()
print(body)
