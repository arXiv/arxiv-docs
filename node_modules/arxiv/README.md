# node-arxiv

Wrapper over the [Arxiv API](http://arxiv.org/help/api/index)

## Install

```
npm install arxiv
```

## Usage

```js
arxiv = require('arxiv');

search_query = {
    title: 'RNN',
    author: 'William Chan'
};

arxiv.search(search_query, function(err, results) {
    console.log('Found ' + results.items.length + ' results out of ' + results.total);
    console.log(results.items[0].title);
    console.log(results.items[0].authors[0].name);
});
```
