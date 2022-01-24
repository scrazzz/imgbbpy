# imgbbpy
An Asynchronous and Synchronous API Wrapper for the Imgbb API.

## Installation
Install imgbbpy via `pip`.

```sh
pip install imgbbpy
```
imgbbpy requires Python 3.7+

## Quickstart
Asynchronous usage:
```py
import asyncio
from imgbbpy.aio import Client

async def main():
    client = Client('API KEY')
    image = await client.upload(file='path/to/image.jpeg')
    print(image.url)

    await client.close()

asyncio.get_event_loop().run_until_complete(main())
```

Synchronous usage:
```py
from imgbbpy import Client

client = Client('API KEY')
image = client.upload(file='path/to/image.png')
print(image.url)
```

You can get an API Key from https://api.imgbb.com.

## Documentation
Documentation can be found in the `documentation.md` file.

## License
MIT, see LICENSE for more details.
