# MyFly Club SDK

## Development

You can either use local install of `uv` or better, just develop in Docker with

```
docker run -it --rm --volume .:/app --volume /app/.venv $(docker build -q .) /bin/bash
```

then run tests via `uv run test`
