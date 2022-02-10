# Video Streaming from Image

Generates a Stream from Images (here screenshots) based on flask.

## Showcase

![](doc/showcase.gif)

## Usage

### Download

#### Steps

1. Download [Releases](https://github.com/breezko/StreamingImages/releases) source code
2. Unzip
3. Navigate to root directory e.g `StreamingImages-1.0.0`
4. Proceed with [Dependencies](#dependencies) installation.

### Dependencies

```
pip install -r requirements.txt
```

### Running

```
flask run
```

_(optionally to have local network access)_

```
flask run -h 0.0.0.0
```

**Output**

```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Address

```
http://127.0.0.1:5000/
```
