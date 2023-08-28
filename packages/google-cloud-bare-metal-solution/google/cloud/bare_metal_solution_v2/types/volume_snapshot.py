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

from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.baremetalsolution.v2",
    manifest={
        "VolumeSnapshot",
        "GetVolumeSnapshotRequest",
        "ListVolumeSnapshotsRequest",
        "ListVolumeSnapshotsResponse",
        "DeleteVolumeSnapshotRequest",
        "CreateVolumeSnapshotRequest",
        "RestoreVolumeSnapshotRequest",
    },
)


class VolumeSnapshot(proto.Message):
    r"""A snapshot of a volume. Only boot volumes can have snapshots.

    Attributes:
        name (str):
            The name of the snapshot.
        id (str):
            Output only. An identifier for the snapshot,
            generated by the backend.
        description (str):
            The description of the snapshot.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            snapshot.
        storage_volume (str):
            Output only. The name of the volume which
            this snapshot belongs to.
        type_ (google.cloud.bare_metal_solution_v2.types.VolumeSnapshot.SnapshotType):
            Output only. The type of the snapshot which
            indicates whether it was scheduled or
            manual/ad-hoc.
    """

    class SnapshotType(proto.Enum):
        r"""Represents the type of a snapshot.

        Values:
            SNAPSHOT_TYPE_UNSPECIFIED (0):
                Type is not specified.
            AD_HOC (1):
                Snapshot was taken manually by user.
            SCHEDULED (2):
                Snapshot was taken automatically as a part of
                a snapshot schedule.
        """
        SNAPSHOT_TYPE_UNSPECIFIED = 0
        AD_HOC = 1
        SCHEDULED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    storage_volume: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: SnapshotType = proto.Field(
        proto.ENUM,
        number=7,
        enum=SnapshotType,
    )


class GetVolumeSnapshotRequest(proto.Message):
    r"""Message for requesting volume snapshot information.

    Attributes:
        name (str):
            Required. The name of the snapshot.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVolumeSnapshotsRequest(proto.Message):
    r"""Message for requesting a list of volume snapshots.

    Attributes:
        parent (str):
            Required. Parent value for
            ListVolumesRequest.
        page_size (int):
            Requested page size. The server might return
            fewer items than requested. If unspecified,
            server will pick an appropriate default.
        page_token (str):
            A token identifying a page of results from
            the server.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListVolumeSnapshotsResponse(proto.Message):
    r"""Response message containing the list of volume snapshots.

    Attributes:
        volume_snapshots (MutableSequence[google.cloud.bare_metal_solution_v2.types.VolumeSnapshot]):
            The list of snapshots.
        next_page_token (str):
            A token identifying a page of results from
            the server.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    volume_snapshots: MutableSequence["VolumeSnapshot"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="VolumeSnapshot",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteVolumeSnapshotRequest(proto.Message):
    r"""Message for deleting named Volume snapshot.

    Attributes:
        name (str):
            Required. The name of the snapshot to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVolumeSnapshotRequest(proto.Message):
    r"""Message for creating a volume snapshot.

    Attributes:
        parent (str):
            Required. The volume to snapshot.
        volume_snapshot (google.cloud.bare_metal_solution_v2.types.VolumeSnapshot):
            Required. The snapshot to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    volume_snapshot: "VolumeSnapshot" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="VolumeSnapshot",
    )


class RestoreVolumeSnapshotRequest(proto.Message):
    r"""Message for restoring a volume snapshot.

    Attributes:
        volume_snapshot (str):
            Required. Name of the snapshot which will be
            used to restore its parent volume.
    """

    volume_snapshot: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
