# jupyter_drill
A module to help interaction with Jupyter Notebooks and Apache Drill

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ouseful-PR/jupyter_drill/binderise)

---

## TH

static downloaded from apache drill site:
svn export https://github.com/apache/drill/trunk/exec/java-exec/src/main/resources/rest/static drillstatic


?? Not sure if this is working atm. 

- Apache Drill can be started on command line with `apache-drill-1.15.0/bin/drill-embedded` and seems to work
- the html UI exposed via `jupyter-server-proxy` (*Binder URL+*`proxy/8047` or *Binder URL+*`proxy/8047/`) has broken styling
- `pyDrill` seems to connect once it is started:

```
!pip install pydrill
from pydrill.client import PyDrill
drill = PyDrill(port=8047)
drill.is_active()


!pip install pandas
import pandas as pd

df= pd.DataFrame({'a':[1,2,3]})
df.to_csv('test.csv', index=False)
df


q='SELECT * FROM dfs.`/home/jovyan/test.csv`'
drill.query(q).to_dataframe()
```

The `%drill connect` invocation throws an error if we just go with entering empty defaults (default connection is probably http://localhost:8047` ).

---

###
This is a python module that helps to connect Jupyter Notebooks to Apache Drill. It uses the requests module to make request via the Drill API and brings back the data as JSON, and the imported into a Pandas dataframe for use. 



After installing this, to instantiate the module so you can use %drill and %%drill put this in a cell:

```
from drill_core import Drill
ipy = get_ipython()
Drill = Drill(ipy, drill_pin_to_ip=True, drill_rewrite_host=True, pd_use_beaker=True)
ipy.register_magics(Drill)
```
