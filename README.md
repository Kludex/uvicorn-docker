# Uvicorn Docker

The goal of this repository is to maintain a production ready Uvicorn image.

The images generated here only contain the packages **necessary** for uvicorn to have the best possible performance.

There's no support for `websockets` by default. Install the `websockets` package to enable it.

### Customize

On the latest uvicorn release ([0.16.0](https://github.com/encode/uvicorn/releases/tag/0.16.0)), uvicorn enabled its configuration via environment variables.

For that reason, you can change any configuration just by using the `-e` argument on the `docker run` command:

```bash
docker run --rm -e "UVICORN_PORT=8080" --name uvicorn --p 8080:8080 kludex/uvicorn:latest
```

Notice that, uvicorn (and also this image) uses the port 8000 by default.

Feel free to check other configuration parameters on the [uvicorn documentation](https://www.uvicorn.org/settings/).

### Entrypoint

The docker image is able to run scripts before uvicorn takes action. Those scripts need to be located inside the
`/docker-entrypoint.d` directory.

Let's use the below script as an example:

```bash
echo "Hello World!"
```

On the Dockerfile, we need to copy that script to the `/docker-entrypoint.d` directory:
```Dockerfile
FROM kludex/uvicorn:latest

COPY script.sh /docker-entrypoint.d/
```

You'll be able to see the following logs when you run the image:

```bash
Hello World!
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

In case you want to see detailed logs from the entrypoint, you can enable the environment variable `ENTRYPOINT_VERBOSE`, e.g.:

```bash
docker run --rm -e "ENTRYPOINT_VERBOSE=1" -v $(pwd)/script.sh:/docker-entrypoint.d/script.sh --name uvicorn -p 8000:8000 kludex/uvicorn:latest
```

### Inspirations

This project was inspired by both:

- [inboard](https://github.com/br3ndonland/inboard)
- [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)

To be honest, the images are very different either conceptually and in practice, but you can see similarities in some ideas and on the pipeline. 😊

### License

This project is under the MIT license.
