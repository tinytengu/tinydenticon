# tinydenticon

Python 3 implementation of Identicon.

Specifically designed to produce the same results as [identicon.js](https://github.com/stewartlord/identicon.js)

## Installation:
### Pip:
```sh
pip3 install tinydenticon
```

## Usage example:
```python
from PIL import Image
from tinydenticon import Identicon


def main():
    text = "tinytengu"
    size = 500
    rounds = 1337

    identicon = Identicon(text.encode(), hash_rounds=rounds, image_side=size)

    image = Image.new("RGB", (size, size))
    image.putdata(identicon.get_pixels())
    image.show()


if __name__ == "__main__":
    main()

```

## License
[GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)