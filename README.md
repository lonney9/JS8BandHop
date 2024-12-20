# JS8Call Band Hopping Script
Simple band  hopping script for [JS8Call](https://js8call.com/).

Makes use of the [js8net API library](https://github.com/jfrancis42/js8net).

Only js8net.py is needed in addition to [band_hop.py](band_hop.py).

Edit the file to set the time spent on each band, 600 seconds (10 minutes) is set in wait_time. To test this can be changed to 5 or 10 seconds to see that it works with out waiting.

Add/remove frequencies as needed - 80, 40, 30, and 20m are set in dial_values.

In JS8Call Settings > Reporting, the TCP server under API needs to be enabled, assumes default port of 2442.

To interact with the API from the command line using the examples in the js8net readme and see the results:

```python
python3
from js8net import *
start_net("127.0.0.1", 2442)
```
