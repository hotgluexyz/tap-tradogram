"""Stream type classes for tap-tradogram."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_tradogram.client import TradogramStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class SuppliersStream(TradogramStream):
    name = "suppliers"
    path = "/suppliers"
    records_jsonpath = "$.Suppliers[*]"
    primary_keys = ["SupplierCode"]
    replication_key = "ModifiedDate"

    schema_filepath = SCHEMAS_DIR / "suppliers.json"


class InvoicesStream(TradogramStream):
    name = "invoices"
    path = "/invoices"
    records_jsonpath = "$.Bills[*]"
    primary_keys = ["InvoiceCode"]
    replication_key = "ModifiedDate"

    schema_filepath = SCHEMAS_DIR / "invoices.json"

    def get_url_params(self, context, next_page_token):
        """Return a dictionary of values to be used in URL parameterization."""

        params = super().get_url_params(context, next_page_token)

        # Allow filtering by comma separated invoice status e.g. Paid
        if self.config.get("invoice_status"):
            params["status"] = self.config.get("invoice_status")

        return params


class PurchaseOrdersStream(TradogramStream):
    name = "purchase_orders"
    path = "/purchase_orders"
    records_jsonpath = "$.PurchaseOrders[*]"
    primary_keys = ["POCode"]
    replication_key = "ModifiedDate"

    schema_filepath = SCHEMAS_DIR / "purchase_orders.json"
