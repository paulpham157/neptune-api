#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum


class AttributeTypeDTO(str, Enum):
    BOOL = "bool"
    COMPLEX = "complex"
    DATETIME = "datetime"
    EXPERIMENTSTATE = "experimentState"
    FILEREF = "fileRef"
    FILEREFSERIES = "fileRefSeries"
    FLOAT = "float"
    FLOATSERIES = "floatSeries"
    GITREF = "gitRef"
    HISTOGRAMSERIES = "histogramSeries"
    INT = "int"
    STRING = "string"
    STRINGSERIES = "stringSeries"
    STRINGSET = "stringSet"

    def __str__(self) -> str:
        return str(self.value)
