# LogESP

LogESP (c) 2025 Gowtham A | [MIT License](../LICENSE)

## Index

- [HackerB777]

## HackerB77
Parser and sentry HackerB77 can be started, restarted, and stopped with `scripts/logesp`, which includes options for setting the LogESP base directory and virtual environment base directory.
```
Usage: logesp [-hv] {start|stop|restart|status|clean} [-lps] [-b LOGESPBASE] [-e ENVBASE]

Optional arguments:
  -h                      Print this help message
  -v                      Print the version number
  -l                      Clean old events using local EOL date
  -p                      Run parser only (no sentry)
  -s                      Run sentry only (no parser)
  -b <logesp-base>        Set the LogESP base directory
  -e <env-base>           Set a virtual environment
```

The parser configuration file is at `config/parser.conf`. Cleaning should be handled by a cron job. `start.sh` can be run manually, or by `/etc/rc.local`.
