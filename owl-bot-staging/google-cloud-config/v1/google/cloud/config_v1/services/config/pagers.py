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
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.config_v1.types import config


class ListDeploymentsPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.config_v1.types.ListDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.config_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., config.ListDeploymentsResponse],
            request: config.ListDeploymentsRequest,
            response: config.ListDeploymentsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.config_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.config_v1.types.ListDeploymentsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = config.ListDeploymentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config.ListDeploymentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[config.Deployment]:
        for page in self.pages:
            yield from page.deployments

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListDeploymentsAsyncPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.config_v1.types.ListDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.config_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[config.ListDeploymentsResponse]],
            request: config.ListDeploymentsRequest,
            response: config.ListDeploymentsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.config_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.config_v1.types.ListDeploymentsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = config.ListDeploymentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config.ListDeploymentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[config.Deployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListRevisionsPager:
    """A pager for iterating through ``list_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.config_v1.types.ListRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRevisions`` requests and continue to iterate
    through the ``revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.config_v1.types.ListRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., config.ListRevisionsResponse],
            request: config.ListRevisionsRequest,
            response: config.ListRevisionsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.config_v1.types.ListRevisionsRequest):
                The initial request object.
            response (google.cloud.config_v1.types.ListRevisionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = config.ListRevisionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config.ListRevisionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[config.Revision]:
        for page in self.pages:
            yield from page.revisions

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListRevisionsAsyncPager:
    """A pager for iterating through ``list_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.config_v1.types.ListRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRevisions`` requests and continue to iterate
    through the ``revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.config_v1.types.ListRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[config.ListRevisionsResponse]],
            request: config.ListRevisionsRequest,
            response: config.ListRevisionsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.config_v1.types.ListRevisionsRequest):
                The initial request object.
            response (google.cloud.config_v1.types.ListRevisionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = config.ListRevisionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config.ListRevisionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[config.Revision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListResourcesPager:
    """A pager for iterating through ``list_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.config_v1.types.ListResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListResources`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.config_v1.types.ListResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., config.ListResourcesResponse],
            request: config.ListResourcesRequest,
            response: config.ListResourcesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.config_v1.types.ListResourcesRequest):
                The initial request object.
            response (google.cloud.config_v1.types.ListResourcesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = config.ListResourcesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config.ListResourcesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[config.Resource]:
        for page in self.pages:
            yield from page.resources

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListResourcesAsyncPager:
    """A pager for iterating through ``list_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.config_v1.types.ListResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListResources`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.config_v1.types.ListResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[config.ListResourcesResponse]],
            request: config.ListResourcesRequest,
            response: config.ListResourcesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.config_v1.types.ListResourcesRequest):
                The initial request object.
            response (google.cloud.config_v1.types.ListResourcesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = config.ListResourcesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config.ListResourcesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[config.Resource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
