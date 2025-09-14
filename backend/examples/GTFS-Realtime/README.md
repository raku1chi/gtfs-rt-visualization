# GTFS-Realtime サンプルデータ

このディレクトリには、GTFS-Realtime フィードの仕様を定義する Protocol Buffers ファイルが含まれています。

## ファイル

- `gtfs-realtime.proto`: GTFS-Realtime の仕様を定義する Protocol Buffers ファイル

## GTFS-Realtime について

GTFS-Realtime は、交通機関がリアルタイムの運行情報を提供するための仕様です：

- **TripUpdate**: 遅延や運行変更の情報
- **VehiclePosition**: 車両の位置情報
- **Alert**: 運行に関するアラート情報

## 使用方法

この proto ファイルを使用して Python クラスを生成する場合：

```bash
protoc --python_out=. gtfs-realtime.proto
```

これにより、`gtfs_realtime_pb2.py`ファイルが生成され、GTFS-Realtime データの解析・生成に使用できます。
