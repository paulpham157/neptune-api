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

from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type_dto import AttributeTypeDTO
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="FileRefAttributeDTO")


@_attrs_define
class FileRefAttributeDTO:
    """
    Attributes:
        attribute_name (str):
        attribute_type (AttributeTypeDTO):
        mime_type (Union[Unset, str]):
        path (Union[Unset, str]):
        size_bytes (Union[Unset, int]):
    """

    attribute_name: str
    attribute_type: AttributeTypeDTO
    mime_type: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    size_bytes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name

        attribute_type = self.attribute_type.value

        mime_type = self.mime_type

        path = self.path

        size_bytes = self.size_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeName": attribute_name,
                "attributeType": attribute_type,
            }
        )
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if path is not UNSET:
            field_dict["path"] = path
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_name = d.pop("attributeName")

        attribute_type = AttributeTypeDTO(d.pop("attributeType"))

        mime_type = d.pop("mimeType", UNSET)

        path = d.pop("path", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        file_ref_attribute_dto = cls(
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            mime_type=mime_type,
            path=path,
            size_bytes=size_bytes,
        )

        file_ref_attribute_dto.additional_properties = d
        return file_ref_attribute_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
