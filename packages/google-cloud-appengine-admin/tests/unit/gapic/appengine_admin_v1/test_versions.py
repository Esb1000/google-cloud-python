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
import os

# try/except added for compatibility with python < 3.8
try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

from collections.abc import Iterable
import json
import math

from google.api_core import (
    future,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    operation,
    operations_v1,
    path_template,
)
from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import operation_async  # type: ignore
import google.auth
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import json_format
from google.protobuf import timestamp_pb2  # type: ignore
import grpc
from grpc.experimental import aio
from proto.marshal.rules import wrappers
from proto.marshal.rules.dates import DurationRule, TimestampRule
import pytest
from requests import PreparedRequest, Request, Response
from requests.sessions import Session

from google.cloud.appengine_admin_v1.services.versions import (
    VersionsAsyncClient,
    VersionsClient,
    pagers,
    transports,
)
from google.cloud.appengine_admin_v1.types import app_yaml, appengine, deploy
from google.cloud.appengine_admin_v1.types import operation as ga_operation
from google.cloud.appengine_admin_v1.types import version


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert VersionsClient._get_default_mtls_endpoint(None) is None
    assert VersionsClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert (
        VersionsClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        VersionsClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        VersionsClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert VersionsClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (VersionsClient, "grpc"),
        (VersionsAsyncClient, "grpc_asyncio"),
        (VersionsClient, "rest"),
    ],
)
def test_versions_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "appengine.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://appengine.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.VersionsGrpcTransport, "grpc"),
        (transports.VersionsGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.VersionsRestTransport, "rest"),
    ],
)
def test_versions_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (VersionsClient, "grpc"),
        (VersionsAsyncClient, "grpc_asyncio"),
        (VersionsClient, "rest"),
    ],
)
def test_versions_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "appengine.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://appengine.googleapis.com"
        )


def test_versions_client_get_transport_class():
    transport = VersionsClient.get_transport_class()
    available_transports = [
        transports.VersionsGrpcTransport,
        transports.VersionsRestTransport,
    ]
    assert transport in available_transports

    transport = VersionsClient.get_transport_class("grpc")
    assert transport == transports.VersionsGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (VersionsClient, transports.VersionsGrpcTransport, "grpc"),
        (VersionsAsyncClient, transports.VersionsGrpcAsyncIOTransport, "grpc_asyncio"),
        (VersionsClient, transports.VersionsRestTransport, "rest"),
    ],
)
@mock.patch.object(
    VersionsClient, "DEFAULT_ENDPOINT", modify_default_endpoint(VersionsClient)
)
@mock.patch.object(
    VersionsAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(VersionsAsyncClient),
)
def test_versions_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(VersionsClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(VersionsClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(
        api_audience="https://language.googleapis.com"
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com",
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (VersionsClient, transports.VersionsGrpcTransport, "grpc", "true"),
        (
            VersionsAsyncClient,
            transports.VersionsGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (VersionsClient, transports.VersionsGrpcTransport, "grpc", "false"),
        (
            VersionsAsyncClient,
            transports.VersionsGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (VersionsClient, transports.VersionsRestTransport, "rest", "true"),
        (VersionsClient, transports.VersionsRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    VersionsClient, "DEFAULT_ENDPOINT", modify_default_endpoint(VersionsClient)
)
@mock.patch.object(
    VersionsAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(VersionsAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_versions_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                        api_audience=None,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [VersionsClient, VersionsAsyncClient])
@mock.patch.object(
    VersionsClient, "DEFAULT_ENDPOINT", modify_default_endpoint(VersionsClient)
)
@mock.patch.object(
    VersionsAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(VersionsAsyncClient),
)
def test_versions_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                (
                    api_endpoint,
                    cert_source,
                ) = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (VersionsClient, transports.VersionsGrpcTransport, "grpc"),
        (VersionsAsyncClient, transports.VersionsGrpcAsyncIOTransport, "grpc_asyncio"),
        (VersionsClient, transports.VersionsRestTransport, "rest"),
    ],
)
def test_versions_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (VersionsClient, transports.VersionsGrpcTransport, "grpc", grpc_helpers),
        (
            VersionsAsyncClient,
            transports.VersionsGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (VersionsClient, transports.VersionsRestTransport, "rest", None),
    ],
)
def test_versions_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


def test_versions_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.appengine_admin_v1.services.versions.transports.VersionsGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = VersionsClient(client_options={"api_endpoint": "squid.clam.whelk"})
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (VersionsClient, transports.VersionsGrpcTransport, "grpc", grpc_helpers),
        (
            VersionsAsyncClient,
            transports.VersionsGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_versions_client_create_channel_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "appengine.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/appengine.admin",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            scopes=None,
            default_host="appengine.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.ListVersionsRequest,
        dict,
    ],
)
def test_list_versions(request_type, transport: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = appengine.ListVersionsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.ListVersionsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListVersionsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_versions_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        client.list_versions()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.ListVersionsRequest()


@pytest.mark.asyncio
async def test_list_versions_async(
    transport: str = "grpc_asyncio", request_type=appengine.ListVersionsRequest
):
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            appengine.ListVersionsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.ListVersionsRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListVersionsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_list_versions_async_from_dict():
    await test_list_versions_async(request_type=dict)


def test_list_versions_field_headers():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.ListVersionsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        call.return_value = appengine.ListVersionsResponse()
        client.list_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_versions_field_headers_async():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.ListVersionsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            appengine.ListVersionsResponse()
        )
        await client.list_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_versions_pager(transport_name: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                    version.Version(),
                ],
                next_page_token="abc",
            ),
            appengine.ListVersionsResponse(
                versions=[],
                next_page_token="def",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                ],
                next_page_token="ghi",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_versions(request={})

        assert pager._metadata == metadata

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, version.Version) for i in results)


def test_list_versions_pages(transport_name: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials,
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_versions), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                    version.Version(),
                ],
                next_page_token="abc",
            ),
            appengine.ListVersionsResponse(
                versions=[],
                next_page_token="def",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                ],
                next_page_token="ghi",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_versions(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_versions_async_pager():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_versions), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                    version.Version(),
                ],
                next_page_token="abc",
            ),
            appengine.ListVersionsResponse(
                versions=[],
                next_page_token="def",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                ],
                next_page_token="ghi",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_versions(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, version.Version) for i in responses)


@pytest.mark.asyncio
async def test_list_versions_async_pages():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_versions), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                    version.Version(),
                ],
                next_page_token="abc",
            ),
            appengine.ListVersionsResponse(
                versions=[],
                next_page_token="def",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                ],
                next_page_token="ghi",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
        # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
        async for page_ in (  # pragma: no branch
            await client.list_versions(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.GetVersionRequest,
        dict,
    ],
)
def test_get_version(request_type, transport: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = version.Version(
            name="name_value",
            id="id_value",
            inbound_services=[version.InboundServiceType.INBOUND_SERVICE_MAIL],
            instance_class="instance_class_value",
            zones=["zones_value"],
            runtime="runtime_value",
            runtime_channel="runtime_channel_value",
            threadsafe=True,
            vm=True,
            app_engine_apis=True,
            env="env_value",
            serving_status=version.ServingStatus.SERVING,
            created_by="created_by_value",
            disk_usage_bytes=1701,
            runtime_api_version="runtime_api_version_value",
            runtime_main_executable_path="runtime_main_executable_path_value",
            service_account="service_account_value",
            nobuild_files_regex="nobuild_files_regex_value",
            version_url="version_url_value",
        )
        response = client.get_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.GetVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, version.Version)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.inbound_services == [
        version.InboundServiceType.INBOUND_SERVICE_MAIL
    ]
    assert response.instance_class == "instance_class_value"
    assert response.zones == ["zones_value"]
    assert response.runtime == "runtime_value"
    assert response.runtime_channel == "runtime_channel_value"
    assert response.threadsafe is True
    assert response.vm is True
    assert response.app_engine_apis is True
    assert response.env == "env_value"
    assert response.serving_status == version.ServingStatus.SERVING
    assert response.created_by == "created_by_value"
    assert response.disk_usage_bytes == 1701
    assert response.runtime_api_version == "runtime_api_version_value"
    assert response.runtime_main_executable_path == "runtime_main_executable_path_value"
    assert response.service_account == "service_account_value"
    assert response.nobuild_files_regex == "nobuild_files_regex_value"
    assert response.version_url == "version_url_value"


def test_get_version_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_version), "__call__") as call:
        client.get_version()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.GetVersionRequest()


@pytest.mark.asyncio
async def test_get_version_async(
    transport: str = "grpc_asyncio", request_type=appengine.GetVersionRequest
):
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            version.Version(
                name="name_value",
                id="id_value",
                inbound_services=[version.InboundServiceType.INBOUND_SERVICE_MAIL],
                instance_class="instance_class_value",
                zones=["zones_value"],
                runtime="runtime_value",
                runtime_channel="runtime_channel_value",
                threadsafe=True,
                vm=True,
                app_engine_apis=True,
                env="env_value",
                serving_status=version.ServingStatus.SERVING,
                created_by="created_by_value",
                disk_usage_bytes=1701,
                runtime_api_version="runtime_api_version_value",
                runtime_main_executable_path="runtime_main_executable_path_value",
                service_account="service_account_value",
                nobuild_files_regex="nobuild_files_regex_value",
                version_url="version_url_value",
            )
        )
        response = await client.get_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.GetVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, version.Version)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.inbound_services == [
        version.InboundServiceType.INBOUND_SERVICE_MAIL
    ]
    assert response.instance_class == "instance_class_value"
    assert response.zones == ["zones_value"]
    assert response.runtime == "runtime_value"
    assert response.runtime_channel == "runtime_channel_value"
    assert response.threadsafe is True
    assert response.vm is True
    assert response.app_engine_apis is True
    assert response.env == "env_value"
    assert response.serving_status == version.ServingStatus.SERVING
    assert response.created_by == "created_by_value"
    assert response.disk_usage_bytes == 1701
    assert response.runtime_api_version == "runtime_api_version_value"
    assert response.runtime_main_executable_path == "runtime_main_executable_path_value"
    assert response.service_account == "service_account_value"
    assert response.nobuild_files_regex == "nobuild_files_regex_value"
    assert response.version_url == "version_url_value"


@pytest.mark.asyncio
async def test_get_version_async_from_dict():
    await test_get_version_async(request_type=dict)


def test_get_version_field_headers():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.GetVersionRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_version), "__call__") as call:
        call.return_value = version.Version()
        client.get_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_version_field_headers_async():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.GetVersionRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_version), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(version.Version())
        await client.get_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.CreateVersionRequest,
        dict,
    ],
)
def test_create_version(request_type, transport: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.CreateVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_version_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_version), "__call__") as call:
        client.create_version()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.CreateVersionRequest()


@pytest.mark.asyncio
async def test_create_version_async(
    transport: str = "grpc_asyncio", request_type=appengine.CreateVersionRequest
):
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.CreateVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_create_version_async_from_dict():
    await test_create_version_async(request_type=dict)


def test_create_version_field_headers():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.CreateVersionRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_version), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_version_field_headers_async():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.CreateVersionRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_version), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.UpdateVersionRequest,
        dict,
    ],
)
def test_update_version(request_type, transport: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.UpdateVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_version_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_version), "__call__") as call:
        client.update_version()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.UpdateVersionRequest()


@pytest.mark.asyncio
async def test_update_version_async(
    transport: str = "grpc_asyncio", request_type=appengine.UpdateVersionRequest
):
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.UpdateVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_version_async_from_dict():
    await test_update_version_async(request_type=dict)


def test_update_version_field_headers():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.UpdateVersionRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_version), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_version_field_headers_async():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.UpdateVersionRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_version), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.DeleteVersionRequest,
        dict,
    ],
)
def test_delete_version(request_type, transport: str = "grpc"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.DeleteVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_version_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_version), "__call__") as call:
        client.delete_version()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.DeleteVersionRequest()


@pytest.mark.asyncio
async def test_delete_version_async(
    transport: str = "grpc_asyncio", request_type=appengine.DeleteVersionRequest
):
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_version), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == appengine.DeleteVersionRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_delete_version_async_from_dict():
    await test_delete_version_async(request_type=dict)


def test_delete_version_field_headers():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.DeleteVersionRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_version), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_version_field_headers_async():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = appengine.DeleteVersionRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_version), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_version(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.ListVersionsRequest,
        dict,
    ],
)
def test_list_versions_rest(request_type):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "apps/sample1/services/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = appengine.ListVersionsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = appengine.ListVersionsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.list_versions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListVersionsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_versions_rest_interceptors(null_interceptor):
    transport = transports.VersionsRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.VersionsRestInterceptor(),
    )
    client = VersionsClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.VersionsRestInterceptor, "post_list_versions"
    ) as post, mock.patch.object(
        transports.VersionsRestInterceptor, "pre_list_versions"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = appengine.ListVersionsRequest.pb(appengine.ListVersionsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = appengine.ListVersionsResponse.to_json(
            appengine.ListVersionsResponse()
        )

        request = appengine.ListVersionsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = appengine.ListVersionsResponse()

        client.list_versions(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_list_versions_rest_bad_request(
    transport: str = "rest", request_type=appengine.ListVersionsRequest
):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "apps/sample1/services/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.list_versions(request)


def test_list_versions_rest_pager(transport: str = "rest"):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                    version.Version(),
                ],
                next_page_token="abc",
            ),
            appengine.ListVersionsResponse(
                versions=[],
                next_page_token="def",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                ],
                next_page_token="ghi",
            ),
            appengine.ListVersionsResponse(
                versions=[
                    version.Version(),
                    version.Version(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(appengine.ListVersionsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "apps/sample1/services/sample2"}

        pager = client.list_versions(request=sample_request)

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, version.Version) for i in results)

        pages = list(client.list_versions(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.GetVersionRequest,
        dict,
    ],
)
def test_get_version_rest(request_type):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "apps/sample1/services/sample2/versions/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = version.Version(
            name="name_value",
            id="id_value",
            inbound_services=[version.InboundServiceType.INBOUND_SERVICE_MAIL],
            instance_class="instance_class_value",
            zones=["zones_value"],
            runtime="runtime_value",
            runtime_channel="runtime_channel_value",
            threadsafe=True,
            vm=True,
            app_engine_apis=True,
            env="env_value",
            serving_status=version.ServingStatus.SERVING,
            created_by="created_by_value",
            disk_usage_bytes=1701,
            runtime_api_version="runtime_api_version_value",
            runtime_main_executable_path="runtime_main_executable_path_value",
            service_account="service_account_value",
            nobuild_files_regex="nobuild_files_regex_value",
            version_url="version_url_value",
        )

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = version.Version.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.get_version(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, version.Version)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.inbound_services == [
        version.InboundServiceType.INBOUND_SERVICE_MAIL
    ]
    assert response.instance_class == "instance_class_value"
    assert response.zones == ["zones_value"]
    assert response.runtime == "runtime_value"
    assert response.runtime_channel == "runtime_channel_value"
    assert response.threadsafe is True
    assert response.vm is True
    assert response.app_engine_apis is True
    assert response.env == "env_value"
    assert response.serving_status == version.ServingStatus.SERVING
    assert response.created_by == "created_by_value"
    assert response.disk_usage_bytes == 1701
    assert response.runtime_api_version == "runtime_api_version_value"
    assert response.runtime_main_executable_path == "runtime_main_executable_path_value"
    assert response.service_account == "service_account_value"
    assert response.nobuild_files_regex == "nobuild_files_regex_value"
    assert response.version_url == "version_url_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_version_rest_interceptors(null_interceptor):
    transport = transports.VersionsRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.VersionsRestInterceptor(),
    )
    client = VersionsClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        transports.VersionsRestInterceptor, "post_get_version"
    ) as post, mock.patch.object(
        transports.VersionsRestInterceptor, "pre_get_version"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = appengine.GetVersionRequest.pb(appengine.GetVersionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = version.Version.to_json(version.Version())

        request = appengine.GetVersionRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = version.Version()

        client.get_version(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_get_version_rest_bad_request(
    transport: str = "rest", request_type=appengine.GetVersionRequest
):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "apps/sample1/services/sample2/versions/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.get_version(request)


def test_get_version_rest_error():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.CreateVersionRequest,
        dict,
    ],
)
def test_create_version_rest(request_type):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "apps/sample1/services/sample2"}
    request_init["version"] = {
        "name": "name_value",
        "id": "id_value",
        "automatic_scaling": {
            "cool_down_period": {"seconds": 751, "nanos": 543},
            "cpu_utilization": {
                "aggregation_window_length": {},
                "target_utilization": 0.19540000000000002,
            },
            "max_concurrent_requests": 2499,
            "max_idle_instances": 1898,
            "max_total_instances": 2032,
            "max_pending_latency": {},
            "min_idle_instances": 1896,
            "min_total_instances": 2030,
            "min_pending_latency": {},
            "request_utilization": {
                "target_request_count_per_second": 3320,
                "target_concurrent_requests": 2820,
            },
            "disk_utilization": {
                "target_write_bytes_per_second": 3096,
                "target_write_ops_per_second": 2883,
                "target_read_bytes_per_second": 2953,
                "target_read_ops_per_second": 2740,
            },
            "network_utilization": {
                "target_sent_bytes_per_second": 2983,
                "target_sent_packets_per_second": 3179,
                "target_received_bytes_per_second": 3380,
                "target_received_packets_per_second": 3576,
            },
            "standard_scheduler_settings": {
                "target_cpu_utilization": 0.23770000000000002,
                "target_throughput_utilization": 0.3163,
                "min_instances": 1387,
                "max_instances": 1389,
            },
        },
        "basic_scaling": {"idle_timeout": {}, "max_instances": 1389},
        "manual_scaling": {"instances": 968},
        "inbound_services": [1],
        "instance_class": "instance_class_value",
        "network": {
            "forwarded_ports": ["forwarded_ports_value1", "forwarded_ports_value2"],
            "instance_tag": "instance_tag_value",
            "name": "name_value",
            "subnetwork_name": "subnetwork_name_value",
            "session_affinity": True,
        },
        "zones": ["zones_value1", "zones_value2"],
        "resources": {
            "cpu": 0.328,
            "disk_gb": 0.723,
            "memory_gb": 0.961,
            "volumes": [
                {
                    "name": "name_value",
                    "volume_type": "volume_type_value",
                    "size_gb": 0.739,
                }
            ],
            "kms_key_reference": "kms_key_reference_value",
        },
        "runtime": "runtime_value",
        "runtime_channel": "runtime_channel_value",
        "threadsafe": True,
        "vm": True,
        "app_engine_apis": True,
        "beta_settings": {},
        "env": "env_value",
        "serving_status": 1,
        "created_by": "created_by_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "disk_usage_bytes": 1701,
        "runtime_api_version": "runtime_api_version_value",
        "runtime_main_executable_path": "runtime_main_executable_path_value",
        "service_account": "service_account_value",
        "handlers": [
            {
                "url_regex": "url_regex_value",
                "static_files": {
                    "path": "path_value",
                    "upload_path_regex": "upload_path_regex_value",
                    "http_headers": {},
                    "mime_type": "mime_type_value",
                    "expiration": {},
                    "require_matching_file": True,
                    "application_readable": True,
                },
                "script": {"script_path": "script_path_value"},
                "api_endpoint": {"script_path": "script_path_value"},
                "security_level": 1,
                "login": 1,
                "auth_fail_action": 1,
                "redirect_http_response_code": 1,
            }
        ],
        "error_handlers": [
            {
                "error_code": 1,
                "static_file": "static_file_value",
                "mime_type": "mime_type_value",
            }
        ],
        "libraries": [{"name": "name_value", "version": "version_value"}],
        "api_config": {
            "auth_fail_action": 1,
            "login": 1,
            "script": "script_value",
            "security_level": 1,
            "url": "url_value",
        },
        "env_variables": {},
        "build_env_variables": {},
        "default_expiration": {},
        "health_check": {
            "disable_health_check": True,
            "host": "host_value",
            "healthy_threshold": 1819,
            "unhealthy_threshold": 2046,
            "restart_threshold": 1841,
            "check_interval": {},
            "timeout": {},
        },
        "readiness_check": {
            "path": "path_value",
            "host": "host_value",
            "failure_threshold": 1812,
            "success_threshold": 1829,
            "check_interval": {},
            "timeout": {},
            "app_start_timeout": {},
        },
        "liveness_check": {
            "path": "path_value",
            "host": "host_value",
            "failure_threshold": 1812,
            "success_threshold": 1829,
            "check_interval": {},
            "timeout": {},
            "initial_delay": {},
        },
        "nobuild_files_regex": "nobuild_files_regex_value",
        "deployment": {
            "files": {},
            "container": {"image": "image_value"},
            "zip_": {"source_url": "source_url_value", "files_count": 1179},
            "cloud_build_options": {
                "app_yaml_path": "app_yaml_path_value",
                "cloud_build_timeout": {},
            },
        },
        "version_url": "version_url_value",
        "endpoints_api_service": {
            "name": "name_value",
            "config_id": "config_id_value",
            "rollout_strategy": 1,
            "disable_trace_sampling": True,
        },
        "entrypoint": {"shell": "shell_value"},
        "vpc_access_connector": {"name": "name_value", "egress_setting": 1},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = appengine.CreateVersionRequest.meta.fields["version"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["version"].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["version"][field])):
                    del request_init["version"][field][i][subfield]
            else:
                del request_init["version"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.create_version(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_version_rest_interceptors(null_interceptor):
    transport = transports.VersionsRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.VersionsRestInterceptor(),
    )
    client = VersionsClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.VersionsRestInterceptor, "post_create_version"
    ) as post, mock.patch.object(
        transports.VersionsRestInterceptor, "pre_create_version"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = appengine.CreateVersionRequest.pb(appengine.CreateVersionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = appengine.CreateVersionRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.create_version(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_create_version_rest_bad_request(
    transport: str = "rest", request_type=appengine.CreateVersionRequest
):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "apps/sample1/services/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.create_version(request)


def test_create_version_rest_error():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.UpdateVersionRequest,
        dict,
    ],
)
def test_update_version_rest(request_type):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "apps/sample1/services/sample2/versions/sample3"}
    request_init["version"] = {
        "name": "name_value",
        "id": "id_value",
        "automatic_scaling": {
            "cool_down_period": {"seconds": 751, "nanos": 543},
            "cpu_utilization": {
                "aggregation_window_length": {},
                "target_utilization": 0.19540000000000002,
            },
            "max_concurrent_requests": 2499,
            "max_idle_instances": 1898,
            "max_total_instances": 2032,
            "max_pending_latency": {},
            "min_idle_instances": 1896,
            "min_total_instances": 2030,
            "min_pending_latency": {},
            "request_utilization": {
                "target_request_count_per_second": 3320,
                "target_concurrent_requests": 2820,
            },
            "disk_utilization": {
                "target_write_bytes_per_second": 3096,
                "target_write_ops_per_second": 2883,
                "target_read_bytes_per_second": 2953,
                "target_read_ops_per_second": 2740,
            },
            "network_utilization": {
                "target_sent_bytes_per_second": 2983,
                "target_sent_packets_per_second": 3179,
                "target_received_bytes_per_second": 3380,
                "target_received_packets_per_second": 3576,
            },
            "standard_scheduler_settings": {
                "target_cpu_utilization": 0.23770000000000002,
                "target_throughput_utilization": 0.3163,
                "min_instances": 1387,
                "max_instances": 1389,
            },
        },
        "basic_scaling": {"idle_timeout": {}, "max_instances": 1389},
        "manual_scaling": {"instances": 968},
        "inbound_services": [1],
        "instance_class": "instance_class_value",
        "network": {
            "forwarded_ports": ["forwarded_ports_value1", "forwarded_ports_value2"],
            "instance_tag": "instance_tag_value",
            "name": "name_value",
            "subnetwork_name": "subnetwork_name_value",
            "session_affinity": True,
        },
        "zones": ["zones_value1", "zones_value2"],
        "resources": {
            "cpu": 0.328,
            "disk_gb": 0.723,
            "memory_gb": 0.961,
            "volumes": [
                {
                    "name": "name_value",
                    "volume_type": "volume_type_value",
                    "size_gb": 0.739,
                }
            ],
            "kms_key_reference": "kms_key_reference_value",
        },
        "runtime": "runtime_value",
        "runtime_channel": "runtime_channel_value",
        "threadsafe": True,
        "vm": True,
        "app_engine_apis": True,
        "beta_settings": {},
        "env": "env_value",
        "serving_status": 1,
        "created_by": "created_by_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "disk_usage_bytes": 1701,
        "runtime_api_version": "runtime_api_version_value",
        "runtime_main_executable_path": "runtime_main_executable_path_value",
        "service_account": "service_account_value",
        "handlers": [
            {
                "url_regex": "url_regex_value",
                "static_files": {
                    "path": "path_value",
                    "upload_path_regex": "upload_path_regex_value",
                    "http_headers": {},
                    "mime_type": "mime_type_value",
                    "expiration": {},
                    "require_matching_file": True,
                    "application_readable": True,
                },
                "script": {"script_path": "script_path_value"},
                "api_endpoint": {"script_path": "script_path_value"},
                "security_level": 1,
                "login": 1,
                "auth_fail_action": 1,
                "redirect_http_response_code": 1,
            }
        ],
        "error_handlers": [
            {
                "error_code": 1,
                "static_file": "static_file_value",
                "mime_type": "mime_type_value",
            }
        ],
        "libraries": [{"name": "name_value", "version": "version_value"}],
        "api_config": {
            "auth_fail_action": 1,
            "login": 1,
            "script": "script_value",
            "security_level": 1,
            "url": "url_value",
        },
        "env_variables": {},
        "build_env_variables": {},
        "default_expiration": {},
        "health_check": {
            "disable_health_check": True,
            "host": "host_value",
            "healthy_threshold": 1819,
            "unhealthy_threshold": 2046,
            "restart_threshold": 1841,
            "check_interval": {},
            "timeout": {},
        },
        "readiness_check": {
            "path": "path_value",
            "host": "host_value",
            "failure_threshold": 1812,
            "success_threshold": 1829,
            "check_interval": {},
            "timeout": {},
            "app_start_timeout": {},
        },
        "liveness_check": {
            "path": "path_value",
            "host": "host_value",
            "failure_threshold": 1812,
            "success_threshold": 1829,
            "check_interval": {},
            "timeout": {},
            "initial_delay": {},
        },
        "nobuild_files_regex": "nobuild_files_regex_value",
        "deployment": {
            "files": {},
            "container": {"image": "image_value"},
            "zip_": {"source_url": "source_url_value", "files_count": 1179},
            "cloud_build_options": {
                "app_yaml_path": "app_yaml_path_value",
                "cloud_build_timeout": {},
            },
        },
        "version_url": "version_url_value",
        "endpoints_api_service": {
            "name": "name_value",
            "config_id": "config_id_value",
            "rollout_strategy": 1,
            "disable_trace_sampling": True,
        },
        "entrypoint": {"shell": "shell_value"},
        "vpc_access_connector": {"name": "name_value", "egress_setting": 1},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = appengine.UpdateVersionRequest.meta.fields["version"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["version"].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["version"][field])):
                    del request_init["version"][field][i][subfield]
            else:
                del request_init["version"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.update_version(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_version_rest_interceptors(null_interceptor):
    transport = transports.VersionsRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.VersionsRestInterceptor(),
    )
    client = VersionsClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.VersionsRestInterceptor, "post_update_version"
    ) as post, mock.patch.object(
        transports.VersionsRestInterceptor, "pre_update_version"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = appengine.UpdateVersionRequest.pb(appengine.UpdateVersionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = appengine.UpdateVersionRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.update_version(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_update_version_rest_bad_request(
    transport: str = "rest", request_type=appengine.UpdateVersionRequest
):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "apps/sample1/services/sample2/versions/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.update_version(request)


def test_update_version_rest_error():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


@pytest.mark.parametrize(
    "request_type",
    [
        appengine.DeleteVersionRequest,
        dict,
    ],
)
def test_delete_version_rest(request_type):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "apps/sample1/services/sample2/versions/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)

        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        response = client.delete_version(request)

    # Establish that the response is the type that we expect.
    assert response.operation.name == "operations/spam"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_version_rest_interceptors(null_interceptor):
    transport = transports.VersionsRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.VersionsRestInterceptor(),
    )
    client = VersionsClient(transport=transport)
    with mock.patch.object(
        type(client.transport._session), "request"
    ) as req, mock.patch.object(
        path_template, "transcode"
    ) as transcode, mock.patch.object(
        operation.Operation, "_set_result_from_operation"
    ), mock.patch.object(
        transports.VersionsRestInterceptor, "post_delete_version"
    ) as post, mock.patch.object(
        transports.VersionsRestInterceptor, "pre_delete_version"
    ) as pre:
        pre.assert_not_called()
        post.assert_not_called()
        pb_message = appengine.DeleteVersionRequest.pb(appengine.DeleteVersionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = Response()
        req.return_value.status_code = 200
        req.return_value.request = PreparedRequest()
        req.return_value._content = json_format.MessageToJson(
            operations_pb2.Operation()
        )

        request = appengine.DeleteVersionRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()

        client.delete_version(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()


def test_delete_version_rest_bad_request(
    transport: str = "rest", request_type=appengine.DeleteVersionRequest
):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "apps/sample1/services/sample2/versions/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, "request") as req, pytest.raises(
        core_exceptions.BadRequest
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        client.delete_version(request)


def test_delete_version_rest_error():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.VersionsGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = VersionsClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.VersionsGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = VersionsClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.VersionsGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = VersionsClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = VersionsClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.VersionsGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = VersionsClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.VersionsGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = VersionsClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.VersionsGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.VersionsGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.VersionsGrpcTransport,
        transports.VersionsGrpcAsyncIOTransport,
        transports.VersionsRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "rest",
    ],
)
def test_transport_kind(transport_name):
    transport = VersionsClient.get_transport_class(transport_name)(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert transport.kind == transport_name


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.VersionsGrpcTransport,
    )


def test_versions_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.VersionsTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_versions_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.appengine_admin_v1.services.versions.transports.VersionsTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.VersionsTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_versions",
        "get_version",
        "create_version",
        "update_version",
        "delete_version",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client

    # Catch all for all remaining methods and properties
    remainder = [
        "kind",
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_versions_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch(
        "google.cloud.appengine_admin_v1.services.versions.transports.VersionsTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.VersionsTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/appengine.admin",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            quota_project_id="octopus",
        )


def test_versions_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
        "google.cloud.appengine_admin_v1.services.versions.transports.VersionsTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.VersionsTransport()
        adc.assert_called_once()


def test_versions_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        VersionsClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/appengine.admin",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.VersionsGrpcTransport,
        transports.VersionsGrpcAsyncIOTransport,
    ],
)
def test_versions_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/appengine.admin",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.VersionsGrpcTransport,
        transports.VersionsGrpcAsyncIOTransport,
        transports.VersionsRestTransport,
    ],
)
def test_versions_transport_auth_gdch_credentials(transport_class):
    host = "https://language.com"
    api_audience_tests = [None, "https://language2.com"]
    api_audience_expect = [host, "https://language2.com"]
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, "default", autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(
                return_value=gdch_mock
            )
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(e)


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.VersionsGrpcTransport, grpc_helpers),
        (transports.VersionsGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_versions_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            "appengine.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/appengine.admin",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            scopes=["1", "2"],
            default_host="appengine.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [transports.VersionsGrpcTransport, transports.VersionsGrpcAsyncIOTransport],
)
def test_versions_grpc_transport_client_cert_source_for_mtls(transport_class):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


def test_versions_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.VersionsRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


def test_versions_rest_lro_client():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.AbstractOperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_versions_host_no_port(transport_name):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="appengine.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "appengine.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://appengine.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_versions_host_with_port(transport_name):
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="appengine.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "appengine.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://appengine.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_versions_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = VersionsClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = VersionsClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.list_versions._session
    session2 = client2.transport.list_versions._session
    assert session1 != session2
    session1 = client1.transport.get_version._session
    session2 = client2.transport.get_version._session
    assert session1 != session2
    session1 = client1.transport.create_version._session
    session2 = client2.transport.create_version._session
    assert session1 != session2
    session1 = client1.transport.update_version._session
    session2 = client2.transport.update_version._session
    assert session1 != session2
    session1 = client1.transport.delete_version._session
    session2 = client2.transport.delete_version._session
    assert session1 != session2


def test_versions_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.VersionsGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_versions_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.VersionsGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [transports.VersionsGrpcTransport, transports.VersionsGrpcAsyncIOTransport],
)
def test_versions_transport_channel_mtls_with_client_cert_source(transport_class):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [transports.VersionsGrpcTransport, transports.VersionsGrpcAsyncIOTransport],
)
def test_versions_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_versions_grpc_lro_client():
    client = VersionsClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_versions_grpc_lro_async_client():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsAsyncClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = VersionsClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = VersionsClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = VersionsClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = VersionsClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = VersionsClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = VersionsClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = VersionsClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = VersionsClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = VersionsClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = VersionsClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = VersionsClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = VersionsClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = VersionsClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = VersionsClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = VersionsClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.VersionsTransport, "_prep_wrapped_messages"
    ) as prep:
        client = VersionsClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.VersionsTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = VersionsClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


@pytest.mark.asyncio
async def test_transport_close_async():
    client = VersionsAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    with mock.patch.object(
        type(getattr(client.transport, "grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close():
    transports = {
        "rest": "_session",
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = VersionsClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        with mock.patch.object(
            type(getattr(client.transport, close_name)), "close"
        ) as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()


def test_client_ctx():
    transports = [
        "rest",
        "grpc",
    ]
    for transport in transports:
        client = VersionsClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [
        (VersionsClient, transports.VersionsGrpcTransport),
        (VersionsAsyncClient, transports.VersionsGrpcAsyncIOTransport),
    ],
)
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )
