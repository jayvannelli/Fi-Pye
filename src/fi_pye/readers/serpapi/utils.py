

def validate_google_map_zoom(value: int) -> int | None:
    """ """
    if not isinstance(value, int):
        raise TypeError("Google map 'zoom' value must be of type: int. ")

    if value < 3 or value > 21:
        raise ValueError(f"Invalid zoom: {value}. Zoom value must be between 3-21.")

    return value
