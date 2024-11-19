from datetime import datetime


def current_year(request):
    return {"year": datetime.now().year}  # Get the current year
