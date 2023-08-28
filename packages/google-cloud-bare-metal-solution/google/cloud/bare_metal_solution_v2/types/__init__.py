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
from .baremetalsolution import OperationMetadata, ResetInstanceResponse
from .instance import (
    DetachLunRequest,
    DisableInteractiveSerialConsoleRequest,
    DisableInteractiveSerialConsoleResponse,
    EnableInteractiveSerialConsoleRequest,
    EnableInteractiveSerialConsoleResponse,
    GetInstanceRequest,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    RenameInstanceRequest,
    ResetInstanceRequest,
    ServerNetworkTemplate,
    StartInstanceRequest,
    StartInstanceResponse,
    StopInstanceRequest,
    StopInstanceResponse,
    UpdateInstanceRequest,
)
from .lun import EvictLunRequest, GetLunRequest, ListLunsRequest, ListLunsResponse, Lun
from .network import (
    VRF,
    GetNetworkRequest,
    ListNetworksRequest,
    ListNetworksResponse,
    ListNetworkUsageRequest,
    ListNetworkUsageResponse,
    LogicalInterface,
    Network,
    NetworkAddressReservation,
    NetworkMountPoint,
    NetworkUsage,
    RenameNetworkRequest,
    UpdateNetworkRequest,
)
from .nfs_share import (
    CreateNfsShareRequest,
    DeleteNfsShareRequest,
    GetNfsShareRequest,
    ListNfsSharesRequest,
    ListNfsSharesResponse,
    NfsShare,
    RenameNfsShareRequest,
    UpdateNfsShareRequest,
)
from .osimage import ListOSImagesRequest, ListOSImagesResponse, OSImage
from .provisioning import (
    CreateProvisioningConfigRequest,
    GetProvisioningConfigRequest,
    InstanceConfig,
    InstanceQuota,
    ListProvisioningQuotasRequest,
    ListProvisioningQuotasResponse,
    NetworkConfig,
    ProvisioningConfig,
    ProvisioningQuota,
    SubmitProvisioningConfigRequest,
    SubmitProvisioningConfigResponse,
    UpdateProvisioningConfigRequest,
    VolumeConfig,
)
from .ssh_key import (
    CreateSSHKeyRequest,
    DeleteSSHKeyRequest,
    ListSSHKeysRequest,
    ListSSHKeysResponse,
    SSHKey,
)
from .volume import (
    EvictVolumeRequest,
    GetVolumeRequest,
    ListVolumesRequest,
    ListVolumesResponse,
    RenameVolumeRequest,
    ResizeVolumeRequest,
    UpdateVolumeRequest,
    Volume,
)
from .volume_snapshot import (
    CreateVolumeSnapshotRequest,
    DeleteVolumeSnapshotRequest,
    GetVolumeSnapshotRequest,
    ListVolumeSnapshotsRequest,
    ListVolumeSnapshotsResponse,
    RestoreVolumeSnapshotRequest,
    VolumeSnapshot,
)

__all__ = (
    "OperationMetadata",
    "ResetInstanceResponse",
    "VolumePerformanceTier",
    "WorkloadProfile",
    "DetachLunRequest",
    "DisableInteractiveSerialConsoleRequest",
    "DisableInteractiveSerialConsoleResponse",
    "EnableInteractiveSerialConsoleRequest",
    "EnableInteractiveSerialConsoleResponse",
    "GetInstanceRequest",
    "Instance",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "RenameInstanceRequest",
    "ResetInstanceRequest",
    "ServerNetworkTemplate",
    "StartInstanceRequest",
    "StartInstanceResponse",
    "StopInstanceRequest",
    "StopInstanceResponse",
    "UpdateInstanceRequest",
    "EvictLunRequest",
    "GetLunRequest",
    "ListLunsRequest",
    "ListLunsResponse",
    "Lun",
    "GetNetworkRequest",
    "ListNetworksRequest",
    "ListNetworksResponse",
    "ListNetworkUsageRequest",
    "ListNetworkUsageResponse",
    "LogicalInterface",
    "Network",
    "NetworkAddressReservation",
    "NetworkMountPoint",
    "NetworkUsage",
    "RenameNetworkRequest",
    "UpdateNetworkRequest",
    "VRF",
    "CreateNfsShareRequest",
    "DeleteNfsShareRequest",
    "GetNfsShareRequest",
    "ListNfsSharesRequest",
    "ListNfsSharesResponse",
    "NfsShare",
    "RenameNfsShareRequest",
    "UpdateNfsShareRequest",
    "ListOSImagesRequest",
    "ListOSImagesResponse",
    "OSImage",
    "CreateProvisioningConfigRequest",
    "GetProvisioningConfigRequest",
    "InstanceConfig",
    "InstanceQuota",
    "ListProvisioningQuotasRequest",
    "ListProvisioningQuotasResponse",
    "NetworkConfig",
    "ProvisioningConfig",
    "ProvisioningQuota",
    "SubmitProvisioningConfigRequest",
    "SubmitProvisioningConfigResponse",
    "UpdateProvisioningConfigRequest",
    "VolumeConfig",
    "CreateSSHKeyRequest",
    "DeleteSSHKeyRequest",
    "ListSSHKeysRequest",
    "ListSSHKeysResponse",
    "SSHKey",
    "EvictVolumeRequest",
    "GetVolumeRequest",
    "ListVolumesRequest",
    "ListVolumesResponse",
    "RenameVolumeRequest",
    "ResizeVolumeRequest",
    "UpdateVolumeRequest",
    "Volume",
    "CreateVolumeSnapshotRequest",
    "DeleteVolumeSnapshotRequest",
    "GetVolumeSnapshotRequest",
    "ListVolumeSnapshotsRequest",
    "ListVolumeSnapshotsResponse",
    "RestoreVolumeSnapshotRequest",
    "VolumeSnapshot",
)
