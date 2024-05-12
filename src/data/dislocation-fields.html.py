import asyncio

from bs4 import BeautifulSoup
from marimo import MarimoIslandGenerator
from marimo._server.file_router import AppFileRouter
from marimo._utils.marimo_path import MarimoPath

path = MarimoPath("src/data-files/dislocation-fields.py")
file_router = AppFileRouter.from_filename(path)
file_key = file_router.get_unique_file_key()
assert file_key is not None
file_manager = file_router.get_file_manager(file_key)


async def return_marimo_islands(file_manager):
    """async wrapper"""
    stubs = []
    generator = MarimoIslandGenerator()
    for cell_data in file_manager.app.cell_manager.cell_data():
        stubs.append(generator.add_code(cell_data.code))

    await generator.build()
    rendered_stubs = [stub.render() for stub in stubs]
    body = "\n".join(rendered_stubs)
    return body.strip()


body = asyncio.run(return_marimo_islands(file_manager))
soup = BeautifulSoup(body, features="html.parser")
print(soup)
