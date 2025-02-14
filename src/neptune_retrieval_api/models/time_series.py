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
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_series_lineage import TimeSeriesLineage
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.attributes_holder_identifier import AttributesHolderIdentifier


T = TypeVar("T", bound="TimeSeries")


@_attrs_define
class TimeSeries:
    """
    Attributes:
        attribute (str):
        holder (AttributesHolderIdentifier):
        include_preview (Union[Unset, bool]):
        lineage (Union[Unset, TimeSeriesLineage]):
    """

    attribute: str
    holder: "AttributesHolderIdentifier"
    include_preview: Union[Unset, bool] = UNSET
    lineage: Union[Unset, TimeSeriesLineage] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute = self.attribute

        holder = self.holder.to_dict()

        include_preview = self.include_preview

        lineage: Union[Unset, str] = UNSET
        if not isinstance(self.lineage, Unset):
            lineage = self.lineage.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attribute": attribute,
                "holder": holder,
            }
        )
        if include_preview is not UNSET:
            field_dict["includePreview"] = include_preview
        if lineage is not UNSET:
            field_dict["lineage"] = lineage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attributes_holder_identifier import AttributesHolderIdentifier

        d = src_dict.copy()
        attribute = d.pop("attribute")

        holder = AttributesHolderIdentifier.from_dict(d.pop("holder"))

        include_preview = d.pop("includePreview", UNSET)

        _lineage = d.pop("lineage", UNSET)
        lineage: Union[Unset, TimeSeriesLineage]
        if isinstance(_lineage, Unset):
            lineage = UNSET
        else:
            lineage = TimeSeriesLineage(_lineage)

        time_series = cls(
            attribute=attribute,
            holder=holder,
            include_preview=include_preview,
            lineage=lineage,
        )

        time_series.additional_properties = d
        return time_series

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
