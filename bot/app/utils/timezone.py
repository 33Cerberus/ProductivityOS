def guess_timezone_from_language(lang: str) -> str | None:
    if not lang:
        return None

    lang = lang.lower().split("-")[0]

    return {
        "uk": "Europe/Kyiv",
        "ru": "Europe/Moscow",
        "pl": "Europe/Warsaw",
        "de": "Europe/Berlin",
        "fr": "Europe/Paris",
        "es": "Europe/Madrid",
        "it": "Europe/Rome",
        "nl": "Europe/Amsterdam",
        "sv": "Europe/Stockholm",
        "no": "Europe/Oslo",
        "da": "Europe/Copenhagen",
        "fi": "Europe/Helsinki",
        "ja": "Asia/Tokyo",
        "ko": "Asia/Seoul",
        "zh": "Asia/Shanghai",
        "tr": "Europe/Istanbul",
        "ar": "Asia/Riyadh",
        "pt": "America/Sao_Paulo",
        "en": "UTC",
    }.get(lang)

REGION_CITIES = {
    "europe": [
        "Europe/London", "Europe/Berlin", "Europe/Warsaw", "Europe/Kyiv",
        "Europe/Athens", "Europe/Moscow", "Europe/Istanbul"
    ],
    "americas": [
        "America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles",
        "America/Mexico_City", "America/Sao_Paulo", "America/Argentina/Buenos_Aires",
        "America/Lima"
    ],
    "africa": [
        "Africa/Casablanca", "Africa/Lagos", "Africa/Kinshasa",
        "Africa/Johannesburg", "Africa/Nairobi", "Africa/Cairo"
    ],
    "asia": [
        "Asia/Dubai", "Asia/Tehran", "Asia/Karachi", "Asia/Kolkata",
        "Asia/Bangkok", "Asia/Singapore", "Asia/Shanghai", "Asia/Tokyo", "Asia/Seoul"
    ],
    "oceania": [
        "Australia/Perth", "Australia/Adelaide", "Australia/Sydney",
        "Australia/Melbourne", "Pacific/Auckland", "Pacific/Fiji"
    ]
}