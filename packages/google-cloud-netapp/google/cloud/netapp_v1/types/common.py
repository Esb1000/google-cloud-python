# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "ServiceLevel",
        "EncryptionType",
    },
)


class ServiceLevel(proto.Enum):
    r"""The service levels - Storage Pool, Volumes

    Values:
        SERVICE_LEVEL_UNSPECIFIED (0):
            Unspecified service level.
        PREMIUM (1):
            Premium service level.
        EXTREME (2):
            Extreme service level.
        STANDARD (3):
            Standard (Software offering)
    """
    SERVICE_LEVEL_UNSPECIFIED = 0
    PREMIUM = 1
    EXTREME = 2
    STANDARD = 3


class EncryptionType(proto.Enum):
    r"""Defined the current volume encryption key source.

    Values:
        ENCRYPTION_TYPE_UNSPECIFIED (0):
            The source of encryption key is not
            specified.
        SERVICE_MANAGED (1):
            Google managed encryption key.
        CLOUD_KMS (2):
            Customer managed encryption key, which is
            stored in KMS.
    """
    ENCRYPTION_TYPE_UNSPECIFIED = 0
    SERVICE_MANAGED = 1
    CLOUD_KMS = 2


__all__ = tuple(sorted(__protobuf__.manifest))
