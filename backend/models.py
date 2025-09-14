from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Agency(BaseModel):
    agency_id: str
    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_lang: Optional[str] = None
    agency_phone: Optional[str] = None
    agency_fare_url: Optional[str] = None


class AgencyJP(BaseModel):
    agency_id: str
    agency_official_name: Optional[str] = None
    agency_zip_number: Optional[str] = None
    agency_address: Optional[str] = None
    agency_president_pos: Optional[str] = None
    agency_president_name: Optional[str] = None


class Route(BaseModel):
    route_id: str
    agency_id: Optional[str] = None
    route_short_name: str
    route_long_name: str
    route_desc: Optional[str] = None
    route_type: int
    route_url: Optional[str] = None
    route_color: Optional[str] = None
    route_text_color: Optional[str] = None
    route_sort_order: Optional[int] = None


class Stop(BaseModel):
    stop_id: str
    stop_code: Optional[str] = None
    stop_name: str
    stop_desc: Optional[str] = None
    stop_lat: float
    stop_lon: float
    zone_id: Optional[str] = None
    stop_url: Optional[str] = None
    location_type: Optional[int] = None
    parent_station: Optional[str] = None
    stop_timezone: Optional[str] = None
    wheelchair_boarding: Optional[int] = None


class Trip(BaseModel):
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: Optional[str] = None
    trip_short_name: Optional[str] = None
    direction_id: Optional[int] = None
    block_id: Optional[str] = None
    shape_id: Optional[str] = None
    wheelchair_accessible: Optional[int] = None
    bikes_allowed: Optional[int] = None


class StopTime(BaseModel):
    trip_id: str
    arrival_time: str
    departure_time: str
    stop_id: str
    stop_sequence: int
    stop_headsign: Optional[str] = None
    pickup_type: Optional[int] = None
    drop_off_type: Optional[int] = None
    shape_dist_traveled: Optional[float] = None
    timepoint: Optional[int] = None


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
    shape_dist_traveled: Optional[float] = None


class FeedInfo(BaseModel):
    feed_publisher_name: str
    feed_publisher_url: str
    feed_lang: str
    feed_start_date: Optional[date] = None
    feed_end_date: Optional[date] = None
    feed_version: Optional[str] = None


# GTFS-Flex Models
class FlexStopTime(StopTime):
    """GTFS-Flex用の拡張StopTime"""

    start_pickup_drop_off_window: Optional[str] = None
    end_pickup_drop_off_window: Optional[str] = None


class FlexLocation(BaseModel):
    """GTFS-Flexエリア定義"""

    location_id: str
    stop_name: str
    geometry: str  # WKT形式またはGeoJSON文字列


# GTFS-Realtime Models
class VehiclePosition(BaseModel):
    vehicle_id: str
    trip_id: Optional[str] = None
    route_id: Optional[str] = None
    latitude: float
    longitude: float
    bearing: Optional[float] = None
    speed: Optional[float] = None
    timestamp: int
    current_stop_sequence: Optional[int] = None
    current_status: Optional[str] = None
    congestion_level: Optional[str] = None
    occupancy_status: Optional[str] = None


class TripUpdate(BaseModel):
    trip_id: str
    route_id: Optional[str] = None
    start_time: Optional[str] = None
    start_date: Optional[str] = None
    schedule_relationship: Optional[str] = None
    vehicle_id: Optional[str] = None
    timestamp: int
    delay: Optional[int] = None


class StopTimeUpdate(BaseModel):
    stop_sequence: Optional[int] = None
    stop_id: Optional[str] = None
    arrival_delay: Optional[int] = None
    arrival_time: Optional[int] = None
    departure_delay: Optional[int] = None
    departure_time: Optional[int] = None
    schedule_relationship: Optional[str] = None


class Alert(BaseModel):
    alert_id: str
    cause: Optional[str] = None
    effect: Optional[str] = None
    header_text: str
    description_text: Optional[str] = None
    url: Optional[str] = None
    active_period_start: Optional[int] = None
    active_period_end: Optional[int] = None
    informed_entities: List[str] = []


# Response Models
class GTFSDataset(BaseModel):
    """完全なGTFSデータセット"""

    agencies: List[Agency]
    routes: List[Route]
    stops: List[Stop]
    trips: List[Trip]
    stop_times: List[StopTime]
    calendar: List[Calendar]
    calendar_dates: List[CalendarDate]
    shapes: List[Shape]
    feed_info: Optional[FeedInfo] = None


class GTFSFlexDataset(GTFSDataset):
    """GTFS-Flexデータセット"""

    flex_locations: List[FlexLocation]
    flex_stop_times: List[FlexStopTime]


class GTFSRealtimeDataset(BaseModel):
    """GTFS-Realtimeデータセット"""

    vehicle_positions: List[VehiclePosition]
    trip_updates: List[TripUpdate]
    alerts: List[Alert]
