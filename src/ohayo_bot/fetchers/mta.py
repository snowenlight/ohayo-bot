import requests
from google.transit import gtfs_realtime_pb2
from .base import BaseFetcher

_ALERTS_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts"


class MTAFetcher(BaseFetcher):
    def fetch(self) -> dict:
        resp = requests.get(_ALERTS_URL, timeout=10)
        resp.raise_for_status()

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(resp.content)

        disruptions = []
        seen = set()
        for entity in feed.entity:
            if not entity.HasField("alert"):
                continue
            alert = entity.alert
            effect = gtfs_realtime_pb2.Alert.Effect.Name(alert.effect)
            if effect in ("NO_SERVICE", "REDUCED_SERVICE", "SIGNIFICANT_DELAYS", "SUSPENSION"):
                for informed in alert.informed_entity:
                    route = informed.route_id
                    if route and route not in seen:
                        seen.add(route)
                        disruptions.append({"line": route, "status": effect.replace("_", " ").title()})

        return {"disruptions": sorted(disruptions, key=lambda d: d["line"])}
