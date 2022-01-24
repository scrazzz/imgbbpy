"""
The MIT License (MIT)

Copyright (c) 2021-2022 scrazzz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import dataclasses

@dataclasses.dataclass
class Image:
    """Represents an Image.
 
    This is returned from `Client.upload`.

    Attributes
    ----------
    id: str
        The ID of the image.
    filename: str
        The filename of the image.
    url: str
        The URL of the image.
    size: int
        The size of the image in bytes.
    expiration: int
        The time left (in seconds) for the image to expire.
    mime: str
        The mime type of the image.
    extension: str
        The extension of the image.
    delete_url: str
        The delete URL to delete the image.
    """

    id: str
    filename: str
    url: str
    size: int
    expiration: int
    mime: str
    extension: str
    delete_url: str
