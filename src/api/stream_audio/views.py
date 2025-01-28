import mimetypes
import os
import re
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.views.decorators.http import require_GET

from api.common import status

__all__ = [
    "stream_view",
]


class RangeFileWrapper:
    def __init__(self, filelike, blksize=8192, offset=0, length=None):
        self.filelike = filelike
        self.filelike.seek(offset, os.SEEK_SET)
        self.remaining = length
        self.block_size = blksize

    def close(self):
        if hasattr(self.filelike, "close"):
            self.filelike.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining is None:
            if block := self.filelike.read(self.block_size):
                return block
            raise StopIteration()

        if self.remaining <= 0:
            raise StopIteration()

        block = self.filelike.read(min(self.remaining, self.block_size))
        if not block:
            raise StopIteration()

        self.remaining -= len(block)
        return block


def guess_content_type(filename):
    content_type, _ = mimetypes.guess_type(filename)
    return content_type or "application/octet-stream"


def calculate_range(first_byte, last_byte, size):
    first_byte = int(first_byte) if first_byte else 0
    last_byte = int(last_byte) if last_byte else size - 1
    if last_byte >= size:
        last_byte = size - 1
    length = last_byte - first_byte + 1
    return first_byte, last_byte, length


range_re = re.compile(r"bytes\s*=\s*(\d+)\s*-\s*(\d*)", re.I)


@require_GET
def stream_view(request, filename):
    filename = f"media/tracks/{filename}"
    range_match = range_re.match(request.META.get("HTTP_RANGE", "").strip())
    size = os.path.getsize(filename)
    headers = {
        "Content-type": guess_content_type(filename),
        "Accept-Ranges": "bytes",
    }

    if range_match:
        first_byte, last_byte, length = calculate_range(*range_match.groups(), size)
        data = RangeFileWrapper(open(filename, "rb"), offset=first_byte, length=length)
        status_code = status.HTTP_206_PARTIAL_CONTENT
        headers["Content-Length"] = str(length)
        headers["Content-Range"] = "bytes %s-%s/%s" % (first_byte, last_byte, size)
    else:
        data = FileWrapper(open(filename, "rb"))
        status_code = status.HTTP_200_OK
        headers["Content-Length"] = str(size)

    response = StreamingHttpResponse(data, status=status_code)
    for header, value in headers.items():
        response[header] = value

    return response
