import time
from datetime import date

from fastapi import FastAPI

# from gtfs_loader import GTFSDataLoader  # 一時的にコメントアウト
from models import (
    Agency,
    Alert,
    Calendar,
    FeedInfo,
    FlexLocation,
    FlexStopTime,
    GTFSDataset,
    GTFSFlexDataset,
    GTFSRealtimeDataset,
    Route,
    Shape,
    Stop,
    StopTime,
    Trip,
    TripUpdate,
    VehiclePosition,
)

app = FastAPI(title="GTFS API Service", version="0.0.1")


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    return {"status": "healthy", "timestamp": int(time.time())}


# サンプルデータAPIエンドポイント
@app.get("/samples/basic-gtfs", response_model=GTFSDataset)
async def get_basic_gtfs_sample():
    """BasicGTFSサンプルデータを返す"""
    return GTFSDataset(
        agencies=[
            Agency(
                agency_id="DEMO",
                agency_name="Demo Transit",
                agency_url="https://www.demo-transit.com",
                agency_timezone="Asia/Tokyo",
                agency_lang="ja",
                agency_phone="03-1234-5678",
            )
        ],
        routes=[
            Route(
                route_id="ROUTE_001",
                agency_id="DEMO",
                route_short_name="1",
                route_long_name="東京駅 - 渋谷駅線",
                route_desc="東京駅から渋谷駅を結ぶ主要路線",
                route_type=3,
                route_color="FF0000",
                route_text_color="FFFFFF",
            ),
            Route(
                route_id="ROUTE_002",
                agency_id="DEMO",
                route_short_name="2",
                route_long_name="新宿 - 渋谷循環線",
                route_desc="新宿と渋谷を循環する路線",
                route_type=3,
                route_color="0000FF",
                route_text_color="FFFFFF",
            ),
        ],
        stops=[
            Stop(
                stop_id="STOP_001",
                stop_code="001",
                stop_name="東京駅前バス停",
                stop_desc="東京駅前の主要バス停",
                stop_lat=35.681000,
                stop_lon=139.767000,
                zone_id="1",
                location_type=0,
                stop_timezone="Asia/Tokyo",
                wheelchair_boarding=2,
            ),
            Stop(
                stop_id="STOP_002",
                stop_code="002",
                stop_name="新宿駅前バス停",
                stop_desc="新宿駅前の主要バス停",
                stop_lat=35.690800,
                stop_lon=139.700100,
                zone_id="1",
                location_type=0,
                stop_timezone="Asia/Tokyo",
                wheelchair_boarding=2,
            ),
            Stop(
                stop_id="STOP_003",
                stop_code="003",
                stop_name="渋谷駅前バス停",
                stop_desc="渋谷駅前の主要バス停",
                stop_lat=35.657900,
                stop_lon=139.701500,
                zone_id="1",
                location_type=0,
                stop_timezone="Asia/Tokyo",
                wheelchair_boarding=2,
            ),
        ],
        trips=[
            Trip(
                route_id="ROUTE_001",
                service_id="WEEKDAY",
                trip_id="TRIP_001_1",
                trip_headsign="渋谷駅行き",
                direction_id=0,
                block_id="BLOCK_1",
                shape_id="SHAPE_001",
                wheelchair_accessible=1,
                bikes_allowed=1,
            ),
            Trip(
                route_id="ROUTE_001",
                service_id="WEEKDAY",
                trip_id="TRIP_001_2",
                trip_headsign="東京駅行き",
                direction_id=1,
                block_id="BLOCK_1",
                shape_id="SHAPE_002",
                wheelchair_accessible=1,
                bikes_allowed=1,
            ),
        ],
        stop_times=[
            StopTime(
                trip_id="TRIP_001_1",
                arrival_time="08:00:00",
                departure_time="08:00:00",
                stop_id="STOP_001",
                stop_sequence=1,
                stop_headsign="渋谷駅行き",
                pickup_type=0,
                drop_off_type=0,
                shape_dist_traveled=0.0,
            ),
            StopTime(
                trip_id="TRIP_001_1",
                arrival_time="08:15:00",
                departure_time="08:15:00",
                stop_id="STOP_002",
                stop_sequence=2,
                pickup_type=0,
                drop_off_type=0,
                shape_dist_traveled=5.2,
            ),
            StopTime(
                trip_id="TRIP_001_1",
                arrival_time="08:30:00",
                departure_time="08:30:00",
                stop_id="STOP_003",
                stop_sequence=3,
                stop_headsign="渋谷駅",
                pickup_type=0,
                drop_off_type=0,
                shape_dist_traveled=8.7,
            ),
        ],
        calendar=[
            Calendar(
                service_id="WEEKDAY",
                monday=1,
                tuesday=1,
                wednesday=1,
                thursday=1,
                friday=1,
                saturday=0,
                sunday=0,
                start_date=date(2025, 1, 1),
                end_date=date(2025, 12, 31),
            ),
            Calendar(
                service_id="WEEKEND",
                monday=0,
                tuesday=0,
                wednesday=0,
                thursday=0,
                friday=0,
                saturday=1,
                sunday=1,
                start_date=date(2025, 1, 1),
                end_date=date(2025, 12, 31),
            ),
        ],
        calendar_dates=[],
        shapes=[
            Shape(
                shape_id="SHAPE_001",
                shape_pt_lat=35.681236,
                shape_pt_lon=139.767125,
                shape_pt_sequence=1,
                shape_dist_traveled=0.0,
            ),
            Shape(
                shape_id="SHAPE_001",
                shape_pt_lat=35.690921,
                shape_pt_lon=139.700258,
                shape_pt_sequence=2,
                shape_dist_traveled=5.2,
            ),
            Shape(
                shape_id="SHAPE_001",
                shape_pt_lat=35.658034,
                shape_pt_lon=139.701636,
                shape_pt_sequence=3,
                shape_dist_traveled=8.7,
            ),
        ],
        feed_info=FeedInfo(
            feed_publisher_name="Demo Transit",
            feed_publisher_url="https://www.demo-transit.com",
            feed_lang="ja",
            feed_start_date=date(2025, 1, 1),
            feed_end_date=date(2025, 12, 31),
            feed_version="1.0",
        ),
    )


@app.get("/samples/gtfs-flex", response_model=GTFSFlexDataset)
async def get_gtfs_flex_sample():
    """GTFS-Flexサンプルデータを返す"""
    # 基本GTFSデータ
    basic_data = await get_basic_gtfs_sample()

    # GTFS-Flex特有のデータを追加
    flex_agencies = [
        Agency(
            agency_id="FLEX_DEMO",
            agency_name="FlexDemo Transit",
            agency_url="https://www.flexdemo-transit.com",
            agency_timezone="Asia/Tokyo",
            agency_lang="ja",
            agency_phone="03-9876-5432",
        )
    ]

    flex_routes = [
        Route(
            route_id="FLEX_ROUTE_001",
            agency_id="FLEX_DEMO",
            route_short_name="F1",
            route_long_name="フレックス循環線",
            route_desc="市内デマンド交通路線",
            route_type=715,  # GTFS-Flex用のroute_type
            route_color="00AA00",
            route_text_color="FFFFFF",
        )
    ]

    flex_stops = [
        Stop(
            stop_id="AREA_001",
            stop_code="AREA1",
            stop_name="中央エリア",
            stop_desc="デマンド交通対応エリア1",
            stop_lat=35.680000,
            stop_lon=139.760000,
            zone_id="1",
            location_type=4,  # GTFS-Flexエリア
            stop_timezone="Asia/Tokyo",
            wheelchair_boarding=1,
        ),
        Stop(
            stop_id="FIXED_STOP_001",
            stop_code="F001",
            stop_name="市役所前",
            stop_desc="市役所前の固定停留所",
            stop_lat=35.685000,
            stop_lon=139.765000,
            zone_id="1",
            location_type=0,
            stop_timezone="Asia/Tokyo",
            wheelchair_boarding=1,
        ),
    ]

    flex_trips = [
        Trip(
            route_id="FLEX_ROUTE_001",
            service_id="FLEX_WEEKDAY",
            trip_id="FLEX_TRIP_001",
            trip_headsign="市内循環",
            trip_short_name="F1-1",
            direction_id=0,
            block_id="FLEX_BLOCK_1",
            wheelchair_accessible=1,
            bikes_allowed=0,
        )
    ]

    return GTFSFlexDataset(
        agencies=flex_agencies,
        routes=flex_routes,
        stops=flex_stops,
        trips=flex_trips,
        stop_times=basic_data.stop_times,
        calendar=basic_data.calendar,
        calendar_dates=[],
        shapes=[],
        feed_info=FeedInfo(
            feed_publisher_name="FlexDemo Transit",
            feed_publisher_url="https://www.flexdemo-transit.com",
            feed_lang="ja",
            feed_start_date=date(2025, 1, 1),
            feed_end_date=date(2025, 12, 31),
            feed_version="1.0",
        ),
        flex_locations=[
            FlexLocation(
                location_id="AREA_001",
                stop_name="中央エリア",
                geometry='{"type":"Polygon","coordinates":[[[139.755,35.675],[139.765,35.675],[139.765,35.685],[139.755,35.685],[139.755,35.675]]]}',
            )
        ],
        flex_stop_times=[
            FlexStopTime(
                trip_id="FLEX_TRIP_001",
                arrival_time="09:15:00",
                departure_time="09:45:00",
                stop_id="AREA_001",
                stop_sequence=2,
                pickup_type=3,
                drop_off_type=3,
                shape_dist_traveled=5.0,
                timepoint=0,
                start_pickup_drop_off_window="09:15:00",
                end_pickup_drop_off_window="09:45:00",
            )
        ],
    )


@app.get("/samples/gtfs-realtime", response_model=GTFSRealtimeDataset)
async def get_gtfs_realtime_sample():
    """GTFS-Realtimeサンプルデータを返す"""
    current_time = int(time.time())

    return GTFSRealtimeDataset(
        vehicle_positions=[
            VehiclePosition(
                vehicle_id="BUS_001",
                trip_id="TRIP_001_1",
                route_id="ROUTE_001",
                latitude=35.685000,
                longitude=139.760000,
                bearing=45.0,
                speed=12.5,
                timestamp=current_time,
                current_stop_sequence=2,
                current_status="IN_TRANSIT_TO",
                congestion_level="RUNNING_SMOOTHLY",
                occupancy_status="FEW_SEATS_AVAILABLE",
            ),
            VehiclePosition(
                vehicle_id="BUS_002",
                trip_id="TRIP_001_2",
                route_id="ROUTE_001",
                latitude=35.675000,
                longitude=139.680000,
                bearing=225.0,
                speed=8.0,
                timestamp=current_time - 30,
                current_stop_sequence=1,
                current_status="STOPPED_AT",
                congestion_level="STOP_AND_GO",
                occupancy_status="STANDING_ROOM_ONLY",
            ),
        ],
        trip_updates=[
            TripUpdate(
                trip_id="TRIP_001_1",
                route_id="ROUTE_001",
                start_time="08:00:00",
                start_date="20250915",
                schedule_relationship="SCHEDULED",
                vehicle_id="BUS_001",
                timestamp=current_time,
                delay=120,  # 2分遅れ
            ),
            TripUpdate(
                trip_id="TRIP_001_2",
                route_id="ROUTE_001",
                start_time="09:00:00",
                start_date="20250915",
                schedule_relationship="SCHEDULED",
                vehicle_id="BUS_002",
                timestamp=current_time - 30,
                delay=-60,  # 1分早着
            ),
        ],
        alerts=[
            Alert(
                alert_id="ALERT_001",
                cause="CONSTRUCTION",
                effect="DETOUR",
                header_text="工事による迂回運行",
                description_text="渋谷駅前の道路工事により、一部区間で迂回運行を実施しています。",
                url="https://www.demo-transit.com/alerts/001",
                active_period_start=current_time - 3600,
                active_period_end=current_time + 7200,
                informed_entities=["ROUTE_001", "ROUTE_002"],
            ),
            Alert(
                alert_id="ALERT_002",
                cause="WEATHER",
                effect="SIGNIFICANT_DELAYS",
                header_text="悪天候による遅延",
                description_text="強風の影響により、一部路線で遅延が発生しています。",
                active_period_start=current_time - 1800,
                active_period_end=current_time + 3600,
                informed_entities=["ROUTE_001"],
            ),
        ],
    )
