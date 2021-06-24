# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.dataflow_v1beta3.services.messages_v1_beta3 import pagers
from google.dataflow_v1beta3.types import messages
from .transports.base import MessagesV1Beta3Transport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import MessagesV1Beta3GrpcAsyncIOTransport
from .client import MessagesV1Beta3Client


class MessagesV1Beta3AsyncClient:
    """The Dataflow Messages API is used for monitoring the progress
    of Dataflow jobs.
    """

    _client: MessagesV1Beta3Client

    DEFAULT_ENDPOINT = MessagesV1Beta3Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = MessagesV1Beta3Client.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        MessagesV1Beta3Client.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        MessagesV1Beta3Client.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(MessagesV1Beta3Client.common_folder_path)
    parse_common_folder_path = staticmethod(
        MessagesV1Beta3Client.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        MessagesV1Beta3Client.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        MessagesV1Beta3Client.parse_common_organization_path
    )
    common_project_path = staticmethod(MessagesV1Beta3Client.common_project_path)
    parse_common_project_path = staticmethod(
        MessagesV1Beta3Client.parse_common_project_path
    )
    common_location_path = staticmethod(MessagesV1Beta3Client.common_location_path)
    parse_common_location_path = staticmethod(
        MessagesV1Beta3Client.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            MessagesV1Beta3AsyncClient: The constructed client.
        """
        return MessagesV1Beta3Client.from_service_account_info.__func__(MessagesV1Beta3AsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            MessagesV1Beta3AsyncClient: The constructed client.
        """
        return MessagesV1Beta3Client.from_service_account_file.__func__(MessagesV1Beta3AsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> MessagesV1Beta3Transport:
        """Returns the transport used by the client instance.

        Returns:
            MessagesV1Beta3Transport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(MessagesV1Beta3Client).get_transport_class, type(MessagesV1Beta3Client)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, MessagesV1Beta3Transport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the messages v1 beta3 client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.MessagesV1Beta3Transport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = MessagesV1Beta3Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_job_messages(
        self,
        request: messages.ListJobMessagesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListJobMessagesAsyncPager:
        r"""Request the job status.

        To request the status of a job, we recommend using
        ``projects.locations.jobs.messages.list`` with a [regional
        endpoint]
        (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints).
        Using ``projects.jobs.messages.list`` is not recommended, as you
        can only request the status of jobs that are running in
        ``us-central1``.

        Args:
            request (:class:`google.dataflow_v1beta3.types.ListJobMessagesRequest`):
                The request object. Request to list job messages.
                Up to max_results messages will be returned in the time
                range specified starting with the oldest messages first.
                If no time range is specified the results with start
                with the oldest message.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.dataflow_v1beta3.services.messages_v1_beta3.pagers.ListJobMessagesAsyncPager:
                Response to a request to list job
                messages.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = messages.ListJobMessagesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_job_messages,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListJobMessagesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-dataflow",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("MessagesV1Beta3AsyncClient",)
