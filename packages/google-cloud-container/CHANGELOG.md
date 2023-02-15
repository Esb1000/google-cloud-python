# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-container/#history

## [2.17.3](https://github.com/googleapis/python-container/compare/v2.17.2...v2.17.3) (2023-02-03)


### Documentation

* Add clarification on whether `NodePool.version` is a required field ([#344](https://github.com/googleapis/python-container/issues/344)) ([071c147](https://github.com/googleapis/python-container/commit/071c147df8e6edd72ff66b1997f21e881acd9b32))

## [2.17.2](https://github.com/googleapis/python-container/compare/v2.17.1...v2.17.2) (2023-01-30)


### Documentation

* Add references for available node image types ([76cfff8](https://github.com/googleapis/python-container/commit/76cfff85542aa1a8326efbfbc6d1c95b663e1452))
* Clarified wording around the NodePoolUpdateStrategy default behavior ([76cfff8](https://github.com/googleapis/python-container/commit/76cfff85542aa1a8326efbfbc6d1c95b663e1452))

## [2.17.1](https://github.com/googleapis/python-container/compare/v2.17.0...v2.17.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([cc5ebab](https://github.com/googleapis/python-container/commit/cc5ebabb1d584b137c42f45f55e6b803db72bf6d))


### Documentation

* Add documentation for enums ([cc5ebab](https://github.com/googleapis/python-container/commit/cc5ebabb1d584b137c42f45f55e6b803db72bf6d))

## [2.17.0](https://github.com/googleapis/python-container/compare/v2.16.0...v2.17.0) (2023-01-17)


### Features

* Add support for viewing the subnet IPv6 CIDR and services IPv6 CIDR assigned to dual stack clusters ([#333](https://github.com/googleapis/python-container/issues/333)) ([4d0a583](https://github.com/googleapis/python-container/commit/4d0a583f4ff23dca157b7835d9e59ec7ca9d16da))

## [2.16.0](https://github.com/googleapis/python-container/compare/v2.15.0...v2.16.0) (2023-01-10)


### Features

* Add etags for cluster and node pool update operations ([8eeee3b](https://github.com/googleapis/python-container/commit/8eeee3bda1e0eaae6fb375b47cc68b959f9b9feb))
* Add support for python 3.11 ([8eeee3b](https://github.com/googleapis/python-container/commit/8eeee3bda1e0eaae6fb375b47cc68b959f9b9feb))

## [2.15.0](https://github.com/googleapis/python-container/compare/v2.14.0...v2.15.0) (2023-01-09)


### Features

* Add EphemeralStorageLocalSsdConfig and LocalNvmeSsdBlockConfig APIs ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Add etags for cluster and node pool update operations ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Add support for specifying stack type for clusters ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Add WindowsNodeConfig field ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* CLUSTER_SCOPE option now available in DNSScope ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))
* Release GKE CloudDNS Cluster Scope ([403c1ad](https://github.com/googleapis/python-container/commit/403c1ad328e6d052d9e6aab667bb74b8b6a559b7))

## [2.14.0](https://github.com/googleapis/python-container/compare/v2.13.0...v2.14.0) (2022-12-15)


### Features

* Add API to enable GKE Gateway controller ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add compact placement feature for node pools ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add nodeconfig resource_labels api ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add support for `google.cloud.container.__version__` ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* Add support for specifying stack type for clusters. This will allow clusters to be created as dual stack or toggled between IPV4 and dual stack ([#323](https://github.com/googleapis/python-container/issues/323)) ([5c1d04f](https://github.com/googleapis/python-container/commit/5c1d04f874b64aabc378aa18370e0b6be503a886))
* Add typing to proto.Message based class attributes ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* GKE cluster's control plan/node-pool network isolation ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* **v1:** Add a FastSocket API ([4d61084](https://github.com/googleapis/python-container/commit/4d61084846ae9583140b04a4c68da070479d79b9))
* **v1beta1:** Add a FastSocket API ([#319](https://github.com/googleapis/python-container/issues/319)) ([5072864](https://github.com/googleapis/python-container/commit/50728649c915df27e8876af572ef824a26a660b7))


### Bug Fixes

* Add dict typing for client_options ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))
* Drop usage of pkg_resources ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))
* Fix timeout default values ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([944001d](https://github.com/googleapis/python-container/commit/944001d24215b0757da36898c26b8e22ca3f7a12))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([25c47a8](https://github.com/googleapis/python-container/commit/25c47a8433050c1cfcdf033dff16b3dcaedb1a9b))

## [2.13.0](https://github.com/googleapis/python-container/compare/v2.12.2...v2.13.0) (2022-10-26)


### Features

* launch GKE Cost Allocations configuration to the v1 GKE API ([d625e34](https://github.com/googleapis/python-container/commit/d625e3456bd37aa6cca4b0cf9de44c9ddb69ec21))
* vulnerability scanning exposed to public ([d625e34](https://github.com/googleapis/python-container/commit/d625e3456bd37aa6cca4b0cf9de44c9ddb69ec21))

## [2.12.2](https://github.com/googleapis/python-container/compare/v2.12.1...v2.12.2) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#305](https://github.com/googleapis/python-container/issues/305)) ([728fc48](https://github.com/googleapis/python-container/commit/728fc485d91c113a151dea2641ccfe163a5accaf))

## [2.12.1](https://github.com/googleapis/python-container/compare/v2.12.0...v2.12.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#301](https://github.com/googleapis/python-container/issues/301)) ([a4d1351](https://github.com/googleapis/python-container/commit/a4d1351c67659624d373f1fe4e3f5c61e99fa074))

## [2.12.0](https://github.com/googleapis/python-container/compare/v2.11.2...v2.12.0) (2022-09-16)


### Features

* Added High Throughput Logging API for Google Kubernetes Engine ([#297](https://github.com/googleapis/python-container/issues/297)) ([f774719](https://github.com/googleapis/python-container/commit/f7747196207f8487a4d50c93d76f8ea6e02f3f7c))


### Documentation

* missing period in description for min CPU platform ([f774719](https://github.com/googleapis/python-container/commit/f7747196207f8487a4d50c93d76f8ea6e02f3f7c))
* ReservationAffinity key field docs incorrect ([f774719](https://github.com/googleapis/python-container/commit/f7747196207f8487a4d50c93d76f8ea6e02f3f7c))

## [2.11.2](https://github.com/googleapis/python-container/compare/v2.11.1...v2.11.2) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([d68c842](https://github.com/googleapis/python-container/commit/d68c842bddad08c52ff0e4f1b34b70b4db667f8e))
* **deps:** require proto-plus >= 1.22.0 ([d68c842](https://github.com/googleapis/python-container/commit/d68c842bddad08c52ff0e4f1b34b70b4db667f8e))

## [2.11.1](https://github.com/googleapis/python-container/compare/v2.11.0...v2.11.1) (2022-08-02)


### Documentation

* **v1beta1:** BinaryAuthorization.enabled field is marked as deprecated ([0088035](https://github.com/googleapis/python-container/commit/00880358b4021191ff90f1f2a0f08160ce7b6d6a))
* **v1:** BinaryAuthorization.enabled field is marked as deprecated ([#272](https://github.com/googleapis/python-container/issues/272)) ([0088035](https://github.com/googleapis/python-container/commit/00880358b4021191ff90f1f2a0f08160ce7b6d6a))

## [2.11.0](https://github.com/googleapis/python-container/compare/v2.10.8...v2.11.0) (2022-07-16)


### Features

* add audience parameter ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add Binauthz Evaluation mode support to GKE Classic ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add GKE Identity Service ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add Location Policy API ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add managed prometheus feature ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add network tags to autopilot cluster ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* add support to modify kubelet pod pid limit in node system configuration ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support enabling Confidential Nodes in the node pool ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support GPU timesharing ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support node pool blue-green upgrade ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support spot VM ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* support Tier 1 bandwidth ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* update support for node pool labels, taints and network tags ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([e9dbd98](https://github.com/googleapis/python-container/commit/e9dbd9833c97733c402339a64e3440fa0dfb375e))
* require python 3.7+ ([#266](https://github.com/googleapis/python-container/issues/266)) ([01b78af](https://github.com/googleapis/python-container/commit/01b78af7d314551d69075005abd5f4e4ac826f5f))

## [2.10.8](https://github.com/googleapis/python-container/compare/v2.10.7...v2.10.8) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#252](https://github.com/googleapis/python-container/issues/252)) ([f5ab2a8](https://github.com/googleapis/python-container/commit/f5ab2a89d1238b2315963f4dd8469323746459f0))


### Documentation

* fix changelog header to consistent size ([#253](https://github.com/googleapis/python-container/issues/253)) ([9db4c78](https://github.com/googleapis/python-container/commit/9db4c786430da9a5831893a31321cb0e65db4751))

## [2.10.7](https://github.com/googleapis/python-container/compare/v2.10.6...v2.10.7) (2022-03-22)


### Bug Fixes

* test cleanup stages with try finally ([#212](https://github.com/googleapis/python-container/issues/212)) ([529bcbf](https://github.com/googleapis/python-container/commit/529bcbf618858aab17b6f5e86d25069a1266860a))

## [2.10.6](https://github.com/googleapis/python-container/compare/v2.10.5...v2.10.6) (2022-03-07)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#202](https://github.com/googleapis/python-container/issues/202)) ([444b806](https://github.com/googleapis/python-container/commit/444b8065a22da4c261b8b33ae8564d8329d3435d))
* **deps:** require proto-plus>=1.15.0 ([444b806](https://github.com/googleapis/python-container/commit/444b8065a22da4c261b8b33ae8564d8329d3435d))

## [2.10.5](https://github.com/googleapis/python-container/compare/v2.10.4...v2.10.5) (2022-02-16)


### Documentation

* **samples:** add usage samples to show handling of LRO response Operation ([#191](https://github.com/googleapis/python-container/issues/191)) ([309ad62](https://github.com/googleapis/python-container/commit/309ad6219a6e80d08bcd365a163e8273a6413ede))

## [2.10.4](https://github.com/googleapis/python-container/compare/v2.10.3...v2.10.4) (2022-02-14)


### Bug Fixes

* **deps:** move libcst to extras ([#194](https://github.com/googleapis/python-container/issues/194)) ([1c308c2](https://github.com/googleapis/python-container/commit/1c308c2e44dc16d0e8df5976de0b65d1e7c2041e))

## [2.10.3](https://github.com/googleapis/python-container/compare/v2.10.2...v2.10.3) (2022-02-11)


### Documentation

* add generated snippets ([#192](https://github.com/googleapis/python-container/issues/192)) ([e3a3a05](https://github.com/googleapis/python-container/commit/e3a3a056d80ac713edbf5cb4a8358063f8a83214))

## [2.10.2](https://github.com/googleapis/python-container/compare/v2.10.1...v2.10.2) (2022-02-04)

### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([07fbf3c](https://github.com/googleapis/python-container/commit/07fbf3cb1e140abf020e7cfbd083ed79aae701bf))

## [2.10.1](https://www.github.com/googleapis/python-container/compare/v2.10.0...v2.10.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([838a97b](https://www.github.com/googleapis/python-container/commit/838a97b0a45dcb16e81ec3795beaf35eaa5e460d))
* **deps:** require google-api-core >= 1.28.0 ([838a97b](https://www.github.com/googleapis/python-container/commit/838a97b0a45dcb16e81ec3795beaf35eaa5e460d))


### Documentation

* list oneofs in docstring ([838a97b](https://www.github.com/googleapis/python-container/commit/838a97b0a45dcb16e81ec3795beaf35eaa5e460d))

## [2.10.0](https://www.github.com/googleapis/python-container/compare/v2.9.0...v2.10.0) (2021-10-13)


### Features

* add support for python 3.10 ([#160](https://www.github.com/googleapis/python-container/issues/160)) ([ab146a5](https://www.github.com/googleapis/python-container/commit/ab146a5017805ec200dab2b74e025de0c647d742))

## [2.9.0](https://www.github.com/googleapis/python-container/compare/v2.8.1...v2.9.0) (2021-10-08)


### Features

* add context manager support in client ([#157](https://www.github.com/googleapis/python-container/issues/157)) ([03953f8](https://www.github.com/googleapis/python-container/commit/03953f8087b2583369b877672be81f2b8638020c))

## [2.8.1](https://www.github.com/googleapis/python-container/compare/v2.8.0...v2.8.1) (2021-10-04)


### Bug Fixes

* improper types in pagers generation ([6814251](https://www.github.com/googleapis/python-container/commit/68142512b75ee81a1fee0e982edd00a617706a00))

## [2.8.0](https://www.github.com/googleapis/python-container/compare/v2.7.1...v2.8.0) (2021-09-23)


### Features

* added a flag to enable/disable gvnic on a node pool ([#147](https://www.github.com/googleapis/python-container/issues/147)) ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added configuration for node pool defaults, autopilot, logging and monitoring ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added configuration for workload certificates and identity service component ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added node pool level network config ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added the option to list supported windows versions ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added the option to specify L4 load balancer configuration and IP v6 configuration ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* added update support for node pool labels, taints and network tags ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))


### Bug Fixes

* add 'dict' annotation type to 'request' ([c912605](https://www.github.com/googleapis/python-container/commit/c9126057cde7fc28094785cceab9cf43e42ca8e0))
* deprecated cluster status condition code ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* deprecated KALM addon config option ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))
* **deps:** require proto-plus 1.15.0 ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))


### Documentation

* clarified SetNodePoolSize API behavior ([616b21a](https://www.github.com/googleapis/python-container/commit/616b21a6abe2b0c4dd647cf56d544c2aff7312f7))

## [2.7.1](https://www.github.com/googleapis/python-container/compare/v2.7.0...v2.7.1) (2021-07-24)


### Bug Fixes

* enable self signed jwt for grpc ([#133](https://www.github.com/googleapis/python-container/issues/133)) ([6e34b81](https://www.github.com/googleapis/python-container/commit/6e34b81070b14de226c703191e8fe7f37357dea8))

## [2.7.0](https://www.github.com/googleapis/python-container/compare/v2.6.1...v2.7.0) (2021-07-22)


### Features

* add Samples section to CONTRIBUTING.rst ([#129](https://www.github.com/googleapis/python-container/issues/129)) ([a5905b8](https://www.github.com/googleapis/python-container/commit/a5905b820c970217a3ad1604982a7e38412d8dda))

## [2.6.1](https://www.github.com/googleapis/python-container/compare/v2.6.0...v2.6.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#128](https://www.github.com/googleapis/python-container/issues/128)) ([7a8fb93](https://www.github.com/googleapis/python-container/commit/7a8fb93cc083ffbd44b9c321a706ce6f37066ee1))

## [2.6.0](https://www.github.com/googleapis/python-container/compare/v2.5.0...v2.6.0) (2021-07-09)


### Features

* allow updating security group on existing clusters ([#120](https://www.github.com/googleapis/python-container/issues/120)) ([28a3fc9](https://www.github.com/googleapis/python-container/commit/28a3fc94cd7587b5900408bbadf994f143b0d0c3))
* allow updating security group on existing clusters ([#123](https://www.github.com/googleapis/python-container/issues/123)) ([e0d70e9](https://www.github.com/googleapis/python-container/commit/e0d70e98991eec24880497516829a0d4ed1dbc18))

## [2.5.0](https://www.github.com/googleapis/python-container/compare/v2.4.1...v2.5.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#119](https://www.github.com/googleapis/python-container/issues/119)) ([bb598c4](https://www.github.com/googleapis/python-container/commit/bb598c45f5f2c5ca75a638c17168d6a4a15547a4))
* support for NodeAutoprovisioning ImageType ([#107](https://www.github.com/googleapis/python-container/issues/107)) ([d56f699](https://www.github.com/googleapis/python-container/commit/d56f699dad3e7fdf654861e36a007a79df760790))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-container/issues/1127)) ([#112](https://www.github.com/googleapis/python-container/issues/112)) ([5a3941a](https://www.github.com/googleapis/python-container/commit/5a3941a03c48e3cef4d21ac10fc8e7b1b594ad1e)), closes [#1126](https://www.github.com/googleapis/python-container/issues/1126)

## [2.4.1](https://www.github.com/googleapis/python-container/compare/v2.4.0...v2.4.1) (2021-05-16)


### Bug Fixes

* **deps:** add packaging requirement ([#97](https://www.github.com/googleapis/python-container/issues/97)) ([1c46866](https://www.github.com/googleapis/python-container/commit/1c468663bd59bcb529311bd5736861b332a269b3))

## [2.4.0](https://www.github.com/googleapis/python-container/compare/v2.3.1...v2.4.0) (2021-03-24)


### Features

* add `from_service_account_info` ([#66](https://www.github.com/googleapis/python-container/issues/66)) ([f4f154d](https://www.github.com/googleapis/python-container/commit/f4f154db737fed68c49303133f4479199c0fdb12))

## [2.3.1](https://www.github.com/googleapis/python-container/compare/v2.3.0...v2.3.1) (2021-02-18)


### Bug Fixes

* remove client recv msg limit fix: add enums to `types/__init__.py` ([#60](https://www.github.com/googleapis/python-container/issues/60)) ([9207193](https://www.github.com/googleapis/python-container/commit/9207193fbaae7c6d91d87ffb9db57223f02544d6))

## [2.3.0](https://www.github.com/googleapis/python-container/compare/v2.2.0...v2.3.0) (2020-12-08)


### Features

* sync v1beta1 GKE API; deprecate SetLocations and use UpdateCluster; support for sysctls config in Linux nodes; support for node kubelet config controlling CPU manager policy, CFS quota; support for Customer Managed Encryption ([17f0a29](https://www.github.com/googleapis/python-container/commit/17f0a29401ffeaafca6166f9f6169a83c00b145a))


### Bug Fixes

* Update CODEOWNERS ([#59](https://www.github.com/googleapis/python-container/issues/59)) ([0f9a41e](https://www.github.com/googleapis/python-container/commit/0f9a41eb3394d4940941bc38a3e2e5cb3ad6b8dd)), closes [#58](https://www.github.com/googleapis/python-container/issues/58)


### Documentation

* **python:** update intersphinx for grpc and auth ([#53](https://www.github.com/googleapis/python-container/issues/53)) ([6a0fef7](https://www.github.com/googleapis/python-container/commit/6a0fef7f30976357cc9f42c0213931d1a2c76eac))

## [2.2.0](https://www.github.com/googleapis/python-container/compare/v2.1.0...v2.2.0) (2020-11-17)

All changes are from [#51](https://www.github.com/googleapis/python-container/issues/51) / [d3f5465](https://www.github.com/googleapis/python-container/commit/d3f546574300cd18bb0cb1627f226cfe34ee8098)

### Features

* support for GetJSONWebKeys
* support for Workload Identity
* support for Gvisor in nodes
* support for node reservation affinity
* support for Customer Managed Encryption in nodes
* support for NodeLocalDNS
* support for ConfigConnector
* support for private cluster VPC peering
* support for CloudRun load balancers
* support using routes for pod IPs
* support for Shielded Nodes
* support for release channels
* support for disabling default sNAT
* operations now store more granular progress
* support for node Surge Upgrades
* support for updating node pool locations.
* support for Node Auto Provisioning
* support for specifying node disk size and type

 
  
### Bug Fixes
* deprecate SetLocations; use UpdateCluster
* provide name alias for GetOperation (as method signature annotation)
* deprecate basic auth fields (removed in 1.19 clusters)
* deprecate Cluster/NodePool.status_message; use conditions

## [2.1.0](https://www.github.com/googleapis/python-container/compare/v2.0.1...v2.1.0) (2020-09-16)


### Features

* regenerate client lib to pick up new mtls env ([#44](https://www.github.com/googleapis/python-container/issues/44)) ([c4ffea0](https://www.github.com/googleapis/python-container/commit/c4ffea02fbc6c6566a4e772e2b353a5b4dc5b2fc))

## [2.0.1](https://www.github.com/googleapis/python-container/compare/v2.0.0...v2.0.1) (2020-07-24)


### Bug Fixes

* Update README.rst ([#35](https://www.github.com/googleapis/python-container/issues/35)) ([e7d1c66](https://www.github.com/googleapis/python-container/commit/e7d1c66a3f14dc9554a9fbdc78ec16bc912de5f9))


### Documentation

* link to migration guide ([#39](https://www.github.com/googleapis/python-container/issues/39)) ([5341b96](https://www.github.com/googleapis/python-container/commit/5341b96719a82cb8509f4dcc9e66ee05acd95ae9))

## [2.0.0](https://www.github.com/googleapis/python-container/compare/v1.0.1...v2.0.0) (2020-07-16)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#33). See the [migration guide](https://github.com/googleapis/python-container/blob/main/UPGRADING.md).

### Features

* migrate to microgenerator ([#33](https://www.github.com/googleapis/python-container/issues/33)) ([aa9b20c](https://www.github.com/googleapis/python-container/commit/aa9b20c6f4ccb6dff305bfcd72e1bde4a1ee86cd))

## [1.0.1](https://www.github.com/googleapis/python-container/compare/v1.0.0...v1.0.1) (2020-06-16)


### Bug Fixes

* fix `release_status` in `setup.py` ([#27](https://www.github.com/googleapis/python-container/issues/27)) ([d853d99](https://www.github.com/googleapis/python-container/commit/d853d99c73f4716721aa26d96ec6bc1a5c916dc4))

## [1.0.0](https://www.github.com/googleapis/python-container/compare/v0.5.0...v1.0.0) (2020-06-16)


### Features

* release as production/stable ([#24](https://www.github.com/googleapis/python-container/issues/24)) ([0e0095d](https://www.github.com/googleapis/python-container/commit/0e0095d8fad004d8098af62c6c27a40aa96d6257))

## [0.5.0](https://www.github.com/googleapis/python-container/compare/v0.4.0...v0.5.0) (2020-04-14)


### Features

* make `project_id`, `zone`, `cluster_id`, `node_pool` optional arguments to methods in `cluster_manager_client`; change default timeout config; add 2.7 sunset warning; bump copyright year to 2020 (via synth)([#8](https://www.github.com/googleapis/python-container/issues/8)) ([6afc050](https://www.github.com/googleapis/python-container/commit/6afc050f21c57a2d0eda3327c07510f2226aa6a6))

## [0.4.0](https://www.github.com/googleapis/python-container/compare/v0.3.0...v0.4.0) (2020-02-03)


### Features

* **container:** add 'list_usable_subnetworks' method; apply proto annotations (via synth) ([#9741](https://www.github.com/googleapis/python-container/issues/9741)) ([541a9e3](https://www.github.com/googleapis/python-container/commit/541a9e3974c38e2601c17c569099ce8602a1c4be))

## 0.3.0

07-30-2019 10:28 PDT


### Implementation Changes

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8501](https://github.com/googleapis/google-cloud-python/pull/8501))
- Add synth support for v1beta1 API version (via manual synth). ([#8436](https://github.com/googleapis/google-cloud-python/pull/8436))
-  Allow kwargs to be passed to create_channel (via synth).  ([#8384](https://github.com/googleapis/google-cloud-python/pull/8384))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### Documentation
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))

### Internal / Testing Changes
- Pin black version (via synth). ([#8575](https://github.com/googleapis/google-cloud-python/pull/8575))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8347](https://github.com/googleapis/google-cloud-python/pull/8347))
- Add disclaimer to auto-generated template files (via synth).  ([#8309](https://github.com/googleapis/google-cloud-python/pull/8309))
- Update noxfile and setup.py (via synth). ([#8298](https://github.com/googleapis/google-cloud-python/pull/8298))
- Blacken (via synth). ([#8285](https://github.com/googleapis/google-cloud-python/pull/8285))
- Add routing header to method metadata, add nox session `docs` (via synth). ([#7922](https://github.com/googleapis/google-cloud-python/pull/7922))
- Copy proto files alongside protoc versions.
- Minor gapic-generator change. ([#7225](https://github.com/googleapis/google-cloud-python/pull/7225))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers ([#7140](https://github.com/googleapis/google-cloud-python/pull/7140))
- Protoc-generated serialization update. ([#7078](https://github.com/googleapis/google-cloud-python/pull/7078))
- Pick up stub docstring fix in GAPIC generator. ([#6966](https://github.com/googleapis/google-cloud-python/pull/6966))

## 0.2.1

12-17-2018 16:36 PST


### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Improve linkage between container docs pages. ([#6852](https://github.com/googleapis/google-cloud-python/pull/6852))

### Internal / Testing Changes
- Add baseline for synth.metadata

## 0.2.0

12-04-2018 11:28 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core.iam.policy` ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6634](https://github.com/googleapis/google-cloud-python/pull/6634))
- Fix `client_info` bug, update docstrings. ([#6407](https://github.com/googleapis/google-cloud-python/pull/6407))
- Avoid overwriting '__module__' of messages from shared modules. ([#5364](https://github.com/googleapis/google-cloud-python/pull/5364))
- Fix bad trove classifier

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Docs: normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Container: harmonize / DRY 'README.rst' / 'docs/index.rst'. ([#6018](https://github.com/googleapis/google-cloud-python/pull/6018))
- Rename releases to changelog and include from CHANGELOG.md ([#5191](https://github.com/googleapis/google-cloud-python/pull/5191))

### Internal / Testing Changes
- Update noxfile.
- blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local dependencies from coverage. ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Unblack container gapic and protos.
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Pass posargs to py.test ([#6653](https://github.com/googleapis/google-cloud-python/pull/6653))
- Update synth.py yaml location ([#6480](https://github.com/googleapis/google-cloud-python/pull/6480))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Container: add 'synth.py'. ([#6084](https://github.com/googleapis/google-cloud-python/pull/6084))
- Nox: use inplace installs ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))
- Modify system tests to use prerelease versions of grpcio ([#5304](https://github.com/googleapis/google-cloud-python/pull/5304))
- Add Test runs for Python 3.7 and remove 3.4 ([#5295](https://github.com/googleapis/google-cloud-python/pull/5295))

## 0.1.1

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Documentation

- Replacing references to `stable/` docs with `latest/`. (#4638)

### Testing and internal changes

- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)
- nox unittest updates (#4646)

## 0.1.0

[![release level](https://img.shields.io/badge/release%20level-alpha-orange.svg?style&#x3D;flat)](https://cloud.google.com/terms/launch-stages)

Google Kubernetes Engine is a managed environment for deploying containerized
applications. It brings our latest innovations in developer productivity,
resource efficiency, automated operations, and open source flexibility to
accelerate your time to market.

PyPI: https://pypi.org/project/google-cloud-container/0.1.0/