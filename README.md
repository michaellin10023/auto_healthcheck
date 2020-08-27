#auto_healthcheck

ASU Health check auto login

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install selenium
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Setting up crontab (for MAC)
* * * * *  command to execute
│ │ │ │ │
│ │ │ │ └─── day of week (0 - 6) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
│ │ │ └──────── month (1 - 12)
│ │ └───────────── day of month (1 - 31)
│ └────────────────── hour (0 - 23)
└─────────────────────── min (0 - 59)

ie. 0 12 * * *

Go to terminal : env crontab -e

Paste: 
0 12 * * * cd /PATH/TO/SCRIPT && python3 healthCheck.py
