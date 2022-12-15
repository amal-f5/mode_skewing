# mode_skewing

## Eve configuration

```json
{
    "app": {
        "name": "myapp",
        "primary": {
            "type": "flask",
            "config": {
                "module": "flask_sc",
                "callable": "app"
            }
        }
    },
    "deployment": "mydeploy",
    "sources": {
        "name": "myrepo",
        "primary": {
            "branch": "master",
            "type": "repository",
            "uri": "https://github.com/amal-f5/mode_skewing.git"
        }
    }
}
```

## Changes required

Inside flask_sc.py, please wrap `app.run(..)` inside a `if __name__ == '__main__'` conditional
