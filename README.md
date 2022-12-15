# mode_skewing

## NGINX unit configuration inside eve container

```json
{
	"listeners": {
		"*:8080": {
			"pass": "applications/eve"
		},

		"*:9100": {
			"pass": "applications/metrics"
		},

		"*:8001": {
			"pass": "applications/sagar"
		}
	},

	"applications": {
		"eve": {
			"type": "python 3",
			"path": "/usr/local/eve",
			"module": "eveapi.__main__",
			"callable": "app",
			"user": "root"
		},

		"metrics": {
			"type": "python 3",
			"path": "/usr/local/eve/evemetrics",
			"module": "metrics",
			"callable": "app",
			"user": "evemetrics"
		},

		"sagar": {
			"type": "python 3",
			"path": "/mode_skewing",
			"working_directory": "/mode_skewing",
			"home": "/mode_skewing/venv",
			"module": "flask_sc",
			"callable": "app"
		}
	},

	"routes": {}
}

```
