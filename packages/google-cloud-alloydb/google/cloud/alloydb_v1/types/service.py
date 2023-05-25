# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.alloydb_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.alloydb.v1",
    manifest={
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "DeleteClusterRequest",
        "RestoreClusterRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "CreateInstanceRequests",
        "BatchCreateInstancesRequest",
        "BatchCreateInstancesResponse",
        "BatchCreateInstancesMetadata",
        "BatchCreateInstanceStatus",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "FailoverInstanceRequest",
        "RestartInstanceRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "CreateBackupRequest",
        "UpdateBackupRequest",
        "DeleteBackupRequest",
        "ListSupportedDatabaseFlagsRequest",
        "ListSupportedDatabaseFlagsResponse",
        "OperationMetadata",
    },
)


class ListClustersRequest(proto.Message):
    r"""Message for requesting list of Clusters

    Attributes:
        parent (str):
            Required. The name of the parent resource. For the required
            format, see the comment on the Cluster.name field.
            Additionally, you can perform an aggregated list operation
            by specifying a value with the following format:

            -  projects/{project}/locations/-
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListClustersResponse(proto.Message):
    r"""Message for response to listing Clusters

    Attributes:
        clusters (MutableSequence[google.cloud.alloydb_v1.types.Cluster]):
            The list of Cluster
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence[resources.Cluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Cluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClusterRequest(proto.Message):
    r"""Message for getting a Cluster

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Cluster.name field.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClusterRequest(proto.Message):
    r"""Message for creating a Cluster

    Attributes:
        parent (str):
            Required. The name of the parent resource.
            For the required format, see the comment on the
            Cluster.name field.
        cluster_id (str):
            Required. ID of the requesting object.
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            create request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateClusterRequest(proto.Message):
    r"""Message for updating a Cluster

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Cluster resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            update request.
        allow_missing (bool):
            Optional. If set to true, update succeeds even if cluster is
            not found. In that case, a new cluster is created and
            ``update_mask`` is ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteClusterRequest(proto.Message):
    r"""Message for deleting a Cluster

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Cluster.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        etag (str):
            Optional. The current etag of the Cluster.
            If an etag is provided and does not match the
            current etag of the Cluster, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            delete.
        force (bool):
            Optional. Whether to cascade delete child
            instances for given cluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class RestoreClusterRequest(proto.Message):
    r"""Message for restoring a Cluster from a backup or another
    cluster at a given point in time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_source (google.cloud.alloydb_v1.types.BackupSource):
            Backup source.

            This field is a member of `oneof`_ ``source``.
        parent (str):
            Required. The name of the parent resource.
            For the required format, see the comment on the
            Cluster.name field.
        cluster_id (str):
            Required. ID of the requesting object.
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            import request.
    """

    backup_source: resources.BackupSource = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message=resources.BackupSource,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListInstancesRequest(proto.Message):
    r"""Message for requesting list of Instances

    Attributes:
        parent (str):
            Required. The name of the parent resource. For the required
            format, see the comment on the Instance.name field.
            Additionally, you can perform an aggregated list operation
            by specifying a value with one of the following formats:

            -  projects/{project}/locations/-/clusters/-
            -  projects/{project}/locations/{region}/clusters/-
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInstancesResponse(proto.Message):
    r"""Message for response to listing Instances

    Attributes:
        instances (MutableSequence[google.cloud.alloydb_v1.types.Instance]):
            The list of Instance
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence[resources.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Instance,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Message for getting a Instance

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        view (google.cloud.alloydb_v1.types.InstanceView):
            The view of the instance to return.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: resources.InstanceView = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.InstanceView,
    )


class CreateInstanceRequest(proto.Message):
    r"""Message for creating a Instance

    Attributes:
        parent (str):
            Required. The name of the parent resource.
            For the required format, see the comment on the
            Instance.name field.
        instance_id (str):
            Required. ID of the requesting object.
        instance (google.cloud.alloydb_v1.types.Instance):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            create request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: resources.Instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Instance,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class CreateInstanceRequests(proto.Message):
    r"""See usage below for notes.

    Attributes:
        create_instance_requests (MutableSequence[google.cloud.alloydb_v1.types.CreateInstanceRequest]):
            Required. Primary and read replica instances
            to be created. This list should not be empty.
    """

    create_instance_requests: MutableSequence[
        "CreateInstanceRequest"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CreateInstanceRequest",
    )


class BatchCreateInstancesRequest(proto.Message):
    r"""Message for creating a batch of instances under the specified
    cluster.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        requests (google.cloud.alloydb_v1.types.CreateInstanceRequests):
            Required. Resources being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: "CreateInstanceRequests" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CreateInstanceRequests",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchCreateInstancesResponse(proto.Message):
    r"""Message for creating batches of instances in a cluster.

    Attributes:
        instances (MutableSequence[google.cloud.alloydb_v1.types.Instance]):
            Created instances.
    """

    instances: MutableSequence[resources.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Instance,
    )


class BatchCreateInstancesMetadata(proto.Message):
    r"""Message for metadata that is specific to BatchCreateInstances
    API.

    Attributes:
        instance_targets (MutableSequence[str]):
            The instances being created in the API call.
            Each string in this list is the server defined
            resource path for target instances in the
            request and for the format of each string, see
            the comment on the Instance.name field.
        instance_statuses (MutableMapping[str, google.cloud.alloydb_v1.types.BatchCreateInstanceStatus]):
            A map representing state of the instances involved in the
            BatchCreateInstances operation during the operation
            execution. The instance state will be in STATE_UNSPECIFIED
            state if the instance has not yet been picked up for
            processing. The key of the map is the name of the instance
            resource. For the format, see the comment on the
            Instance.name field.
    """

    instance_targets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    instance_statuses: MutableMapping[
        str, "BatchCreateInstanceStatus"
    ] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="BatchCreateInstanceStatus",
    )


class BatchCreateInstanceStatus(proto.Message):
    r"""Message for current status of an instance in the
    BatchCreateInstances operation. For example, lets say a
    BatchCreateInstances workflow has 4 instances, Instance1 through
    Instance4. Lets also assume that 2 instances succeeded but the third
    failed to create and the 4th was never picked up for creation
    because of failure of the previous one. Then, resulting states would
    look something like:

    1. Instance1 = ROLLED_BACK
    2. Instance2 = ROLLED_BACK
    3. Instance3 = FAILED
    4. Instance4 = FAILED However, while the operation is running, the
       instance might be in other states including PENDING_CREATE,
       ACTIVE, DELETING and CREATING. The states / do not get further
       updated once the operation is done.

    Attributes:
        state (google.cloud.alloydb_v1.types.BatchCreateInstanceStatus.State):
            The current state of an instance involved in the batch
            create operation. Once the operation is complete, the final
            state of the instances in the LRO can be one of:

            1. ACTIVE, indicating that instances were created
               successfully
            2. FAILED, indicating that a particular instance failed
               creation
            3. ROLLED_BACK indicating that although the instance was
               created successfully, it had to be rolled back and
               deleted due to failure in other steps of the workflow.
        error_msg (str):
            DEPRECATED - Use the error field instead.
            Error, if any error occurred and is available,
            during instance creation.
        error (google.rpc.status_pb2.Status):
            The RPC status of the instance creation
            operation. This field will be present if an
            error happened during the instance creation.
        type_ (google.cloud.alloydb_v1.types.Instance.InstanceType):

    """

    class State(proto.Enum):
        r"""State contains all valid instance states for the
        BatchCreateInstances operation. This is mainly used for status
        reporting through the LRO metadata.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the instance is unknown.
            PENDING_CREATE (1):
                Instance is pending creation and has not yet
                been picked up for processsing in the backend.
            READY (2):
                The instance is active and running.
            CREATING (3):
                The instance is being created.
            DELETING (4):
                The instance is being deleted.
            FAILED (5):
                The creation of the instance failed or a
                fatal error occurred during an operation on the
                instance or a batch of instances.
            ROLLED_BACK (6):
                The instance was created successfully, but
                was rolled back and deleted due to some other
                failure during BatchCreateInstances operation.
        """
        STATE_UNSPECIFIED = 0
        PENDING_CREATE = 1
        READY = 2
        CREATING = 3
        DELETING = 4
        FAILED = 5
        ROLLED_BACK = 6

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    error_msg: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )
    type_: resources.Instance.InstanceType = proto.Field(
        proto.ENUM,
        number=3,
        enum=resources.Instance.InstanceType,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Message for updating a Instance

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Instance resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        instance (google.cloud.alloydb_v1.types.Instance):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            update request.
        allow_missing (bool):
            Optional. If set to true, update succeeds even if instance
            is not found. In that case, a new instance is created and
            ``update_mask`` is ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: resources.Instance = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Instance,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Message for deleting a Instance

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        etag (str):
            Optional. The current etag of the Instance.
            If an etag is provided and does not match the
            current etag of the Instance, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class FailoverInstanceRequest(proto.Message):
    r"""Message for triggering failover on an Instance

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            failover.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class RestartInstanceRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request validation
            (e.g. permission checks and any other type of
            validation), but do not actually execute the
            restart.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListBackupsRequest(proto.Message):
    r"""Message for requesting list of Backups

    Attributes:
        parent (str):
            Required. Parent value for ListBackupsRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBackupsResponse(proto.Message):
    r"""Message for response to listing Backups

    Attributes:
        backups (MutableSequence[google.cloud.alloydb_v1.types.Backup]):
            The list of Backup
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence[resources.Backup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Backup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupRequest(proto.Message):
    r"""Message for getting a Backup

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBackupRequest(proto.Message):
    r"""Message for creating a Backup

    Attributes:
        parent (str):
            Required. Value for parent.
        backup_id (str):
            Required. ID of the requesting object.
        backup (google.cloud.alloydb_v1.types.Backup):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup: resources.Backup = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Backup,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateBackupRequest(proto.Message):
    r"""Message for updating a Backup

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Backup resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        backup (google.cloud.alloydb_v1.types.Backup):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
        allow_missing (bool):
            Optional. If set to true, update succeeds even if instance
            is not found. In that case, a new backup is created and
            ``update_mask`` is ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup: resources.Backup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Backup,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteBackupRequest(proto.Message):
    r"""Message for deleting a Backup

    Attributes:
        name (str):
            Required. Name of the resource. For the
            required format, see the comment on the
            Backup.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
        etag (str):
            Optional. The current etag of the Backup.
            If an etag is provided and does not match the
            current etag of the Backup, deletion will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSupportedDatabaseFlagsRequest(proto.Message):
    r"""Message for listing the information about the supported
    Database flags.

    Attributes:
        parent (str):
            Required. The name of the parent resource. The required
            format is:

            -  projects/{project}/locations/{location}

            Regardless of the parent specified here, as long it is
            contains a valid project and location, the service will
            return a static list of supported flags resources. Note that
            we do not yet support region-specific flags.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
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


class ListSupportedDatabaseFlagsResponse(proto.Message):
    r"""Message for response to listing SupportedDatabaseFlags.

    Attributes:
        supported_database_flags (MutableSequence[google.cloud.alloydb_v1.types.SupportedDatabaseFlag]):
            The list of SupportedDatabaseFlags.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    supported_database_flags: MutableSequence[
        resources.SupportedDatabaseFlag
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.SupportedDatabaseFlag,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        batch_create_instances_metadata (google.cloud.alloydb_v1.types.BatchCreateInstancesMetadata):
            Output only. BatchCreateInstances related
            metadata.

            This field is a member of `oneof`_ ``request_specific``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    batch_create_instances_metadata: "BatchCreateInstancesMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="request_specific",
        message="BatchCreateInstancesMetadata",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
