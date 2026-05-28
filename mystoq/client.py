"""Mystoq Python SDK - https://mystoq.com"""
from __future__ import annotations

from typing import Any

import httpx


class MystoqClient:
    """Thin async/sync client for the Mystoq API."""

    def __init__(
        self,
        api_key: str,
        tenant: str | None = None,
        base_url: str = "https://api.mystoq.com/v1",
        timeout: float = 30.0,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")
        self._headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if tenant:
            self._headers["X-Tenant-ID"] = tenant
        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            headers=self._headers,
            timeout=timeout,
        )

    def list_products(self, **params: Any) -> dict:
        return self._req("GET", "/products", params=params)

    def get_product(self, product_id: str) -> dict:
        return self._req("GET", f"/products/{product_id}")

    def create_order(self, data: dict) -> dict:
        return self._req("POST", "/orders", json=data)

    def list_wilayas(self) -> dict:
        return self._req("GET", "/wilayas")

    def _req(self, method: str, path: str, **kw: Any) -> dict:
        r = self._client.request(method, path, **kw)
        r.raise_for_status()
        return r.json()

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "MystoqClient":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
