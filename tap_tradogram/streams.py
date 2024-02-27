"""Stream type classes for tap-tradogram."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_tradogram.client import TradogramStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class SuppliersStream(TradogramStream):
    """Define custom stream."""

    name = "suppliers"
    path = "/suppliers"
    records_jsonpath = "$.Suppliers[*]"
    primary_keys = ["SupplierCode"]
    replication_key = "ModifiedDate"

    schema_filepath = SCHEMAS_DIR / "suppliers.json"
