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
from google.cloud.dlp_v2 import gapic_version as package_version

__version__ = package_version.__version__


from .services.dlp_service import DlpServiceAsyncClient, DlpServiceClient
from .types.dlp import (
    Action,
    ActivateJobTriggerRequest,
    AnalyzeDataSourceRiskDetails,
    BoundingBox,
    BucketingConfig,
    ByteContentItem,
    CancelDlpJobRequest,
    CharacterMaskConfig,
    CharsToIgnore,
    Color,
    Container,
    ContentItem,
    ContentLocation,
    ContentOption,
    CreateDeidentifyTemplateRequest,
    CreateDlpJobRequest,
    CreateInspectTemplateRequest,
    CreateJobTriggerRequest,
    CreateStoredInfoTypeRequest,
    CryptoDeterministicConfig,
    CryptoHashConfig,
    CryptoKey,
    CryptoReplaceFfxFpeConfig,
    DataProfileAction,
    DataProfileConfigSnapshot,
    DataProfileJobConfig,
    DataProfileLocation,
    DataProfilePubSubCondition,
    DataProfilePubSubMessage,
    DataRiskLevel,
    DateShiftConfig,
    DateTime,
    DeidentifyConfig,
    DeidentifyContentRequest,
    DeidentifyContentResponse,
    DeidentifyTemplate,
    DeleteDeidentifyTemplateRequest,
    DeleteDlpJobRequest,
    DeleteInspectTemplateRequest,
    DeleteJobTriggerRequest,
    DeleteStoredInfoTypeRequest,
    DlpJob,
    DlpJobType,
    DocumentLocation,
    EncryptionStatus,
    Error,
    ExcludeByHotword,
    ExcludeInfoTypes,
    ExclusionRule,
    FieldTransformation,
    Finding,
    FinishDlpJobRequest,
    FixedSizeBucketingConfig,
    GetDeidentifyTemplateRequest,
    GetDlpJobRequest,
    GetInspectTemplateRequest,
    GetJobTriggerRequest,
    GetStoredInfoTypeRequest,
    HybridContentItem,
    HybridFindingDetails,
    HybridInspectDlpJobRequest,
    HybridInspectJobTriggerRequest,
    HybridInspectResponse,
    HybridInspectStatistics,
    ImageLocation,
    ImageTransformations,
    InfoTypeCategory,
    InfoTypeDescription,
    InfoTypeStats,
    InfoTypeSummary,
    InfoTypeSupportedBy,
    InfoTypeTransformations,
    InspectConfig,
    InspectContentRequest,
    InspectContentResponse,
    InspectDataSourceDetails,
    InspectionRule,
    InspectionRuleSet,
    InspectJobConfig,
    InspectResult,
    InspectTemplate,
    JobTrigger,
    KmsWrappedCryptoKey,
    LargeCustomDictionaryConfig,
    LargeCustomDictionaryStats,
    ListDeidentifyTemplatesRequest,
    ListDeidentifyTemplatesResponse,
    ListDlpJobsRequest,
    ListDlpJobsResponse,
    ListInfoTypesRequest,
    ListInfoTypesResponse,
    ListInspectTemplatesRequest,
    ListInspectTemplatesResponse,
    ListJobTriggersRequest,
    ListJobTriggersResponse,
    ListStoredInfoTypesRequest,
    ListStoredInfoTypesResponse,
    Location,
    Manual,
    MatchingType,
    MetadataLocation,
    MetadataType,
    OtherInfoTypeSummary,
    OutputStorageConfig,
    PrimitiveTransformation,
    PrivacyMetric,
    ProfileStatus,
    QuasiId,
    QuoteInfo,
    Range,
    RecordCondition,
    RecordLocation,
    RecordSuppression,
    RecordTransformation,
    RecordTransformations,
    RedactConfig,
    RedactImageRequest,
    RedactImageResponse,
    ReidentifyContentRequest,
    ReidentifyContentResponse,
    RelationalOperator,
    ReplaceDictionaryConfig,
    ReplaceValueConfig,
    ReplaceWithInfoTypeConfig,
    ResourceVisibility,
    RiskAnalysisJobConfig,
    Schedule,
    StatisticalTable,
    StorageMetadataLabel,
    StoredInfoType,
    StoredInfoTypeConfig,
    StoredInfoTypeState,
    StoredInfoTypeStats,
    StoredInfoTypeVersion,
    Table,
    TableDataProfile,
    TableLocation,
    TimePartConfig,
    TransformationConfig,
    TransformationContainerType,
    TransformationDescription,
    TransformationDetails,
    TransformationDetailsStorageConfig,
    TransformationErrorHandling,
    TransformationLocation,
    TransformationOverview,
    TransformationResultStatus,
    TransformationResultStatusType,
    TransformationSummary,
    TransformationType,
    TransientCryptoKey,
    UnwrappedCryptoKey,
    UpdateDeidentifyTemplateRequest,
    UpdateInspectTemplateRequest,
    UpdateJobTriggerRequest,
    UpdateStoredInfoTypeRequest,
    Value,
    ValueFrequency,
    VersionDescription,
)
from .types.storage import (
    BigQueryField,
    BigQueryKey,
    BigQueryOptions,
    BigQueryTable,
    CloudStorageFileSet,
    CloudStorageOptions,
    CloudStoragePath,
    CloudStorageRegexFileSet,
    CustomInfoType,
    DatastoreKey,
    DatastoreOptions,
    EntityId,
    FieldId,
    FileType,
    HybridOptions,
    InfoType,
    Key,
    KindExpression,
    Likelihood,
    PartitionId,
    RecordKey,
    SensitivityScore,
    StorageConfig,
    StoredType,
    TableOptions,
)

__all__ = (
    "DlpServiceAsyncClient",
    "Action",
    "ActivateJobTriggerRequest",
    "AnalyzeDataSourceRiskDetails",
    "BigQueryField",
    "BigQueryKey",
    "BigQueryOptions",
    "BigQueryTable",
    "BoundingBox",
    "BucketingConfig",
    "ByteContentItem",
    "CancelDlpJobRequest",
    "CharacterMaskConfig",
    "CharsToIgnore",
    "CloudStorageFileSet",
    "CloudStorageOptions",
    "CloudStoragePath",
    "CloudStorageRegexFileSet",
    "Color",
    "Container",
    "ContentItem",
    "ContentLocation",
    "ContentOption",
    "CreateDeidentifyTemplateRequest",
    "CreateDlpJobRequest",
    "CreateInspectTemplateRequest",
    "CreateJobTriggerRequest",
    "CreateStoredInfoTypeRequest",
    "CryptoDeterministicConfig",
    "CryptoHashConfig",
    "CryptoKey",
    "CryptoReplaceFfxFpeConfig",
    "CustomInfoType",
    "DataProfileAction",
    "DataProfileConfigSnapshot",
    "DataProfileJobConfig",
    "DataProfileLocation",
    "DataProfilePubSubCondition",
    "DataProfilePubSubMessage",
    "DataRiskLevel",
    "DatastoreKey",
    "DatastoreOptions",
    "DateShiftConfig",
    "DateTime",
    "DeidentifyConfig",
    "DeidentifyContentRequest",
    "DeidentifyContentResponse",
    "DeidentifyTemplate",
    "DeleteDeidentifyTemplateRequest",
    "DeleteDlpJobRequest",
    "DeleteInspectTemplateRequest",
    "DeleteJobTriggerRequest",
    "DeleteStoredInfoTypeRequest",
    "DlpJob",
    "DlpJobType",
    "DlpServiceClient",
    "DocumentLocation",
    "EncryptionStatus",
    "EntityId",
    "Error",
    "ExcludeByHotword",
    "ExcludeInfoTypes",
    "ExclusionRule",
    "FieldId",
    "FieldTransformation",
    "FileType",
    "Finding",
    "FinishDlpJobRequest",
    "FixedSizeBucketingConfig",
    "GetDeidentifyTemplateRequest",
    "GetDlpJobRequest",
    "GetInspectTemplateRequest",
    "GetJobTriggerRequest",
    "GetStoredInfoTypeRequest",
    "HybridContentItem",
    "HybridFindingDetails",
    "HybridInspectDlpJobRequest",
    "HybridInspectJobTriggerRequest",
    "HybridInspectResponse",
    "HybridInspectStatistics",
    "HybridOptions",
    "ImageLocation",
    "ImageTransformations",
    "InfoType",
    "InfoTypeCategory",
    "InfoTypeDescription",
    "InfoTypeStats",
    "InfoTypeSummary",
    "InfoTypeSupportedBy",
    "InfoTypeTransformations",
    "InspectConfig",
    "InspectContentRequest",
    "InspectContentResponse",
    "InspectDataSourceDetails",
    "InspectJobConfig",
    "InspectResult",
    "InspectTemplate",
    "InspectionRule",
    "InspectionRuleSet",
    "JobTrigger",
    "Key",
    "KindExpression",
    "KmsWrappedCryptoKey",
    "LargeCustomDictionaryConfig",
    "LargeCustomDictionaryStats",
    "Likelihood",
    "ListDeidentifyTemplatesRequest",
    "ListDeidentifyTemplatesResponse",
    "ListDlpJobsRequest",
    "ListDlpJobsResponse",
    "ListInfoTypesRequest",
    "ListInfoTypesResponse",
    "ListInspectTemplatesRequest",
    "ListInspectTemplatesResponse",
    "ListJobTriggersRequest",
    "ListJobTriggersResponse",
    "ListStoredInfoTypesRequest",
    "ListStoredInfoTypesResponse",
    "Location",
    "Manual",
    "MatchingType",
    "MetadataLocation",
    "MetadataType",
    "OtherInfoTypeSummary",
    "OutputStorageConfig",
    "PartitionId",
    "PrimitiveTransformation",
    "PrivacyMetric",
    "ProfileStatus",
    "QuasiId",
    "QuoteInfo",
    "Range",
    "RecordCondition",
    "RecordKey",
    "RecordLocation",
    "RecordSuppression",
    "RecordTransformation",
    "RecordTransformations",
    "RedactConfig",
    "RedactImageRequest",
    "RedactImageResponse",
    "ReidentifyContentRequest",
    "ReidentifyContentResponse",
    "RelationalOperator",
    "ReplaceDictionaryConfig",
    "ReplaceValueConfig",
    "ReplaceWithInfoTypeConfig",
    "ResourceVisibility",
    "RiskAnalysisJobConfig",
    "Schedule",
    "SensitivityScore",
    "StatisticalTable",
    "StorageConfig",
    "StorageMetadataLabel",
    "StoredInfoType",
    "StoredInfoTypeConfig",
    "StoredInfoTypeState",
    "StoredInfoTypeStats",
    "StoredInfoTypeVersion",
    "StoredType",
    "Table",
    "TableDataProfile",
    "TableLocation",
    "TableOptions",
    "TimePartConfig",
    "TransformationConfig",
    "TransformationContainerType",
    "TransformationDescription",
    "TransformationDetails",
    "TransformationDetailsStorageConfig",
    "TransformationErrorHandling",
    "TransformationLocation",
    "TransformationOverview",
    "TransformationResultStatus",
    "TransformationResultStatusType",
    "TransformationSummary",
    "TransformationType",
    "TransientCryptoKey",
    "UnwrappedCryptoKey",
    "UpdateDeidentifyTemplateRequest",
    "UpdateInspectTemplateRequest",
    "UpdateJobTriggerRequest",
    "UpdateStoredInfoTypeRequest",
    "Value",
    "ValueFrequency",
    "VersionDescription",
)
