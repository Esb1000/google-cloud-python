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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.apps.meet_v2beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object]  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore

from google.apps.meet_v2beta.services.conference_records_service import pagers
from google.apps.meet_v2beta.types import resource, service

from .client import ConferenceRecordsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, ConferenceRecordsServiceTransport
from .transports.grpc_asyncio import ConferenceRecordsServiceGrpcAsyncIOTransport


class ConferenceRecordsServiceAsyncClient:
    """REST API for services dealing with conference records."""

    _client: ConferenceRecordsServiceClient

    DEFAULT_ENDPOINT = ConferenceRecordsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ConferenceRecordsServiceClient.DEFAULT_MTLS_ENDPOINT

    conference_record_path = staticmethod(
        ConferenceRecordsServiceClient.conference_record_path
    )
    parse_conference_record_path = staticmethod(
        ConferenceRecordsServiceClient.parse_conference_record_path
    )
    participant_path = staticmethod(ConferenceRecordsServiceClient.participant_path)
    parse_participant_path = staticmethod(
        ConferenceRecordsServiceClient.parse_participant_path
    )
    participant_session_path = staticmethod(
        ConferenceRecordsServiceClient.participant_session_path
    )
    parse_participant_session_path = staticmethod(
        ConferenceRecordsServiceClient.parse_participant_session_path
    )
    recording_path = staticmethod(ConferenceRecordsServiceClient.recording_path)
    parse_recording_path = staticmethod(
        ConferenceRecordsServiceClient.parse_recording_path
    )
    space_path = staticmethod(ConferenceRecordsServiceClient.space_path)
    parse_space_path = staticmethod(ConferenceRecordsServiceClient.parse_space_path)
    transcript_path = staticmethod(ConferenceRecordsServiceClient.transcript_path)
    parse_transcript_path = staticmethod(
        ConferenceRecordsServiceClient.parse_transcript_path
    )
    transcript_entry_path = staticmethod(
        ConferenceRecordsServiceClient.transcript_entry_path
    )
    parse_transcript_entry_path = staticmethod(
        ConferenceRecordsServiceClient.parse_transcript_entry_path
    )
    common_billing_account_path = staticmethod(
        ConferenceRecordsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ConferenceRecordsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ConferenceRecordsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ConferenceRecordsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ConferenceRecordsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ConferenceRecordsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        ConferenceRecordsServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        ConferenceRecordsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        ConferenceRecordsServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        ConferenceRecordsServiceClient.parse_common_location_path
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
            ConferenceRecordsServiceAsyncClient: The constructed client.
        """
        return ConferenceRecordsServiceClient.from_service_account_info.__func__(ConferenceRecordsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            ConferenceRecordsServiceAsyncClient: The constructed client.
        """
        return ConferenceRecordsServiceClient.from_service_account_file.__func__(ConferenceRecordsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ConferenceRecordsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ConferenceRecordsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConferenceRecordsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ConferenceRecordsServiceClient).get_transport_class,
        type(ConferenceRecordsServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, ConferenceRecordsServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conference records service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ConferenceRecordsServiceTransport]): The
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
        self._client = ConferenceRecordsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def get_conference_record(
        self,
        request: Optional[Union[service.GetConferenceRecordRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.ConferenceRecord:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Gets a conference record by conference ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_get_conference_record():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.GetConferenceRecordRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conference_record(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.GetConferenceRecordRequest, dict]]):
                The request object. Request to get a conference record.
            name (:class:`str`):
                Required. Resource name of the
                conference.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.types.ConferenceRecord:
                [Developer Preview](\ https://developers.google.com/workspace/preview).
                   Single instance of a meeting held in a space.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetConferenceRecordRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_conference_record,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_conference_records(
        self,
        request: Optional[Union[service.ListConferenceRecordsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConferenceRecordsAsyncPager:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Lists the conference records by start time and in descending
        order.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_list_conference_records():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.ListConferenceRecordsRequest(
                )

                # Make the request
                page_result = client.list_conference_records(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.ListConferenceRecordsRequest, dict]]):
                The request object. Request to fetch list of conference
                records per user.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.services.conference_records_service.pagers.ListConferenceRecordsAsyncPager:
                Response of ListConferenceRecords
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListConferenceRecordsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_conference_records,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListConferenceRecordsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_participant(
        self,
        request: Optional[Union[service.GetParticipantRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.Participant:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Gets a participant by participant ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_get_participant():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.GetParticipantRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.GetParticipantRequest, dict]]):
                The request object. Request to get a Participant.
            name (:class:`str`):
                Required. Resource name of the
                participant.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.types.Participant:
                [Developer Preview](\ https://developers.google.com/workspace/preview).
                   User who attended or is attending a conference.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetParticipantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_participant,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_participants(
        self,
        request: Optional[Union[service.ListParticipantsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListParticipantsAsyncPager:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Lists the participants in a conference record, by default
        ordered by join time and in descending order. This API supports
        ``fields`` as standard parameters like every other API. However,
        when the ``fields`` request parameter is omitted, this API
        defaults to ``'participants/*, next_page_token'``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_list_participants():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.ListParticipantsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_participants(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.ListParticipantsRequest, dict]]):
                The request object. Request to fetch list of participant
                per conference.
            parent (:class:`str`):
                Required. Format:
                ``conferenceRecords/{conference_record}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.services.conference_records_service.pagers.ListParticipantsAsyncPager:
                Response of ListParticipants method.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListParticipantsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_participants,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListParticipantsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_participant_session(
        self,
        request: Optional[Union[service.GetParticipantSessionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.ParticipantSession:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Gets a participant session by participant session ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_get_participant_session():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.GetParticipantSessionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_participant_session(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.GetParticipantSessionRequest, dict]]):
                The request object. Request to get a participant session.
            name (:class:`str`):
                Required. Resource name of the
                participant.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.types.ParticipantSession:
                [Developer Preview](\ https://developers.google.com/workspace/preview).
                   Refers to each unique join/leave session when a user
                   joins a conference from a device. Note that any time
                   a user joins the conference a new unique ID is
                   assigned. That means if a user joins a space multiple
                   times from the same device, they're assigned
                   different IDs, and are also be treated as different
                   participant sessions.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetParticipantSessionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_participant_session,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_participant_sessions(
        self,
        request: Optional[Union[service.ListParticipantSessionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListParticipantSessionsAsyncPager:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Lists the participant sessions of a participant in a conference
        record, by default ordered by join time and in descending order.
        This API supports ``fields`` as standard parameters like every
        other API. However, when the ``fields`` request parameter is
        omitted this API defaults to
        ``'participantsessions/*, next_page_token'``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_list_participant_sessions():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.ListParticipantSessionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_participant_sessions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.ListParticipantSessionsRequest, dict]]):
                The request object. Request to fetch list of participant
                sessions per conference record per
                participant.
            parent (:class:`str`):
                Required. Format:
                ``conferenceRecords/{conference_record}/participants/{participant}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.services.conference_records_service.pagers.ListParticipantSessionsAsyncPager:
                Response of ListParticipants method.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListParticipantSessionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_participant_sessions,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListParticipantSessionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_recording(
        self,
        request: Optional[Union[service.GetRecordingRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.Recording:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Gets a recording by recording ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_get_recording():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.GetRecordingRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_recording(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.GetRecordingRequest, dict]]):
                The request object. Request message for GetRecording
                method.
            name (:class:`str`):
                Required. Resource name of the
                recording.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.types.Recording:
                [Developer Preview](\ https://developers.google.com/workspace/preview).
                   Metadata about a recording created during a
                   conference.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetRecordingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_recording,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_recordings(
        self,
        request: Optional[Union[service.ListRecordingsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListRecordingsAsyncPager:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Lists the recording resources from the conference record.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_list_recordings():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.ListRecordingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_recordings(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.ListRecordingsRequest, dict]]):
                The request object. Request for ListRecordings method.
            parent (:class:`str`):
                Required. Format:
                ``conferenceRecords/{conference_record}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.services.conference_records_service.pagers.ListRecordingsAsyncPager:
                Response for ListRecordings method.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListRecordingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_recordings,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListRecordingsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_transcript(
        self,
        request: Optional[Union[service.GetTranscriptRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.Transcript:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Gets a transcript by transcript ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_get_transcript():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.GetTranscriptRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_transcript(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.GetTranscriptRequest, dict]]):
                The request object. Request for GetTranscript method.
            name (:class:`str`):
                Required. Resource name of the
                transcript.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.types.Transcript:
                [Developer Preview](\ https://developers.google.com/workspace/preview).
                   Metadata for a transcript generated from a
                   conference. It refers to the ASR (Automatic Speech
                   Recognition) result of user's speech during the
                   conference.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetTranscriptRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_transcript,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_transcripts(
        self,
        request: Optional[Union[service.ListTranscriptsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTranscriptsAsyncPager:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Lists the set of transcripts from the conference record.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_list_transcripts():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.ListTranscriptsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transcripts(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.ListTranscriptsRequest, dict]]):
                The request object. Request for ListTranscripts method.
            parent (:class:`str`):
                Required. Format:
                ``conferenceRecords/{conference_record}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.services.conference_records_service.pagers.ListTranscriptsAsyncPager:
                Response for ListTranscripts method.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListTranscriptsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transcripts,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTranscriptsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_transcript_entry(
        self,
        request: Optional[Union[service.GetTranscriptEntryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.TranscriptEntry:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Gets a ``TranscriptEntry`` resource by entry ID.

        Note: The transcript entries returned by the Google Meet API
        might not match the transcription found in the Google Docs
        transcript file. This can occur when the Google Docs transcript
        file is modified after generation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_get_transcript_entry():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.GetTranscriptEntryRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_transcript_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.GetTranscriptEntryRequest, dict]]):
                The request object. Request for GetTranscriptEntry
                method.
            name (:class:`str`):
                Required. Resource name of the ``TranscriptEntry``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.types.TranscriptEntry:
                [Developer Preview](\ https://developers.google.com/workspace/preview).
                   Single entry for one user’s speech during a
                   transcript session.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetTranscriptEntryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_transcript_entry,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_transcript_entries(
        self,
        request: Optional[Union[service.ListTranscriptEntriesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTranscriptEntriesAsyncPager:
        r"""`Developer
        Preview <https://developers.google.com/workspace/preview>`__.
        Lists the structured transcript entries per transcript. By
        default, ordered by start time and in ascending order.

        Note: The transcript entries returned by the Google Meet API
        might not match the transcription found in the Google Docs
        transcript file. This can occur when the Google Docs transcript
        file is modified after generation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2beta

            async def sample_list_transcript_entries():
                # Create a client
                client = meet_v2beta.ConferenceRecordsServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2beta.ListTranscriptEntriesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transcript_entries(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2beta.types.ListTranscriptEntriesRequest, dict]]):
                The request object. Request for ListTranscriptEntries
                method.
            parent (:class:`str`):
                Required. Format:
                ``conferenceRecords/{conference_record}/transcripts/{transcript}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.apps.meet_v2beta.services.conference_records_service.pagers.ListTranscriptEntriesAsyncPager:
                Response for ListTranscriptEntries
                method
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListTranscriptEntriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transcript_entries,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTranscriptEntriesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "ConferenceRecordsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("ConferenceRecordsServiceAsyncClient",)
