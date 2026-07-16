"""Shared project constants used by synchronization and validation scripts."""

PLATFORM_SKILL_NAMES = (
    "sku-taobao",
    "sku-tmall",
    "sku-pinduoduo",
    "sku-jd",
    "sku-1688",
    "sku-amazon",
    "sku-shopify",
    "sku-tiktok-shop",
)

CORE_SKILL_NAMES = (
    "sku-detail-page-director",
    "sku-product-core",
    "sku-reference-migration",
)

ALL_SKILL_NAMES = (
    *CORE_SKILL_NAMES,
    *PLATFORM_SKILL_NAMES,
)
