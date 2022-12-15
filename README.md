# mode_skewing

## NGINX unit configuration

```json
{
	"listeners": {
		"*:8001": {
			"pass": "applications/sagar"
		}
	},

	"applications": {
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
