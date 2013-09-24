latitude_conversion
===================

Convert Latitude's json from Google Takeout into a Splunk friendly JSON log file.

Latitude's format isn't very friendly, this will take it and do the following:

Convert the timestampMs into an ISO 8601 friendly UTC timestamped value.
Convert LatitudeE7/LongitudeE7 into Latitude/Longitude with decimals.
Drop all the commas and other formatting so it looks like a JSON log file.
