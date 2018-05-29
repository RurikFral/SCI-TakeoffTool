class HelperService:
    def __init__ (self):
        return

    def safe_cast(self, val, to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default