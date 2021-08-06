from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Iterable,
)

from file_reader.file_readers import BasicFileReader
from hosts_parser import HostsParser
from text_file_reader.reader import (
    AbstractFileReader,
    TextFileReader,
)


@dataclass
class HostsFileReader(BasicFileReader):
    parser: HostsParser = field(default=HostsParser(), init=False)
    file_readers: Iterable[AbstractFileReader] = field(
        default=(TextFileReader(),), init=False
    )
