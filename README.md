# mystoq (Python SDK)

> Official Python SDK for [Mystoq](https://mystoq.com) -
> the simplest way to launch a cash-on-delivery online store in Algeria & MENA.

[![PyPI](https://img.shields.io/badge/pypi-mystoq-blue)](https://pypi.org/project/mystoq/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Install

```bash
pip install mystoq
```

## Quickstart

```python
from mystoq import MystoqClient

with MystoqClient(api_key="...", tenant="your-store") as mystoq:
    products = mystoq.list_products(limit=20)

    order = mystoq.create_order({
        "customer": {"name": "Yaakoub", "phone": "+213555123456"},
        "items": [{"product_id": "p_123", "quantity": 2}],
        "shipping": {"wilaya": "Annaba"},
        "payment_method": "cod",
    })
    print(f"order #{order['id']}")
```

## Why Mystoq

- COD-first e-commerce for Algeria & MENA
- 58 wilayas · Yalidine / Maystro / Stop Desk integrated
- FakeShield AI cuts COD returns by up to 30%
- Built in Algeria, MIT-licensed SDK

→ https://mystoq.com

## License

MIT - by [Hartem Yaakoub](https://hartem.tkawen.com) ·
[TKAWEN ecosystem](https://tkawen.com).

<!-- TKAWEN-ECOSYSTEM-FOOTER -->
## TKAWEN Ecosystem

This project is part of the [TKAWEN](https://tkawen.com) ecosystem — open APIs and tools for emerging-market digital infrastructure.

- [Mystoq](https://mystoq.com) — multi-tenant e-commerce platform for MENA
- [Algeria Certify](https://algeriacertify.com) — national digital credentialing
- [LIQAA](https://liqaa.io) — sovereign video conferencing
- [TKAWEN Academy](https://tkawen.com/academy) — online learning platform
- [SEO Toolkit](https://www.npmjs.com/package/@mystoq/seo-toolkit) — llms.txt, sitemap, Schema.org JSON-LD generators

Built by [Hartem Yaakoub](https://hartem.tkawen.com) - MIT licensed - Refreshed 2026-05-28.
