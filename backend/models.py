from datetime import date

from pydantic import BaseModel


class Agency(BaseModel):
    agency_id: str
    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_lang: str | None = None
    agency_phone: str | None = None
    agency_fare_url: str | None = None


class AgencyJP(BaseModel):
    agency_id: str
    agency_official_name: str | None = None
    agency_zip_number: str | None = None
    agency_address: str | None = None
    agency_president_pos: str | None = None
    agency_president_name: str | None = None


class Route(BaseModel):
    route_id: str
    agency_id: str | None = None
    route_short_name: str
    route_long_name: str
    route_desc: str | None = None
    route_type: int
    route_url: str | None = None
    route_color: str | None = None
    route_text_color: str | None = None
    route_sort_order: int | None = None


class Stop(BaseModel):
    stop_id: str
    stop_code: str | None = None
    stop_name: str
    stop_desc: str | None = None
    stop_lat: float
    stop_lon: float
    zone_id: str | None = None
    stop_url: str | None = None
    location_type: int | None = None
    parent_station: str | None = None
    stop_timezone: str | None = None
    wheelchair_boarding: int | None = None


class Trip(BaseModel):
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: str | None = None
    trip_short_name: str | None = None
    direction_id: int | None = None
    block_id: str | None = None
    shape_id: str | None = None
    wheelchair_accessible: int | None = None
    bikes_allowed: int | None = None


class StopTime(BaseModel):
    trip_id: str
    arrival_time: str
    departure_time: str
    stop_id: str
    stop_sequence: int
    stop_headsign: str | None = None
    pickup_type: int | None = None
    drop_off_type: int | None = None
    shape_dist_traveled: float | None = None
    timepoint: int | None = None


class Calendar(BaseModel):
    service_id: str
    monday: int
    tuesday: int
    wednesday: int
    thursday: int
    friday: int
    saturday: int
    sunday: int
    start_date: date
    end_date: date


class CalendarDate(BaseModel):
    service_id: str
    date: date
    exception_type: int


class Shape(BaseModel):
    shape_id: str
    shape_pt_lat: float
    shape_pt_lon: float
    shape_pt_sequence: int
    shape_dist_traveled: float | None = None


class FeedInfo(BaseModel):
    feed_publisher_name: str
    feed_publisher_url: str
    feed_lang: str
    feed_start_date: date | None = None
    feed_end_date: date | None = None
    feed_version: str | None = None


# GTFS-Flex Models
class FlexStopTime(StopTime):
    """GTFS-Flex用の拡張StopTime"""

    start_pickup_drop_off_window: str | None = None
    end_pickup_drop_off_window: str | None = None


class FlexLocation(BaseModel):
    """GTFS-Flexエリア定義"""

    location_id: str
    stop_name: str
    geometry: str  # WKT形式またはGeoJSON文字列


# GTFS-Realtime Models
class VehiclePosition(BaseModel):
    vehicle_id: str
    trip_id: str | None = None
    route_id: str | None = None
    latitude: float
    longitude: float
    bearing: float | None = None
    speed: float | None = None
    timestamp: int
    current_stop_sequence: int | None = None
    current_status: str | None = None
    congestion_level: str | None = None
    occupancy_status: str | None = None


class TripUpdate(BaseModel):
    trip_id: str
    route_id: str | None = None
    start_time: str | None = None
    start_date: str | None = None
    schedule_relationship: str | None = None
    vehicle_id: str | None = None
    timestamp: int
    delay: int | None = None


class StopTimeUpdate(BaseModel):
    stop_sequence: int | None = None
    stop_id: str | None = None
    arrival_delay: int | None = None
    arrival_time: int | None = None
    departure_delay: int | None = None
    departure_time: int | None = None
    schedule_relationship: str | None = None


class Alert(BaseModel):
    alert_id: str
    cause: str | None = None
    effect: str | None = None
    header_text: str
    description_text: str | None = None
    url: str | None = None
    active_period_start: int | None = None
    active_period_end: int | None = None
    informed_entities: list[str] = []


# Response Models
class GTFSDataset(BaseModel):
    """完全なGTFSデータセット"""

    agencies: list[Agency]
    routes: list[Route]
    stops: list[Stop]
    trips: list[Trip]
    stop_times: list[StopTime]
    calendar: list[Calendar]
    calendar_dates: list[CalendarDate]
    shapes: list[Shape]
    feed_info: FeedInfo | None = None


class GTFSFlexDataset(GTFSDataset):
    """GTFS-Flexデータセット"""

    flex_locations: list[FlexLocation]
    flex_stop_times: list[FlexStopTime]


class GTFSRealtimeDataset(BaseModel):
    """GTFS-Realtimeデータセット"""

    vehicle_positions: list[VehiclePosition]
    trip_updates: list[TripUpdate]
    alerts: list[Alert]
