# jupyter_drill
A module to help interaction with Jupyter Notebooks and Apache Drill

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ouseful-PR/jupyter_drill/binderise)

---

## TH

static downloaded from apache drill site:
svn export https://github.com/apache/drill/trunk/exec/java-exec/src/main/resources/rest/static drillstatic

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
