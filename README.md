# flask-das
An implementation of a dynamic advanced search **form** based on Flask, Flaks-wtf and Vanilla Javascript.

![](form.gif)

## Getting started
This repository is not a module but an example of a possible implementation.

To test it:

```
git clone https://github.com/giacomomarchioro/flask-das
cd /pathto/flask-das
pip install -r requirements.txt
flask run
```
The code example is not linked to any database the aim of this repository is 
only to create a dynamic form for adding multiple conditions, not to provide query
mechanisms.

Two versions of the `index.html` file are provided: one with the embedded javascript
the other pointing to the Javascript in the static folder. 

The `form.data` for the example shown in the gif will have the following structure:

```
{'conditions': [{'booleanoperator': 'and', 'filteroperator': 'contains', 'searchtext': 'this word'}, 
                {'booleanoperator': 'and', 'filteroperator': 'contains', 'searchtext': 'asfd'}],
'csrf_token': 'ImYzNjRiZWNlYzliMDEzZDlmMWUyMTc4YWFmYzJlMWQzNWQwNmI2YmMi.YihUvA.R_RpR5vN7RLM5UXKqXnFoQPXYkU'}
```

## Acknowledgments
This [blog post from
Rafael Medina](https://www.rmedgar.com/blog/dynamic-fields-flask-wtf/)  helped me in the creation of the dynamic form.