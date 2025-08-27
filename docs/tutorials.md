
## Simple diagram
```python linenums="1" exec="0" source="above"
--8<-- "examples/simple_rbd.py:5:5,8:"
```

```python exec="on" html="on" workdir="docs/examples"
import pymupdf

doc = pymupdf.open("simple_RBD.pdf")
page = doc[0]

# Convert page to SVG
svg_content = page.get_svg_image()

# Save to file
with open("simple_RBD.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

doc.close()
```

<image width="500" src='examples/simple_RBD.svg'/>


## Example with more functionality

```python linenums="1" exec="0" source="above"
--8<-- "examples/example_rbd.py:5:5,8:"
```

```python exec="on" html="on" workdir="docs/examples"
import pymupdf

doc = pymupdf.open("example_RBD.pdf")
page = doc[0]

# Convert page to SVG
svg_content = page.get_svg_image()

# Save to file
with open("example_RBD.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

doc.close()
```

<image width="1000" src='examples/example_RBD.svg'/>
