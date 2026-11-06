import os

from dotenv import load_dotenv

from config import INTERNAL_SYNC_KEY, SERVICE_TOKEN

load_dotenv()


def main():
    base_url = os.getenv("NAGRO_API_BASE_URL", "").rstrip("/")
    api_key = os.getenv("NAGRO_API_KEY", "")
    webhook_secret = os.getenv("NAGRO_WEBHOOK_SECRET", "")
    tenant_id = os.getenv("NAGRO_TENANT_ID", "")
    client_id = os.getenv("NAGRO_CLIENT_ID", "")
    client_secret = os.getenv("NAGRO_CLIENT_SECRET", "")
    signing_key_id = os.getenv("NAGRO_SIGNING_KEY_ID", "")
    partner_slug = os.getenv("NAGRO_PARTNER_SLUG", "")
    timeout_raw = os.getenv("NAGRO_REQUEST_TIMEOUT_SECONDS", "30")
    environment = os.getenv("NAGRO_ENVIRONMENT", "")
    try:
        request_timeout_seconds = int(timeout_raw)
    except ValueError:
        request_timeout_seconds = 30
    _ = {
        "base_url": base_url,
        "api_key": api_key,
        "webhook_secret": webhook_secret,
        "tenant_id": tenant_id,
        "client_id": client_id,
        "client_secret": client_secret,
        "signing_key_id": signing_key_id,
        "partner_slug": partner_slug,
        "request_timeout_seconds": request_timeout_seconds,
        "environment": environment,
        "service_token": SERVICE_TOKEN,
        "internal_sync_key": INTERNAL_SYNC_KEY,
    }
    return _


if __name__ == "__main__":
    main()
