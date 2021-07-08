
# Metadata Selections

_PLEASE NOTE: It's difficult to talk about python class structures in the abstract, so for our purposes here I'm going to use json representations. That's **not** how it actually works, it is however an excellent way to conceptualise the structure you're working with._.

### 1.) Selecting your distribution

This is the most common action for working with metadata object and is universal step for all pipelines.

Think of an example scrape holding metadata much like the following.

```json
{
    "metadata": {
        "dataset": {
            "name": "dataset1",
            "distributions": [
                {
                    "title": "Import Data",
                    "issued": "1/2/2021",
                    "downloadURL": "www.foo.com/imports.xls",
                    "mediaType": "application/vnd.ms-excel"
                },
                {
                    "title": "Export Data",
                    "issued": "1/1/2021",
                    "downloadURL": "www.foo.com/exports.csv",
                    "mediaType": "text/csv"
                }   
            ]
        }
    }
}
```
The trick is to use the metadata fields within each distribution to filter down to the single distribution you want to work with.

You could select the **first distribution** from the above via any of these example commands

```python
distribution = meatadata.distibution(title = "Import Data")
distribution = meatadata.distibution(title = lambda x: "Import" in x)
distribution = metadata.distribution(medaType = "application/vnd.ms-excel")
distribution = metadata.distribution(latest = True)
```

_Note: when you run gssutils via a notebook you'll notice it generates multiple markdown previews (please see [this example](https://ci.floop.org.uk/job/GSS_data/job/Trade/job/DCMS-Sectors-Economic-Estimates-Year-Trade-in-services/63/Transform/)). The purpose of the previews is to let the DE know which fields we can use for filtering to the required distribution (in this case, title and mediaType)._

### 2.) Working with a metadata catalog

_Note: you'll know if you're working with metadata in a catalog structure, gssutils will tell you via the markdown preview._

Metadata (broadly) comes in a structure like the following (I'm using json to represent this so the keys are **not** accurate, but this should suffice to get the principles across).

think of a catalog of being structured like this

```json
{
    "metadata": {
        "dataset": "",
        "catalog": [
            {"name": "dataset1", "distributions": ["<LIST OF DISTRIBUTIONS>"]},
            {"name": "dataset2", "distributions": ["<LIST OF DISTRIBUTIONS>"]},
            {"name": "dataset3", "distributions": ["<LIST OF DISTRIBUTIONS>"]},
            {"name": "dataset4", "distributions": ["<LIST OF DISTRIBUTIONS>"]}
        ]
    }
}
```

When you apply for example `select_dataset(title="dataset1")` command you are altering it in place to eg:

```json
{
    "metadata": {
        "dataset": {"name": "dataset1", "distributions": ["<LIST OF DISTRIBUTIONS>"]},
        "catalog": []
    }
}
```

From the point, can you apply the distribution selection logic exactly as detailed earlier.