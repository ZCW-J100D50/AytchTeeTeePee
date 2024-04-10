#

Verrrrry simple HTTP server in Java. Well, not as simple as golang or python, but well, _because java._

## To create the JAR file

```bash
mvn clean package
```

## To run the server

```bash
java -cp target/AytchTeeTeePee-1.0-SNAPSHOT.jar rocks.zipcode.ZipWebServer
```

### To run the python client

```bash
python3 src/main/java/rocks/zipcode/client.py
```

_Hey, Data, What would we have to do to make this a work with a url like below?_

```bash
python3 src/main/java/rocks/zipcode/client.py http://localhost:8000/foo
```

### To run the Java client

```bash
java -cp target/AytchTeeTeePee-1.0-SNAPSHOT.jar rocks.zipcode.WebClient http://localhost:8000/bar

# or
java -cp target/AytchTeeTeePee-1.0-SNAPSHOT.jar rocks.zipcode.WebClient
```

## In other languages

- In `python3`

````bash
in python3

```python
bash$ python3 -m http.server 9000
````

And that's all. (seriously, will start serving files from CWD)

- In golang

This is pretty simple.

```go
package main

import (
    "net/http"
)

// create a handler struct
type HttpHandler struct{}

// implement `ServeHTTP` method on `HttpHandler` struct
func (h HttpHandler) ServeHTTP(res http.ResponseWriter, req *http.Request) {
    // create response binary data
    data := []byte("Hello World!") // slice of bytes
    // write `data` to response
    res.Write(data)
}

func main() {

    // create a new handler
    handler := HttpHandler{}

    // listen and serve
    http.ListenAndServe(":9000", handler)

}
```

or again in go

```go
package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "Hello, playground")
	})

	log.Println("Starting server...")
	l, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		log.Fatal(err)
	}
	go func() {
		log.Fatal(http.Serve(l, nil))
	}()

	log.Println("Sending request...")
	res, err := http.Get("http://localhost:8080/hello")
	if err != nil {
		log.Fatal(err)
	}

	log.Println("Reading response...")
	if _, err := io.Copy(os.Stdout, res.Body); err != nil {
		log.Fatal(err)
	}
}
```
