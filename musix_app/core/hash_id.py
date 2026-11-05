import hashlib
import base64

def get_id(text: str, length: int = 8) -> str:
    hash_bytes = hashlib.md5(text.encode('utf-8')).digest()
    base64_id = base64.urlsafe_b64encode(hash_bytes).decode('utf-8')
    return base64_id.replace('=', '')[:length]

def get_hex_id(text: str, length: int = 10) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:length]