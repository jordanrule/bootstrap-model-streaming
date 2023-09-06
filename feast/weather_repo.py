from datetime import timedelta

import pandas as pd

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource,
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float64, String

loc = Entity(name="location", join_keys=["location"])

weather_stats_source = FileSource(
    name="weather_stats_source",
    path="/Users/jordan.rule/git/austin_weather/feature_repo/data/austin_weather.parquet",
    timestamp_field="date",
)

weather_stats_push_source = PushSource(
    name="weather_stats_push_source",
    batch_source=weather_stats_source,
)

weather_stats_fresh_fv = FeatureView(
    name="weather_hourly_stats_fresh",
    entities=[loc],
    schema=[
        Field(name="date", dtype=String),
        Field(name="temperature", dtype=Float64),
    ],
    online=True,
    source=weather_stats_source,
)

weather_stats_online = FeatureService(
    name="weather_stats_online",
    features=[weather_stats_fresh_fv],
)
