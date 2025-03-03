# Changelog

## [0.6.3](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.2...google-maps-routing-v0.6.3) (2023-12-07)


### Features

* Add support for python 3.12 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Introduce compatibility with native namespace packages ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))
* Use `retry_async` instead of `retry` in async client ([31d043d](https://github.com/googleapis/google-cloud-python/commit/31d043de5a0b8bd329e8d5a36e7811d5ea7bd7a1))

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.1...google-maps-routing-v0.6.2) (2023-09-19)


### Documentation

* Minor formatting ([77bf61a](https://github.com/googleapis/google-cloud-python/commit/77bf61a36539bc2e6317dca1f954189d5241e4f1))

## [0.6.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.6.0...google-maps-routing-v0.6.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11450](https://github.com/googleapis/google-cloud-python/issues/11450)) ([bf58f57](https://github.com/googleapis/google-cloud-python/commit/bf58f5787dbc694e5bbe8fb48a1ede9e0089d26a))

## [0.6.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.5.1...google-maps-routing-v0.6.0) (2023-06-29)


### Features

* Add HTML Navigation Instructions feature to ComputeRoutes ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add more navigation instruction maneuvers ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add more toll pass values ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add TrafficModel feature in ComputeRoutes and ComputeRouteMatrix ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Add Waypoint Optimization feature to ComputeRoutes ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Support returning localized values in ComputeRoutes and ComputeRouteMatrix ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))
* Support Transit routes in ComputeRoutes and ComputeRouteMatrix ([e6e1e79](https://github.com/googleapis/google-cloud-python/commit/e6e1e7981085ccd1b0c9d97cc1009a6683a9192b))

## [0.5.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.5.0...google-maps-routing-v0.5.1) (2023-06-03)


### Documentation

* fix broken client library documentation links ([#11192](https://github.com/googleapis/google-cloud-python/issues/11192)) ([5e17f7a](https://github.com/googleapis/google-cloud-python/commit/5e17f7a901bbbae8ff9a44ed62f1abd2386da2c8))

## [0.5.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.4.0...google-maps-routing-v0.5.0) (2023-03-25)


### Features

* Add support for specifying region_code and language_code in the ComputeRouteMatrixRequest ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Add support for specifying region_code in the ComputeRoutesRequest ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Add support for specifying waypoints as addresses ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))


### Documentation

* Clarify usage of compute_alternative_routes in proto comment ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Clarify usage of RouteLegStepTravelAdvisory in comment ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))
* Update proto comments to contain concrete references to other proto messages ([80f77f1](https://github.com/googleapis/google-cloud-python/commit/80f77f17494d4d98e9f8ad7e0d4a693e4bd12ede))

## [0.4.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.3.1...google-maps-routing-v0.4.0) (2023-02-09)


### Features

* enable "rest" transport in Python for services supporting numeric enums ([#10839](https://github.com/googleapis/google-cloud-python/issues/10839)) ([ad59d56](https://github.com/googleapis/google-cloud-python/commit/ad59d569bda339ed31500602e2db369afdbfcf0b))

## [0.3.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.3.0...google-maps-routing-v0.3.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))


### Documentation

* Add documentation for enums ([900a608](https://github.com/googleapis/google-cloud-python/commit/900a6083e59bfebf215e4e469bc842d8788bba18))

## [0.3.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.2.0...google-maps-routing-v0.3.0) (2023-01-19)


### Features

* Add ExtraComputations feature to ComputeRoutes and ComputeRouteMatrix ([#10820](https://github.com/googleapis/google-cloud-python/issues/10820)) ([1812a88](https://github.com/googleapis/google-cloud-python/commit/1812a8860f4aa21fc1afaf8d37c8486010fa3984))

## [0.2.0](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.1.2...google-maps-routing-v0.2.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#10812](https://github.com/googleapis/google-cloud-python/issues/10812)) ([e5f88ee](https://github.com/googleapis/google-cloud-python/commit/e5f88eebd47c677850d61ddc3774532723f5505e))

## [0.1.2](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.1.1...google-maps-routing-v0.1.2) (2022-12-14)


### Documentation

* updated comment for ComputeRoutesRequest and ComputeRouteMatrixRequest ([2d9d62b](https://github.com/googleapis/google-cloud-python/commit/2d9d62b948c985cd0afac7bea0447f57e4b6ab69))
* updated comment for Route.route_token ([2d9d62b](https://github.com/googleapis/google-cloud-python/commit/2d9d62b948c985cd0afac7bea0447f57e4b6ab69))
* updated comment for RouteTravelMode ([2d9d62b](https://github.com/googleapis/google-cloud-python/commit/2d9d62b948c985cd0afac7bea0447f57e4b6ab69))

## [0.1.1](https://github.com/googleapis/google-cloud-python/compare/google-maps-routing-v0.1.0...google-maps-routing-v0.1.1) (2022-12-06)


### Bug Fixes

* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))
* Drop usage of pkg_resources ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))
* Fix timeout default values ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))


### Documentation

* **samples:** Snippetgen should call await on the operation coroutine before calling result ([e477ab2](https://github.com/googleapis/google-cloud-python/commit/e477ab2581f44b540051dd201b9f543a30044833))

## 0.1.0 (2022-11-10)


### Features

* add initial files for google.maps.routing.v2 ([#10770](https://github.com/googleapis/google-cloud-python/issues/10770)) ([42e0e59](https://github.com/googleapis/google-cloud-python/commit/42e0e594a8dd2ff06abc92111b537ee9271046e5))
* Add typing to proto.Message based class attributes ([a6cbc16](https://github.com/googleapis/google-cloud-python/commit/a6cbc167835880f9fe31b4030ec5fba69e35b383))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([a6cbc16](https://github.com/googleapis/google-cloud-python/commit/a6cbc167835880f9fe31b4030ec5fba69e35b383))

## Changelog
