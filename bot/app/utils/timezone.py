from datetime import datetime
from zoneinfo import ZoneInfo

REGION_CITIES = {
    "europe": ["Europe/London", "Europe/Berlin", "Europe/Warsaw", "Europe/Kyiv",
               "Europe/Athens", "Europe/Moscow", "Europe/Istanbul"],
    "americas": ["America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles",
                 "America/Mexico_City", "America/Sao_Paulo", "America/Argentina/Buenos_Aires",
                 "America/Lima"],
    "africa": ["Africa/Casablanca", "Africa/Lagos", "Africa/Kinshasa",
               "Africa/Johannesburg", "Africa/Nairobi", "Africa/Cairo"],
    "asia": ["Asia/Dubai", "Asia/Tehran", "Asia/Karachi", "Asia/Kolkata",
             "Asia/Bangkok", "Asia/Singapore", "Asia/Shanghai", "Asia/Tokyo", "Asia/Seoul"],
    "oceania": ["Australia/Perth", "Australia/Adelaide", "Australia/Sydney",
                "Australia/Melbourne", "Pacific/Auckland", "Pacific/Fiji"]
}

LANG_TO_TZ = {
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
}

def guess_timezone_from_language(lang: str) -> str | None:
    if not lang:
        return None
    return LANG_TO_TZ.get(lang.lower().split("-")[0])

def format_tz_offset(tz_name: str) -> str:
    offset_sec = datetime.now(ZoneInfo(tz_name)).utcoffset().total_seconds()
    hours = int(offset_sec // 3600)
    minutes = int((offset_sec % 3600) // 60)
    return f"UTC{hours:+d}" if minutes == 0 else f"UTC{hours:+d}:{minutes:02d}"