import marimo

__generated_with = "0.6.1-dev29"
app = marimo.App()


@app.cell
async def __():
    # imports
    import marimo as mo
    import sys

    if "pyodide" in sys.modules:
        import micropip
        await micropip.install('cowsay') 

    import cowsay
    cow_string = cowsay.get_output_string('cow', 'Hello, Marimo!')
    cow_string
    return cow_string, cowsay, micropip, mo, sys


if __name__ == "__main__":
    app.run()
