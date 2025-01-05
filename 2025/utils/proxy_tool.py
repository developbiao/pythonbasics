import os
from typing import Optional, Dict

class ProxyTool:
    PROXY_VARS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']
    _original_proxies: Dict[str, Optional[str]] = {}
    _is_enabled: bool = False
    
    @classmethod
    def set_proxy(cls, proxy_value: Optional[str] = None) -> None:
        """Set proxy value for future use."""
        if proxy_value is None:
            proxy_value = os.getenv("PROXY_VALUE", "http://localhost:7897")
        cls._proxy_value = proxy_value

    @classmethod
    def enable_proxy(cls) -> None:
        """Enable proxy settings and store original values."""
        if not cls._is_enabled and hasattr(cls, '_proxy_value'):
            # Store original values
            cls._original_proxies = {var: os.environ.get(var) for var in cls.PROXY_VARS}
            # Set new proxy values
            for proxy_var in cls.PROXY_VARS:
                os.environ[proxy_var] = cls._proxy_value
            cls._is_enabled = True

    @classmethod
    def disable_proxy(cls) -> None:
        """Disable proxy settings and restore original values."""
        if cls._is_enabled:
            # Restore original values or remove if not existed
            for var in cls.PROXY_VARS:
                if cls._original_proxies.get(var) is None:
                    os.environ.pop(var, None)
                else:
                    os.environ[var] = cls._original_proxies[var]
            cls._is_enabled = False

    @classmethod
    def is_enabled(cls) -> bool:
        """Check if proxy is currently enabled."""
        return cls._is_enabled
