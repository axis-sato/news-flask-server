import pytz

timezone = pytz.timezone('Asia/Tokyo')

def localize(datetime):
    return timezone.localize(datetime)
