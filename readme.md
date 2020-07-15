# environment

This application is only tested on MacOS 10.15.5.

Use Python 3.7 or above.

# setup

Install python libraries.

Please instal same version of chromedriver_binary as your chrome on Mac.

```bash

pip install -r requirements.txt

```

# run script

```bash

python main.py

```

# crontab setting

```bash

crontab -e

```

edit your crontab setting

```bash

14,29,44,59 10-14 * * 1-5 /some/where/python /some/where/dev/main.py

```

