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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.compute_v1.types import compute
from google.cloud.compute_v1.services import zone_operations

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-compute",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class InstanceGroupsTransport(abc.ABC):
    """Abstract transport class for InstanceGroups."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/compute",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    DEFAULT_HOST: str = "compute.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        self._extended_operations_services: Dict[str, Any] = {}

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.add_instances: gapic_v1.method.wrap_method(
                self.add_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.aggregated_list: gapic_v1.method.wrap_method(
                self.aggregated_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete: gapic_v1.method.wrap_method(
                self.delete,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get: gapic_v1.method.wrap_method(
                self.get,
                default_timeout=None,
                client_info=client_info,
            ),
            self.insert: gapic_v1.method.wrap_method(
                self.insert,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list: gapic_v1.method.wrap_method(
                self.list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_instances: gapic_v1.method.wrap_method(
                self.list_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_instances: gapic_v1.method.wrap_method(
                self.remove_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_named_ports: gapic_v1.method.wrap_method(
                self.set_named_ports,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def add_instances(
        self,
    ) -> Callable[
        [compute.AddInstancesInstanceGroupRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def aggregated_list(
        self,
    ) -> Callable[
        [compute.AggregatedListInstanceGroupsRequest],
        Union[
            compute.InstanceGroupAggregatedList,
            Awaitable[compute.InstanceGroupAggregatedList],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete(
        self,
    ) -> Callable[
        [compute.DeleteInstanceGroupRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get(
        self,
    ) -> Callable[
        [compute.GetInstanceGroupRequest],
        Union[compute.InstanceGroup, Awaitable[compute.InstanceGroup]],
    ]:
        raise NotImplementedError()

    @property
    def insert(
        self,
    ) -> Callable[
        [compute.InsertInstanceGroupRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list(
        self,
    ) -> Callable[
        [compute.ListInstanceGroupsRequest],
        Union[compute.InstanceGroupList, Awaitable[compute.InstanceGroupList]],
    ]:
        raise NotImplementedError()

    @property
    def list_instances(
        self,
    ) -> Callable[
        [compute.ListInstancesInstanceGroupsRequest],
        Union[
            compute.InstanceGroupsListInstances,
            Awaitable[compute.InstanceGroupsListInstances],
        ],
    ]:
        raise NotImplementedError()

    @property
    def remove_instances(
        self,
    ) -> Callable[
        [compute.RemoveInstancesInstanceGroupRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_named_ports(
        self,
    ) -> Callable[
        [compute.SetNamedPortsInstanceGroupRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()

    @property
    def _zone_operations_client(self) -> zone_operations.ZoneOperationsClient:
        ex_op_service = self._extended_operations_services.get("zone_operations")
        if not ex_op_service:
            ex_op_service = zone_operations.ZoneOperationsClient(
                credentials=self._credentials,
                transport=self.kind,
            )
            self._extended_operations_services["zone_operations"] = ex_op_service

        return ex_op_service


__all__ = ("InstanceGroupsTransport",)
