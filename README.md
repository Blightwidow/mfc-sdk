# MyFly Club SDK

## Install

```
pip install https://github.com/Blightwidow/mfc-sdk
```

## Usage

Once you set the environment variables (see /.env.example), then you can simply call the library:

```
aiports = mfc.aiports.all()
```

For the full documentation please refer to TODO


## Development

You can either use local install of `uv` or better, just develop in Docker with

```
docker run -it --rm --volume .:/app --volume /app/.venv $(docker build -q .) /bin/bash
```

then run tests via `uv run test`

### Jupyter

You can also setup a Jupyter playbook by using

```
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```

Once the kernek is install, you can simply start the hosting of the kernel via `uv run --with jupyter jupyter lab` or use an IDE like VSCode
