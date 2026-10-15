from pathlib import Path

from fastapi import UploadFile

UPLOAD_DIR = Path("data/uploads")
MAX_UPLOAD_BYTES = 20 * 1024 * 1024


async def save_upload(file: UploadFile, document_id: str) -> Path:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    destination = UPLOAD_DIR / f"{document_id}.pdf"
    total = 0
    try:
        with destination.open("wb") as output:
            while chunk := await file.read(1024 * 1024):
                total += len(chunk)
                if total > MAX_UPLOAD_BYTES:
                    raise ValueError("PDF exceeds the 20 MB starter limit")
                output.write(chunk)
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    finally:
        await file.close()
    return destination
