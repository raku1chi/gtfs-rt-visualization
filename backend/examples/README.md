# GTFS-RT Visualization サンプルデータ

このディレクトリには、GTFS、GTFS-Flex、GTFS-Realtime の各形式のサンプルデータが含まれています。

## サンプルデータの種類

### 1. BasicGTFS

標準的な GTFS フィードのサンプルデータです。

- 東京駅、新宿駅、渋谷駅を結ぶバス路線
- 平日・休日のサービスパターン
- 基本的な GTFS ファイル構成（agency.txt、stops.txt、routes.txt 等）

### 2. GTFS-Flex

デマンド交通対応の GTFS-Flex サンプルデータです。

- フレキシブルサービスエリア（中央エリア、西部エリア）
- 固定停留所とフレキシブルエリアの組み合わせ
- デマンド応答型交通の予約対応時間窓

### 3. GTFS-Realtime

GTFS-Realtime の仕様定義ファイルです。

- Protocol Buffers での仕様定義
- TripUpdate、VehiclePosition、Alert メッセージ
