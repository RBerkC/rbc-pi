from typing import (
    Hashable,
    Mapping,
    Sequence,
)

from pandas._typing import FilePathOrBuffer

class CSVFormatter:
    obj = ...
    sep = ...
    na_rep = ...
    float_format = ...
    decimal = ...
    header = ...
    index = ...
    index_label = ...
    mode = ...
    encoding = ...
    compression = ...
    quoting = ...
    quotechar = ...
    doublequote = ...
    escapechar = ...
    line_terminator = ...
    date_format = ...
    has_mi_columns = ...
    cols = ...
    blocks = ...
    data = ...
    chunksize = ...
    data_index = ...
    nlevels = ...
    def __init__(
        self,
        obj,
        path_or_buf: FilePathOrBuffer[str] | None = ...,
        sep: str = ...,
        na_rep: str = ...,
        float_format: str | None = ...,
        cols=...,
        header: bool | Sequence[Hashable] = ...,
        index: bool = ...,
        index_label: bool | Hashable | Sequence[Hashable] | None = ...,
        mode: str = ...,
        encoding: str | None = ...,
        compression: str | Mapping[str, str] | None = ...,
        quoting: int | None = ...,
        line_terminator=...,
        chunksize: int | None = ...,
        quotechar=...,
        date_format: str | None = ...,
        doublequote: bool = ...,
        escapechar: str | None = ...,
        decimal=...,
    ) -> None: ...
    writer = ...
    def save(self) -> None: ...