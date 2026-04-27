"""クルマコンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "クルマコンパス"
BLOG_DESCRIPTION = "中古車買取・査定の完全ガイド。カーセンサー・ガリバー・ナビクル等の業者比較、査定額アップの交渉術、廃車・事故車の売却まで徹底解説。"
BLOG_URL = "https://musclelove-777.github.io/kuruma-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/kuruma-compass"

TARGET_CATEGORIES = [
    "中古車買取業者比較",
    "査定の流れと準備",
    "査定額アップ術",
    "高額売却の交渉テクニック",
    "廃車・事故車の買取",
    "車種別買取相場",
    "売却時のトラブル対策",
    "下取り vs 買取",
]

THEME = {
    "primary": "#1f2d3d",
    "accent": "#f39c12",
    "gradient_start": "#1f2d3d",
    "gradient_end": "#f39c12",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
