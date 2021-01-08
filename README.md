<div align="center">
  <h1>fetch-dummy-data</h1>
  Fetching dummy data asynchronously
</div>

<hr />

[![version](https://image-link)](https://package-link) [![downloads](https://image-link)](https://package-link) [![MIT License](https://image-link)](https://License-link)

A dummy data fetching module using javascript `callback`, `promise` and `async/await`.

fetc-dummy-data allows you to check and understand the working of javascipt's asynchronous function calls by using three different ways, namely:
1. JavaScript Callbacks
2. JavaScript Promises
3. JavaScript Async

## Features

- `.callbackProto` to fetch data asynchronously using javascript's callback feature by including `userId` as the function parameter.

- `.promiseProto` to fetch data asynchronously using javascript's promise feature by including `userId` as the function parameter.

- `.asyncAwaitProto` to fetch data asynchronously using javascript's async/await features by including `userId` as the function parameter.

- [Demo](#demo)
- [Installation](#installation)
- [Importing](#importing)
- [Fetching Dummy Data](#fetching-dummy-data)
    - [API](#api)
    - [Usage](#usage)

## Demo

#### Running callback

**`.callbackProto`**

#### Running promise

**`.promiseProto`**

#### Running async/await

**`.asyncAwaitProto`**

## Installation

`npm i --save-dev fetch-dummy-data`

`yarn add -D fetch-dummy-data`

## Importing

fetch-dummy-data is a default export so it can be imported with whatever name you like.

```js
const dummy = require('../fetch-dummy-data');
```

## Fetching Dummy Data

### API

#### `callbackProto(userId)`

##### `.callbackProto`:

- parameters: `Number` the userId of the data to be fetched.

#### `promiseProto(userId)`

##### `.promiseProto`:

- parameters: `Number` the userId of the data to be fetched.

#### `asyncAwaitProto(userId)`

##### `.asyncAwaitProto`:

- parameters: `Number` the userId of the data to be fetched.

### Usage

#### `.callbackProto(userId)`

1. ```js
    dummy.callbackProto(2);
    ```
    returns `String` ["Fetched Data: Donald Trump"]

2. ```js
    dummy.callbackProto(-2);
    ```
    returns `String` ["Error: Invalid ID"]

3. ```js
    dummy.callbackProto();
    ```
    returns `String` ["Error: ID missing"]

#### `.promiseProto(userId)`

1. ```js
    dummy.promiseProto(1);
    ```
    returns `String` ["Fetched Data: Joe Biden"]

2. ```js
    dummy.promiseProto(-2);
    ```
    returns `String` ["Error: Invalid ID"]

3. ```js
    dummy.promiseProto();
    ```
    returns `String` ["Error: ID missing"]

#### `.asyncAwaitProto(userId)`

1. ```js
    dummy.asyncAwaitProto(4);
    ```
    returns `String` ["Fetched Data: Howie Hawkins"]

2. ```js
    dummy.asyncAwaitProto(-2);
    ```
    returns `String` ["Error: Invalid ID"]

3. ```js
    dummy.asyncAwaitProto();
    ```
    returns `String` ["Error: ID missing"]

## License

To Be Added
