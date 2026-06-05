from pathlib import Path
from functools import lru_cache
import re


UI_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = UI_DIR.parents[1]
DATA_DIR = PROJECT_ROOT / "data"
LLM_CODE_DIR = UI_DIR / "LLM code"
VECTOR_DATA_DIR = LLM_CODE_DIR / "vector_data"
MOTOR_IMAGE_DIR = UI_DIR / "characteristics_curves_and_data_sheet"
MOTOR_SPEC_PDF = DATA_DIR / "B65542EN_01_ai-D伺服馬達仕樣.pdf"


def normalize_model_name(model_value) -> str:
    if model_value is None:
        return ""
    return " ".join(str(model_value).strip().split()).replace("α", "a").lower()


def normalize_page_filename(page_value) -> str | None:
    if page_value is None:
        return None

    page_text = str(page_value).strip()
    if not page_text or page_text.lower() == "nan":
        return None

    if page_text.endswith(".0"):
        page_text = page_text[:-2]

    if page_text.lower().endswith(".png"):
        page_text = page_text[:-4]

    if page_text.lower().startswith("page_"):
        page_text = page_text[5:]

    page_text = page_text.strip()
    if not page_text:
        return None

    return f"page_{page_text}.png"


@lru_cache(maxsize=1)
def _motor_model_image_map() -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    if not MOTOR_SPEC_PDF.exists():
        return mapping

    try:
        import fitz
    except Exception:
        return mapping

    try:
        doc = fitz.open(str(MOTOR_SPEC_PDF))
        for page_num in range(32, min(130, len(doc))):
            image_path = MOTOR_IMAGE_DIR / f"page_{page_num}.png"
            if not image_path.exists():
                continue

            lines = [line.strip() for line in doc[page_num].get_text().splitlines() if line.strip()]
            for line in lines:
                if not line.startswith("Model "):
                    continue
                model_name = line.replace("Model ", "", 1).strip()
                key = normalize_model_name(model_name)
                if key and key not in mapping:
                    mapping[key] = image_path
                break
    except Exception:
        return mapping
    finally:
        try:
            doc.close()
        except Exception:
            pass

    return mapping


def motor_image_path(page_value, model_name=None) -> Path | None:
    if model_name is not None:
        mapped_path = _motor_model_image_map().get(normalize_model_name(model_name))
        if mapped_path is not None:
            return mapped_path

    filename = normalize_page_filename(page_value)
    if filename is None:
        return None
    return MOTOR_IMAGE_DIR / filename


def _page_number_from_image_path(image_path: Path | None) -> int | None:
    if image_path is None:
        return None
    match = re.search(r"page_(\d+)\.png$", image_path.name)
    if not match:
        return None
    return int(match.group(1))


@lru_cache(maxsize=128)
def _render_motor_pdf_page(page_num: int, zoom: float = 3.0) -> bytes | None:
    if not MOTOR_SPEC_PDF.exists():
        return None

    try:
        import fitz
    except Exception:
        return None

    try:
        doc = fitz.open(str(MOTOR_SPEC_PDF))
        if page_num < 0 or page_num >= len(doc):
            return None

        page = doc[page_num]
        matrix = fitz.Matrix(zoom, zoom)
        clip = fitz.Rect(50, 50, 565, 300)
        pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
        return pix.tobytes("png")
    except Exception:
        return None
    finally:
        try:
            doc.close()
        except Exception:
            pass


def motor_image_png_bytes(page_value, model_name=None, zoom: float = 3.0) -> bytes | None:
    image_path = motor_image_path(page_value, model_name=model_name)
    page_num = _page_number_from_image_path(image_path)
    if page_num is None:
        return None
    return _render_motor_pdf_page(page_num, zoom=zoom)
