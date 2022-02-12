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
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteEvent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-video-live-stream


# [START livestream_generated_live_stream_v1_LivestreamService_DeleteEvent_sync]
from google.cloud.video import live_stream_v1


def sample_delete_event():
    # Create a client
    client = live_stream_v1.LivestreamServiceClient()

    # Initialize request argument(s)
    request = live_stream_v1.DeleteEventRequest(
        name="name_value",
    )

    # Make the request
    client.delete_event(request=request)


# [END livestream_generated_live_stream_v1_LivestreamService_DeleteEvent_sync]
